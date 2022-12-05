import io
import logging
from functools import reduce
import operator


TEST1 = """110100101111111000101000"""
TEST2 = """00111000000000000110111101000101001010010001001000000000"""
TEST3 = """11101110000000001101010000001100100000100011000001100000"""
TEST4_HEX = """8A004A801A8002F478"""
TEST5_HEX = """620080001611562C8802118E34"""
TEST6_HEX = """C0015000016115A2E0802F182340"""
TEST7_HEX = """A0016C880162017C3686B18A3D4780"""

INPUT = """005473C9244483004B001F79A9CE75FF9065446725685F1223600542661B7A9F4D001428C01D8C30C61210021F0663043A20042616C75868800BAC9CB59F4BC3A40232680220008542D89B114401886F1EA2DCF16CFE3BE6281060104B00C9994B83C13200AD3C0169B85FA7D3BE0A91356004824A32E6C94803A1D005E6701B2B49D76A1257EC7310C2015E7C0151006E0843F8D000086C4284910A47518CF7DD04380553C2F2D4BFEE67350DE2C9331FEFAFAD24CB282004F328C73F4E8B49C34AF094802B2B004E76762F9D9D8BA500653EEA4016CD802126B72D8F004C5F9975200C924B5065C00686467E58919F960C017F00466BB3B6B4B135D9DB5A5A93C2210050B32A9400A9497D524BEA660084EEA8EF600849E21EFB7C9F07E5C34C014C009067794BCC527794BCC424F12A67DCBC905C01B97BF8DE5ED9F7C865A4051F50024F9B9EAFA93ECE1A49A2C2E20128E4CA30037100042612C6F8B600084C1C8850BC400B8DAA01547197D6370BC8422C4A72051291E2A0803B0E2094D4BB5FDBEF6A0094F3CCC9A0002FD38E1350E7500C01A1006E3CC24884200C46389312C401F8551C63D4CC9D08035293FD6FCAFF1468B0056780A45D0C01498FBED0039925B82CCDCA7F4E20021A692CC012B00440010B8691761E0002190E21244C98EE0B0C0139297660B401A80002150E20A43C1006A0E44582A400C04A81CD994B9A1004BB1625D0648CE440E49DC402D8612BB6C9F5E97A5AC193F589A100505800ABCF5205138BD2EB527EA130008611167331AEA9B8BDCC4752B78165B39DAA1004C906740139EB0148D3CEC80662B801E60041015EE6006801364E007B801C003F1A801880350100BEC002A3000920E0079801CA00500046A800C0A001A73DFE9830059D29B5E8A51865777DCA1A2820040E4C7A49F88028B9F92DF80292E592B6B840"""


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def hex_to_bin_str(hex_txt, iostream=True):
    # From https://stackoverflow.com/questions/3258330/converting-from-hex-to-binary-without-losing-leading-0s-python
    bin_txt = bin(int('1' + hex_txt, 16))[3:]
    if iostream:
        return io.StringIO(bin_txt)
    return bin_txt


class Packet:
    def __init__(self, stream):
        logging.debug("Starting new packet")
        self.subpackets = []
        self._len = 0
        self.version = self.read(stream, 3)
        logging.debug(f"    v{self.version}")
        self.type_id = self.read(stream, 3)
        logging.debug(f"    id={self.type_id}")
        self.literal_value = 0
        if self.type_id == 4:
            logging.debug("    Looking for literal")
            self.number_as_text = ''
            while 1:
                num_block = self.read(stream, 5, keep_str=True)
                self.number_as_text += num_block[1:]
                if num_block[0] == '0':
                    break
            self.literal_value = int(self.number_as_text, 2)
            logging.debug(f"    Literal is {self.literal_value}")
            return

        # Operators
        length_type_id = self.read(stream, 1)
        logging.debug(f"    Length Type ID = {length_type_id}")
        if length_type_id == 0:
            length_subpacket = self.read(stream, 15)
            len_cur = 0
            logging.debug(f"    Length of {len_cur} / {length_subpacket}")
            while len_cur < length_subpacket:
                subpacket = Packet(stream)
                len_cur += len(subpacket)
                self.subpackets.append(subpacket)
                logging.debug(f"    Length of {len_cur} / {length_subpacket}")
            if len_cur != length_subpacket:
                raise ValueError(f"Subpackets didn't add up exactly to {length_subpacket} ({len_cur})")
        elif length_type_id == 1:
            nb_subpacket = self.read(stream, 11)
            for i in range(nb_subpacket):
                logging.debug(f"    Packet  {i+1} / {nb_subpacket}")
                self.subpackets.append(Packet(stream))

    def __str__(self):
        text = f"Packet v{self.version} id={self.type_id}. Version sum is {self.version_sum()}."
        if not self.subpackets:
            return text
        text += ' Subpackets are:\n'
        text += '\n'.join(f'\t{packet}' for packet in self.subpackets)
        return text

    def __len__(self):
        return self._len + sum(len(packet) for packet in self.subpackets)

    def version_sum(self):
        return self.version + sum(pck.version_sum() for pck in self.subpackets)

    def read(self, stream, nb, keep_str=False):
        self._len += nb
        if keep_str:
            return stream.read(nb)
        try:
            return int(stream.read(nb), 2)
        except ValueError:
            logging.error(f"Failed! Remaining stream = {stream.read()}")
            raise


def calculate_value(packet: Packet):
    if packet.type_id == 0:  # Sum
        return sum(calculate_value(subp) for subp in packet.subpackets)
    elif packet.type_id == 1:  # Product
        return reduce(operator.mul, [calculate_value(subp) for subp in packet.subpackets], 1)
    elif packet.type_id == 2:  # Min
        return min(calculate_value(subp) for subp in packet.subpackets)
    elif packet.type_id == 3:  # Max
        return max(calculate_value(subp) for subp in packet.subpackets)
    elif packet.type_id == 4:  # Literal
        return packet.literal_value
    elif packet.type_id == 5:  # GT
        return 1 if calculate_value(packet.subpackets[0]) > calculate_value(packet.subpackets[1]) else 0
    elif packet.type_id == 6:  # LT
        return 1 if calculate_value(packet.subpackets[0]) < calculate_value(packet.subpackets[1]) else 0
    elif packet.type_id == 7:  # EQ
        return 1 if calculate_value(packet.subpackets[0]) == calculate_value(packet.subpackets[1]) else 0


def test():
    assert Packet(io.StringIO(TEST1)).version == 6
    assert Packet(io.StringIO(TEST2)).version == 1
    assert hex_to_bin_str('EE00D40C823060', iostream=False) == TEST3
    assert hex_to_bin_str('38006F45291200', iostream=False) == TEST2
    assert Packet(hex_to_bin_str(TEST4_HEX)).version_sum() == 16
    assert Packet(hex_to_bin_str(TEST5_HEX)).version_sum() == 12
    assert Packet(hex_to_bin_str(TEST6_HEX)).version_sum() == 23
    assert Packet(hex_to_bin_str(TEST7_HEX)).version_sum() == 31
    assert calculate_value(Packet(hex_to_bin_str('C200B40A82'))) == 3
    assert calculate_value(Packet(hex_to_bin_str('04005AC33890'))) == 54
    assert calculate_value(Packet(hex_to_bin_str('880086C3E88112'))) == 7
    assert calculate_value(Packet(hex_to_bin_str('CE00C43D881120'))) == 9
    assert calculate_value(Packet(hex_to_bin_str('D8005AC2A8F0'))) == 1
    assert calculate_value(Packet(hex_to_bin_str('F600BC2D8F'))) == 0
    assert calculate_value(Packet(hex_to_bin_str('9C005AC2F8F0'))) == 0
    assert calculate_value(Packet(hex_to_bin_str('9C0141080250320F1802104A08'))) == 1


##########################
if __name__ == '__main__':
    test()
    packet = Packet(hex_to_bin_str(INPUT))
    print(packet.version_sum())
    print(calculate_value(packet))