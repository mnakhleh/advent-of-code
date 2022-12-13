import day3_data.INPUT_TXT
import day3_data.SAMPLE_TXT


private fun part1(txt: String): Int {
    return txt.lines().map{it.splitInHalf()}.sumOf { calculateTotalValue(it)}
}

private fun part2(txt: String): Int {
    return txt.lines().byThree().sumOf { calculateTotalValue(it) }
}

private fun intersectingChar(elfBags: List<String>): Char{
    return elfBags.map{it.toSet()}.reduce{ sum, element -> sum.intersect(element)}.toCharArray()[0]
}

private fun calculateTotalValue(elfBags: List<String>): Int {
    val overlap = intersectingChar(elfBags)
    if (overlap in 'a'..'z') {
        return overlap.code - 96
    }
    return overlap.code - 38
}


private fun String.splitInHalf(): List<String>{
    return this.chunked(this.length / 2)
}


private fun List<String>.byThree(): List<List<String>>{
    return this.withIndex().groupBy{ (it.index / 3) }.values.map{it.map{it2 -> it2.value}}
}

fun main() {
    assert(part1(SAMPLE_TXT) == 157)
    println(part1(INPUT_TXT))
    assert(part2(SAMPLE_TXT) == 70)
    println(part2(INPUT_TXT))
}