SIMPLE_TEST_0 = """...>...
.......
......>
v.....>
......>
.......
..vvv.."""

SIMPLE_TEST_1 = """..vv>..
.......
>......
v.....>
>......
.......
....v.."""

SIMPLE_TEST_2 = """....v>.
..vv...
.>.....
......>
v>.....
.......
......."""

SIMPLE_TEST_3 = """......>
..v.v..
..>v...
>......
..>....
v......
......."""

SIMPLE_TEST_4 = """>......
..v....
..>.v..
.>.v...
...>...
.......
v......"""


TEST_0 = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>"""

TEST_1 = """....>.>v.>
v.v>.>v.v.
>v>>..>v..
>>v>v>.>.v
.>v.v...v.
v>>.>vvv..
..v...>>..
vv...>>vv.
>.v.v..v.v"""

TEST_2 = """>.v.v>>..v
v.v.>>vv..
>v>.>.>.v.
>>v>v.>v>.
.>..v....v
.>v>>.v.v.
v....v>v>.
.vv..>>v..
v>.....vv."""

TEST_57 = """..>>v>vv..
..v.>>vv..
..>>v>>vv.
..>>>>>vv.
v......>vv
v>v....>>v
vvv.....>>
>vv......>
.>v.vv.v.."""

TEST_58 = """..>>v>vv..
..v.>>vv..
..>>v>>vv.
..>>>>>vv.
v......>vv
v>v....>>v
vvv.....>>
>vv......>
.>v.vv.v."""


INPUT = """.v.v.v>...>vv>v>>>.v>..v>.v.>.>v>.v.v.>>v...>.>....>.>vv>>>.....>>...v.>>v..>..vvv.>v...vv...>..>....>.>.>.>vvv....>..vv>v....>v...>>....v.
>.v>..v.>>vv.>>v...v.>.>..v.>.>.>vvv..>>>.>...>v>.>>v....>>>>...>v.v>.v>....>>>v.>>>....vv.....vvv.v.v..>.>..v>>.>.v>.>v>.vvvv.v..v>>..>>vv
.vv>>...v>..v..v>v.>vvv.v.v>>.....v>>.......>...v>.v>.v.vv.v.>v>v.v......>>......>.v...v........v.v........>.v.vv.>>.v.>>.>.>...v....v>>>..
.>.>v.>vv.v...v.>>v>.>v..vv>..v.v.>...v....>vvvvvv>>>v..vv.v.v>>.>>.>>v>v>>..>.v...v.v.>v..>...v.>.>>.v...v>..v...vv.>v.....vvv.v>.v>..>>v.
..>.....v.>>..>>.v>v.>.>>.>..vv.v>>.>..>.>..v>>...>.>>.vv>>>..>>>>.v.>....>>.>..v>>vv>.>>v>vvvv>vv..v.v.>.v>..v>.vvv>>.v.......>>.>...>>.>.
v...>..>..v>.vv.>>.>...>>....v.......v>...v.vvvvv>..v...>.v.>.>>v>v.>....v>...>...v.>.vv>......vv>.v>vv>>....v>.v>.>..>v.v..>>>.>>>..v..>vv
v>v>.v>..v..v.>..>...>v.>..>.>vvvv...v.v>v....>.>v.vvvv....>...v.v..vvvvvv..v.v..v>v....>v....>v.>>.v>.>v..>...v.vv...>v>>..>.>.....v.v..v.
.......v.....v>v.vv.>.v>.>>.>v.....>>..v.v.v>v>.....v...>v.vv>>.vv>>>>.>>.v.>v>..v.v..>v.vv....>>.vv.>v...>>v....v.v.>.vvvv.v....>v>>>>v.>.
v>.v>..v...vv.>vv.v...v.v>.>........>.vv>>..........v...>vv....>.>v>v..>..>>>v.>>..v.>.>...v.v.>..v>>>..>v.....v.>>>>...v>>v...vv>..>>.v.>>
.v>>>>>>v.>.>...>.>>.>.>>v>.........v..>.v>>>v>.....>...>>.>.v..>.vvv.>..v.v..>.>..>v>v.>v......>>...>>v.vv.....>.>...>.....>v.v..>>v.vvvv.
v......>.......>>..>.v.>..v..>>v..>>......v>v.vvv.>...>>>...v..v>vv.....v.v>v>>v..v.v..v.......v.>v>.v.v..>.>..>v.v>>>v..v.>.>.>>v.>..v.v>.
>.v..>>....>.v.>...>>>..>.v..v>v..>>>.v..v....vv>vv.v.v..v...>>..>......>>..v.....v.v>>.v....v>>....>..>v.vv.>.>..v...v>>.>.>v.v.vv>.v..v.>
..v...>...v..v.v...>...>.v..>...v...vv>..v....v>>>v.v..v.v>v..>v..v..v>>vv.v>..v..v...>.......>..>.>v>v..>...>v.....v..>v>v...v>..>.>...vvv
.vv>.>.v...>>...v.>.>v.v.>>v..v.>v.>>vv.v>.>..>....v.>v>vv>..v>v>v.>>v>v.>...v>vvv..>>.v.>v.>vv.>..v>...>.v..>.>>>v>>...v>.>>v..v....v>v..v
..>.>>>...>........>.vvv>>.>v..v.>v..v..>v.>>.>.v..>.v...v>>.>v..vv...v.v>.vvv...vv>vv>v>.>vv>.>v.vv..v.v...v.>>..v...v>...v..vv..v..>.>>>>
..>.>.>v.v.>.....>vv.vvv>.>..v>>>v.>vv.>.v.>.....v>>.....>v..vvv....v.>.v>.v.vv>v.>vv.v..>v>>...v>v....v>>v>....v..>vvvv>..>v>.v..v.....>..
.vv>.....v>.>>>.>>v>>>v>>>v>.v>>.>v..>>v.vvv...>vv.v.v.v.....>>vv..v.>>>>v.>....v>v.>..>..vv>>>....vv.vvvvv>v....v...>.>.vv...v...>vv...>..
>...v.vv.vv.vvv..>v.>.......v...v.>v.>..>.v>..v...>v..>..>v.v..>.v>.>>.v>.>v...v>>.>v.v.v.v>.>..v.>vv.v>>>.>vv.vvv.>vv>>v>..v>>.vvv>v..v.v>
>v.>...>v.vv..vv>..v.v..>..v.>v>>>..vv...>.>.v.v...>>.>v.vv..>.v.>>.>.>.v>..>.>..v>..v>>.v.v.v>.>...v.v.vv.>>>.v>...v.v>..>>..v.v>vv>vv>>vv
vv.vv>....>..>...>>..v.v..v..v....v.>.vvv>>.v.v>.>.vv.>v......>vv>>.>>.....>>....>..v.v..v.v...>>v.>>>v.....v.>......v>v>v>>.v.vv...>.v....
.>v>....vv.v>>...>>....>>>.>.v>...vv.v.>vv>.....v>v.v....v..v.>v>.....>...>v>>....v.vv.v>>.>..v>.v.v...v..>..>>v.v>....v.>....v>......>v...
..vvvv>.>.>.v.>.vv....>>>v..>..v..v>vvv.>v.>>.>v.>.vv>vv.>......v...vv>v..v.v.vv>v.v..vvv>v..>>...>..>.>....>>v>....v.>vvv>>..>>>..v..v.>..
>.....>>..v>.vv.v>..>..v.>vv>>vv>.v>v..vv......>....>.....>.>v.vv.vvv.v..>.vv..>>...>vvvv>..>..>.>>.>v.vv>...>>vvvv.>.v.v...>...>v>..>v....
.v.>v..>vv.>v...>vv.v..vv>.>>.......>v>.vv..v.vv>v..>.>vv.v>>>.>>v>.>...v...vv.>>>v...>>..v>v>v.v.v>..>.v....>.v.v.>vvv.v.vv.>.v..vv.>>v>>.
....v...vvv>>>.>>.>v>...>.>v.v.>.vv>...v...>>v.v.>.v>..>...vvv....v..vv>vv>>>..>.>.>v....>..v.vv.v..v...>>>v..v.>.....v>>v>vvvv.>.>.v.>vv..
.>.>v..v>.v.v.v>v.>.vv...vv.>.>v>....v>>v..>....>>>.v>v.v>>..>.>vv..>.>..>.>>.........>>>>..>...vvv>.>.v.>v.v>...v.>vv..>.>v.>>vv.>>>v>.vvv
>..>>..>.>>>vvv.>....>>v.>..v>v>v....vv.>.>>>v..v..v>.v....v>>...>>v...vvvv>>>>.>.....v>v.v.v..>v.v..>.v.>v>>....>>>v>.v>v.>.v...>>>.>vv.>>
...>>..>..>.>v.v..vv>.>.>vv.v>>.>....>.v>..>.v>>.....v.v.v.v..>...>>v.>.v.v.>>.>v....>..v..v>>..>>.>.v..>>..>vv..vv>v.v.v..v.vv.vv>....vv..
.v.v>..>.>.v..v>>....v>....>v>>>....>......v..v.......>vvvv.vvv.v..>.>..>.>>v.v..>...>>vv>.v..v.v..>vv>..>>.>v.>.v...vvv>>..>.vv..v.>v.v>v>
v>.>.>.v>>v.>>v>.>.vv>.>>...>..>>>.v....>>>v>.v>v.>.v.>..>vvv>.v.>>....>v....v.vvv>..>.>.vv>>..>>v...vv.>.>>.v..v>.v.>.v..>.v>.v....v...>.>
>vvv>.v>..>>..>.vv>>>...>>v.>v..>v....v>vv.>..>.v.>....vv....v....>....vv.v...vv>>>.>..>>>.v....>>vv.vv>vv>>.v...>>>v.v...v.vv..v>.vv..>v>.
v.>...>>..>>v>..v.vvvv..>>.v>.v.>.vvvvv>v..v.v>....v..>>.>>..v.>.v>..v.>.v.vv>.>.>v.v....>v.vvv>>>.v>>.vvv..v..>.>...>.>..>.>...v..>>v.....
.>v.>>v>..vv.>.vv.>>...v.v....>>>v....vvv>.v.>v.>v.vv.>.....>..>>.vv.v.v.>..v.>...>>.>.....>>.>........v>...>.>>>.>v.>.v.>>.....vvvv.v.>v>.
>..v..>.>>>..>vv..v..>.v.v....v>...v>....>>...>v.>v...v..v...>.v>.>.>.vv...v....>>....vv.v>>....v.v.v....>v.....>.v.v...v>..>>..>..>>..>>v>
.>vvv.v>.>vvv>>vv>v>v..>...>vv.>..v>.....>.vv....>>...>>.>>>v..vv.>>.....>>.v..v.v>>.vv>..v.vvv...>>.>..v.v>.v......v...>.>..>..>v....vv>.v
.>v>...>...v..v>.v..v>v.v.>>.>vvv...v.>..............vv..vvvv>.>....>.>>..v.vv.>>.>.vv>...>>v.>.>.v..v>..v..>v...>.>..v.......>.>v.....>...
..v.>v>vv....v>>.v>vv....>.v>.>v.vvv>vv>>vv>..v>.vvv>.v.>v.>....v.>..v>v........v.>>>v..>>.>v>v...>>vv.>.v.>>.>..>..>vvv>.v.>vvvv.v>v.>v..>
.vv>>v......>...v>.vv>..v>>.v>v>>v>...>.>>.>.>...v...>>>>>vv>.>v....>v..v>>.>.vv>..v>>v>.v..v.v..v>......>.vv>....>v>..v>>.>.>>.v>v>v>>>v..
>v.v>.>...vv.>..>.v.>>.vv....>.....>v.v..v.>..>...>.v>v.......vv.v>.>vvv...>..>.>....>v...>..v...>v.......vv..>....v...>v.....>>v.>vv>.v.v>
v>..vv>.vv.v...vv...>......>v..>>.v>vv.v>>v..>v>..vvvv..>.>>.v..vv>.v>.>......>......>vv.v..vv>>..>..v..>v..>..>...>...>.>.........v.vv>v.v
.v>.>.......>.v.>.v..>>.>.v>...>..vv......v.v...>..v>>v..v..v...>>vv..v.v...v.v...v>vv>..v.>>>v.v.v>v..>vv>..v..>>>>...>.>..>.>>>.>>vv>>..v
.>..vvv.v>.v..>..v>>..v>v>>.>.>..v.>vv>.v.>>v>v.vv.....v.>v.>>>>vv>>>..>>...vv>v..vvvv>>>..v.v.>...v.....>>...>>..>.>.>v..>..>...>..v.v>..>
vv..v>.v....v..v>.......>vv..>vv>...vv...v>>vvv>v...v.>v.v>v.>.v.v.>.>.>....v.>>>..>.v.......vv..v.vv>.v...v...>....vvvv>....>.v..v.>v..v..
>.vvv.>v....vv>>v.>..>.vv.>v>.v.>..>>v......vv>>>vv.v..vv.v.vvvvv>>.>>.>>v...v..v.>..>...>v>.v.v>vv>>.v.vv>>..v.>>>...>>.>v.v.>>..vv>..>.v.
..v.v>..>v>..>.......>>.>>>v..v.>....>.v..v>...>v>v.>.v.>.v...>....vv..>..v.>......v...>vvv>..v..v....v>...v.>.v......v>vv..>.vv...vvv.>vv.
vv......vvvv.>>.>v>.>.v>.vv>v>.vv>....v....v.v.>vv>vv.>>.>.v>v...v.....v.>..>....v.>..>..v.....v.v>>v>.v.>..v>..vv.v.>>...>.vv>....>v.v>>..
v>.>>.>.....vv.>v>>.v>..>v.>..>>.v..v.>.>.>>.vv>..v..vv.>>v..>.>........v....v>>v.v.>v..>.>v......>..>.>.v.>...v>..>v>..v.>v>v..>vv>..v.>>>
v..v..>...>.v..>>...>.>v..>v.v.vv.v..>..v..>.v.>>v.>..v.>..v>..>.>vvv..v.>.>>.v.v..v>.>v.>..>v..v>>v>>......vv.>.>.v.>>v......>v...>v...>>.
.>..>...>...v.....>.....vv.v.>v.>.>..v....v>>...>.>.v..>>>...>v.v..>...>vv>..>v>.v.>>.vvv>>v>v.......v.vv...>>>..v...v.>v..v.>..>vv>..>.v>.
....>vv.>..>.>>.v..>.v.>..v..>..v.>>.>v..vv.v>>>v.....>>...>v>......>.>v>.v.>.vv>.vv>.v.>>..v>..>vv.v..v...>vvvv>>..>..v......v>..v.v.v>.>.
....vv>....v....>...v>..v>.>.>.>v..>.v>.......v>..v.vvv.v.>..v.>v>.>vv.v.>vv>.>>v.v..v.v...>vvv.......>v>v.v..>.v>.v>vvvv.>.>>>.>..vv.>v..>
..>.vvv>.>vvv>>>vv.>..>v.v.vvv>..vv.....>v>>..vv>.....>...>.v>.v>>.>.>vv..v...v..>.>>..>>.>.vv>v>>>vv....v>.>>..>..vv>.>>..>v>.v.v.v..>...v
.>.v>............v>v.v......vvv>.vvv>v.v.>vv..>>....v.>.vv.vv..>..>>>>v.....>.>.>..v.>.>..>.vv.v.v......>>.>>>.>>.v..>v>v...v...v>...vv>.>.
>>.v....v..>..v>>v....>...v.v....v.>..>.v>v.>v>.>>v.....>.v.>>.>>>..>.v.v.>>vv>>.>..>>v...>.>.v.vvv>>vv.vv>.v.>.>.>vv.v..>v>.>.vv>>>v..v>.v
>v..v.v.>..>>>>..>>v.v>.v>..>>....v.....>..>.>v>...>>.v>....vvv>....>v.>.v.>.>v>.>v>>.>v>v..>.....v>.vv..v>>...>>v....>v..v>....>...vvv.v>.
.>.v.....>..>.>vvv.>v.>vv.>..v..v.v.>vv>.>..>.>>>.....>v......>v.>....v..>.>..v>v.>..>.>v..>.v.>v>v>...v.v.>.v.>vvv>vv..>.v..v>..vv..>..v>.
.v>.v>v>.v..v>.v..v.>............>v.>..>..>>.v..v>v>vv>>.>v.>>.v..v...v....>.v..>vv.>.....>.>>.vvv..>>..vv>>v>.....>>.v>...v.vvv>>..>..v.v>
v...>..>...v.>>.v...>..v>v...>vv.v..>vv>..vv>>.v..vv.v>v.>>..v>v.v..>.......v...v.v>...>v.v......v.vv>...v.>..>vv>v.v....v.v.vv.vv.vvvv.>v.
.>.v>>....>....vv..>vv>.>..vv.>>...>....>vv.vv...>.vv>v...>>..v...>..v....>v.vvv...v>>.>>>>>v>..v>>vv>vv.>vv..v...v.vv..v>v.>.v.v>..v..v.>v
.>.v.v...v.....>..v>..v>.vv.v>...vv.....>v..>..>..>v.>.v...>.vv.....>.>.v.v>v....>..>>.vv.>vvvv..>>>.v...v...>v.vv>>.v..>v..>..>>.>..v>v..>
>..vv>>v..>.v>>>v>>.v..vv>....v.>vvvv.>...vv...>.v..>v.>v>.>v>v>>v.>.>...>>>.....v.v....v>...>..>.>v.>.vv.....>.>>vv.....>......>.v..>v>.>.
v.......>>.>..v>.v.>.>v..>>.>.>vv..>v.v...>.v>..v....v..v..>.>>...v..v>.vv.>v>>.>....>vv>.v.v.>..vvv.v.>.v>.v>v..>.>>.>.>..>.>...vvvvv.v>..
>..v.v>.>>v.>>...v.>v.....>.v.>.v>v.>v>.vvv>.>>..>v..v.v.>...>v....>v.v.v>>...>.vv>.>v.vv....v>..v>>v.>.>..v>v..>v>..>.>>.v>.>..>..>..v....
.>vv.>.v>>>.>.>.v>v.>..vv>..>>>.>>...v.....>v.v..>.>.>>.v.>.>v>.>v.v..vvvv>.....v.v..vv....v.>...>.vv.>>v.....>.>vv>...v....>v..>v..vv.>>>v
v..>>>v.>..v>.v.v.>.>..>..>>..vv.vv.>.v.v..>v>v.>>>.>.>>.>>.vvv..>...>>..>.>..vvv>.>..v.>.>.v>v>.>v..>.>.v>....v..>..v.>v.>>.v.v..v>v..>v..
....>v...>....>.v>>vv.....vv>..vv.v....vvv>>...vv.v.v.>......v.v>>v..>.v>..v>v.v..>....>....v.vvvv>v..v>v>v>v.>>v....v.>vv>>v>vv>>>.>..>.v>
...>>>.v.v.....v>vv>>v>.>..v.v>v>....v>>vv..vv>v>..vv...>.>v>.>v..v...>.>vv..v.>.v..v...>...v>...v.vv>vv>..v....>.v....v.v>..>.....v..v..v.
.>vv.v..v>..vv....>.>>>>..>>>>..v....>.>v.vv.v.>>.>vvv..vv..>vv.>>v>>v.v..>.....>>v>..v..>>v>vvvv...>.>v>..v..>v>...>>.>vvv.v.>vv.>..v>>...
>>.>...>v.>vv>v>.>.....>.vv.>.vv>.>>.>.>...........v>.>..>>.>.>>..v.v>>v.vv>v>.>v.>..v>vv>.>>.v>>.>.v>v.v..>v.v>.v>v>>.v.>v.>>vv...vv.vv...
>vv>>.>...>v.>v>...>v>.v.>...vv....vv>v>.>..>.v.v.vv.v.>v......>..>.vv..v>.>>.>v>...v.vv..v...>vv.v.v...>>.>.>.v..v..>.vvvvv>>>>v>vv.v.v...
>v>>>.v>..vvvv..vv>...>.>.v>>>..v.v>>.v..v>.v.....>v>>.v..>..>.....>v....>.>..>......>v>.>.v.>..v..vvv>>v.v..v>..v.v.>>>>>>>vvvv.vv.>vv..v>
..v..vv>v>v...v...>.vvvv.v.....v..>.>..>....v.....v>.>>..v.v.vv..>....vv>vv>v>>.>>v>>.>.vv.>..>>v.v>...v>.v...vv.>v....v.>>...>v.>.vv.>.vv.
.v>v..>vvv.vv>v>>>..v..>v>.vvvv.>.>.vvv>.>..vv.>v...>...>v..>..>......v...>.v..v>>.>v...>>>>.....>>>..>vv.>>>v.>v..v>>vv.>....>..>>vv.>.>..
v.>...>vvv>...>.>.v>.v..v..v>.v.>.v>.v...vvv..>.>>v>...>.>>v>>.v.>v...>>.v.v..vv..vv.>.>v.>.v.>>>.>.vv...v.v>.v.>>>>>>..vvvv..>....>..>.v..
>v..>v....v.v....>vv.>.>.>v>.>v>v.v>>>.>v...>>>.v..v.v.v>v......>vv.v..>......>v>.v>>.vv>>>...vvv.v..>.>.........v.vv>.>vv.vv>v.v.>.>vv..v.
>.v>.v.v>v..vv.v>v>.>>....vv..>.vvv>v..>>>>vv.v>....>.vv.>...>>>...>v>.>...v..v>v...>..v...>.v..v>.v...v.....>vv........>....v>v..v.>..>v..
>...>v......v>.>v...>.v...>>v.v>..>v...v.v..v>.>.v>.>...>vv.v>vvv.>..>..>...v...>>..>.>v.>vv.v..>>.v.v.v..>.v>..v.>..v...>>v.>v>v.v.v.>..>.
..v>.>>v>>..>..vv>>..>.>>vv..>..vv....v.>v>.....>v>..v.v>.v..>...vv..v.>>vvv...v>v>.>.v.>>>.v>...v>.>v.v>v>..>...>....>>>v..v..>>...>.v....
....>...vv.>...vvv>v..>vvv>>..>>>>......>>>.v..v>vv>v>.>....>.....v.v..v.v.....v.v..v.v..v>.>v>v>.>.v.>v>....vv.v..>.vv..>..vv>.>v.>.......
vv.>.>...>vvv.>v.>v>.>.>.v..v>..>.>>.v>.v>.v.v..v>v...v..>>.>>.>.>....v.>..>>vv>....>..>>...>>v.>.v>>..>>...vv.v.v.>>..v.v...v.v>..v.v..vv.
.>v.v..v.v.>.v.....>.v...>.vv>.>....vv.v.v..v>.v>v>>>.v..vv.>vv.v....vv..vv.>>>v>.v.......>.vv.v..>v>v...v...>..>vv....>.>.>.>>v...v..v>>.v
...>v.>>.vv...>v.v.v>...v.>vv..v.v...>>>>..>.....>.>v.v.v>.v.v>.>>.>...vv..v....v>.v.vv..>.v>...>>..v.v.v.v>.v.v>v.>..v.>v..>>..>vv.......v
>....v..>..vv.>.v>..>.>.>.>>v..vv.>vv...>>v.>.vv.v.>.v..>vvv>.v...vvvv>vv.>>>.>>..v.>v>>>..>>.>.v>>>v>>>..v>>.>.v.>...v.....v..>..>>.>v>..v
>..vvvv>>..v>v>......>...v>...>>>...>.v>.>.v>.>>....vv..v>>>vv..>>>v.v>.>.v..>.v>..v>....vv>.>.v.....>v>.>.>.v>v.>.>v>v....v.>...>.v.......
.v...v.....>>v.>vv.>v.>>.>.v>>.v...>>.v..v.vv>>.v...>>>v.>v>>..>>...vv.v>v.>..>v>.>v>>..>>.v...>..>.>..vv.....>>.>.vv>v>>.>..vv>.v.>v.>.v>v
.vv>...v.>.vv.>>...v..>.vv...>.v.....>>..v..>v.>.>...v>..>v.v>.v.>v....>..>..>..>.>.>.>.>..>.>.>.>..v..v>>v.>.v>>.....v..>.v.....v>..v....v
.....v>v..vvvv...v>..>.v.vv.>.>.......v.>..v..vvv.....vvv..>...>.v.>v.>v..>....v>.>>...v>...v>..v>v....v...v.v.>.>v>...v.vv.>...v.>>v>v>..>
>v...>...>..>.v.>>>>.>v.vv>vv>.>.>.......v>>v.>vv...>>.>..v..v>vv..>.>..>v..>v>>>.v>>v.>.>..>...>>..v..v>>v.>vv>>.vvv>..v.>vvv..>..v>vv..vv
..vv.>v...>>........v.....>>..>>..>........>>vv.>.>.....vvv.vvvv>>.>..v.>v>...v.v..vv...v.v..v..>>v...v.>>>>...vvv>>>v>...>vv>v>.vvv..>v..>
..>.........vv.>....v>>.>>vv....>>vv....>..>.>...v..vv.v>..>v>.>v>>.>>>...vv>.......v..v>v>.>.>vvv.>...>.v.>>v>.v>>....v..v........vv.>>.vv
..v.>>v.v..>..>>.v..>.v>>>...>..vv>v.>...>...v.vv>.>.v>..>v.vv.......v...vv>.>vvv.>...>>.v.vv...>..vv..v>...v...>>>....>.>v.>.v...v......vv
>vvv>.vv..>>.>....v..v>>>>v.>.>v....v.v...>>>..v.>..>v..>.vvv..v>.v>.v......>.v.v>>v.v.>.v...>.v.>vv.v>v..>..>>>.>v>>.vvv>>vv>.>v.>..vv.vvv
>>>..>v.v>.vv.v>v>vv...v........v>.>.....v>v..v.>>>.>v..vv..>....vv.v>..v....>>>>vv...>v..v>.v.vv.>..>vv.vv...>>..>>.....vv..v>>..>....vvvv
v>......vv>>.vv..v>v.v>>..v...>.v.>...>>..vv.>...vvvv.>v.>...>v.vvvvv..>>.....>v.>....>....>.>.>v..>.v.vvvvv..v..>vv.v>.v.v...>v.>..v>..>..
.v>>>>..vvv>v.vv>.v>vv..vv.v.vv.>>v>.>..>.v>v....>....v>>>.>.v.vvv.>>...v..>v>...v.v>>v>>v.v...v.v...vvv>>v.>.>...>v..>....>>.>..>.vvv>.v>.
>>.v...>.v>...v>v..v.vv.v..v.v.>...v>v.>.>>.v.>.v>>>.>>.>..>....v..v>>>.v>>.>..>>.>.vv.>>.vv.>>>v>.>>.>.v....v>....>..vvvv....v....v.v.v>vv
>..v>vv>.>v.>.....v.>vvv>..>.>.vv>>>..>.....>..>v>.v...>v..>...v...vv..v>>>v.>>..vv>>..>.>>>v.>..>v...v.v..>.>..>.>>..>.v.v>....>...v...v..
>.>.v...v..vv.>>>vv.vvv..>...vv.vv>...v.v>>>>.>.>>v.>..vv...>v>>v>..>..>vv..vv>>.v>>...>.>v...>..>.>>>.......>.>>.>.>....v.v.............>v
...v>.vv..vv...>v>..>>.v..vv.>.v..v..>..>>.>vvvv.vvv.>>vv>v>.>>v>..>...v>...v...v>>.>..>.>.>v>.v..>>......>v...>v>v.>>.....v>..>.>>>>v.v.>>
.v..vv>....>>...v>.v.v.>.>>....>..v>>.v>v..>......>v...v.>.v......v..>v..>....v.vvv.v..>vv..v.>..v..>>>....>>>>v.>.....v>>.>..v..v>v.v..>..
v>......v..v..v>.....>v>>.>v>v>.>>v>v>v>>...>.....v>.v>...v...v.....>>...v...>.vv..vv..>.>>...>v.>.vv>..v.v>..vv..vvvv.>v..>....v>.>..vv.>>
>.>..v>v..>.vv>>.v>>>>>v>....v.v.>vv..>>...v>v>v.vv>.>>>..>.>v.>>v......>>.>v..v>.vv...vv.v.vv>.>....>.>v...>.v..>.>..vv>..>.vvv.>>>v.v....
>.>.vvv.v>.>vvv...v.>..>.v.>.......>.>....v..>..>...>v..>v....v..>v.v>v.v.>..v.vvvv>>v>.>>.>>>...>..>v>..>v.>v.v..v>>vv.>..v.v>vv...vv>..v.
.v>v.v..>...v>v>.>vvv.>.v.....v.>.>>..v>v>.v.>.>....>.v..v.>v.v>.>.v.vv..v>>v>vv....>>....>vv>v>v>>.v..>.vv..>>>......>>>>..v>v>v>.>>..v..v
..>v.vv..>>v>v.v.......vvvv>vv.v>.v...v>v>>.v>.>.v>..vv...>v.>...v.>v>..v>.vv>....>>..v.>.>vv.vvv.>....v...v>.>..vvv>.>>vvvv>>v....>..>>.>.
.v.v.>vv>.>...v...vv.....v...v>>.>v.>vv>.>>....>>...v.vvv..>>..v.>vvvvv>..v.>....>v.>.......v.>.v.v.>..>>v>vv>>vv.>v.>v>>..>.v>.vv..v..vv.>
...vv.v...vv....>..>..v.>>v>v.>.v...>...v>...v>>v...>v.>>.v...v>>v...>..>v..v>..v..>.v>.>.>..v...vv>v.>.vv>>>..>>>vv.>..vvv..v.>.>..vvv>.v.
.>>.v.>.>..v>..>v>..v>.v.v>>.vvv..vv.>v.>>.>.v.vv.v.vv>.>.vv>.>..v>>.>.v.>v..>>v...v..v>>.>.v>.>.>v..v.v.>>>vv.v.>...v..>v.....>vv..v>.>>>>
.>.....>v>>>>....v..>>>vv...v.>>>v..v>vv>>.>.v.>.>v>.v>v..>..v.v...v..v.>.>>...v.>>v.v>vv.v..>.v>.>>vv...v.v...>>....v.>..vv..vv....v>.....
..v>.>v..v>...v>.>..>...vv>v>vv.>...vv>>..v>.v.>....>....v..>v>.>...v>>vvv....v.v..v>.vv.v.vv.v..>v>>..>...>v>>....v.>>..v.>v.>v.>>v.v.v.v.
.>.v>>>v>.v.vvv...v>....vvvvv>>v.vv>>>>>....>.....>>...vv.>vvv..>.v..vvv.vv>vv>..vv>>vvv...>.>.>.>...vv>.>v.v.v..v>v..v.>.v>>.>vv.>...v.v.>
.>....>>vv.>>>>.>v.>.v..>.>>.vvv>..v..v>..>>.v>.>>>.v.v>>vvv>v...vv.vv..>....>.v..v.>.v>..v....v..vv>v>.>..>..>>>.>>>.v.vvv.v..v......vv.vv
.v.v>>>v.>v.>....>..>.>v.......v>>........vv.v>>>...vvv.>>.>.v.>v.v.>...>v.v.....v.v.>vv>.>>v>>..v>>>..v.v..v......>.v>.>.>>v.v.v.vvv>vv.>.
.>..>....>>.....>.>...v.v....>v>>>v.>.v>.>vv..>v>v>v.>>>>>>v.>>>>>.>.>>.v>......v.v.v.v...>.v..v...>..>>>>>.>.>..>.vv..v>.>..v>.v.v....v.>.
..v>>>>.>>>>....v>v..>>vv.>>..>..v>..vvv>.>..v.>...v>>..>.>>>..vvv.v..>.>.vv>...>vvvv>vv>>>vv..>...>v.>vv....>v.v>..>vv....>v>..v>.v.>v>>v>
.>>.>>>v.>.v>.>.v>.v.>......v...>.v.>..>.vv.>v..v>.v>.v..v...>.vv.v>>.>v.v..>v.>...>>...v.>>v.>>..>v...v.>...v>.>.v..v.>.>....v.>>>>v.>v.>.
>vvv..v.v>>..>..v.>vv.vv>..>vv.v.>...>v..v>>....>>...>>.>>....>...>v>..>>>..>...v.>v.v>.....>..v...>vvv.vv.>>.>v>v.v>v..v>...v..>>.>..v...>
>>.>>...>.>>>..v>>..>v..vv>>>>.v.>>v..vv..>.>..vv.....v.v.v.>..>>>....v.v.>v>>vv....>.....v>v..v>..vv...>..>>v..vv...v.....>vv..v>.>..>.>..
..vv>.v>.....v..>.vv>>...>v...>.v.v>>>........>vvvvv>>.>...>.v.v..v....>.>v>>.v.vv.v..v.vv.>.>v>.>v.>..vv...>>..>.....v...>>>v..v..>.v>>v>.
.vvvv>.>...>>.v..>...vvv>vvv..vv>.>v>.....vv.v..v...v.....>>>v.v>v>>.>v..>>>..>.>v..vv...>vv>.v.>.v..v.>>.....>v.>v>>.vv..v..>..>.>.v....v.
>v>>v...>..>.>>..v..vvv>...>>....>.>>....vv>...>......>..>>v...vv..>>>>>.>v.>.>.vv>>.>>vv....>.v>>..v>>...>v..>...vv..>.>..vvv...>.....>.v.
>..v>.>..vv...v.>>>.v>>.>....v.vv.>..>...>..v..>v.>vv.>..v..>.v.>...vv...v>>..>>vvv...>.>v.>.vv.>v..vv.>>vv.>>..>vv>.v.....>>...v..v.vvv.>>
v.v..vvv>...>v......v....>..>>>.....v>v>>>..v.v..vv.>.>>>>.>.v.>....v.>.>v>vv>vv>v..>.>.v.v>.....>..v>>v...v.....v...v.v.vv>>........v.>.v>
.v>>...>>v>.>...v.>>>....>v>>v.>.v.>>v.v>.>>...>.v.v...vv>v....v>v..>>.>v>.>..>vv.v>>.>..v>>v...>v>>>..v..>v>vv.vv>............>v..>vv.v.vv
>.....>vv.>...v>vvvv>vvv..vvv>.v.>...>v..vv>vv.>>>.v..v>v.>..vv.v.>>v....v...v.....>.v.>.>..>.v>..>v..>>>>>>>v..vv>.v.v>v.v>..>....>>>v>.vv
v.>.v>v.v>...>>>..v>..>>.>..v.v....>.>....v.>..>>>.>v.>.>.>vv..>.>...v.>.....>vv>.>..vv.vvv.>>.vv.>.....vvvv>..v.>.>>v..v..>.>>.>...v>>v..>
v..v>v>..vvv>...v..>.>>...v.v..v..>v..>>.>>.v..>>v...v.vv..v..>...v...v....>v.v.v.v.>.v>vvv.v.v>...>v>.>..>v.v>v>v..v..>>>>...>v.....v.>..v
v>v..v..>..v>.....>>>.v..>v>v..>..>v>...v..>....v...v>>vv.....v.vv...v>....v>..v>>.v.>.>>..>v>..>>>vv.>>>...>...v>vv>v>...>..v.v..>.....>>.
vv..>>v..>>>.>...v..v.>v>..v.>>>>>v..v>v>..>v>>>v.....v..>.>.>>vv.v....v.....>v......>.>vv..vv>.vv..vv...vv.v...>.v..>.>.v>v...v>..vv...>vv
.>...vv>>>.v.....v....>.v......vvvv>.>..>vv>v..vv..>v>>.>v.v>.v>v.vvvvv.v>v......v.>v>vv..>v..>vv.v.v.vvv..>.>.>>v.v.......>vv..v.vv>.>.v..
....v...v.>.v>>>v.>.....>>v>..v>.v.>.v.>..>v.>vv>>vv.>........v..>v>.v>>v>>v.>....>.>...>.>.v.......v....v>vvv..v>..>..v>....v...>.v.>.v...
..vvv.v>.>...>>.vvv>...v...>..>..>...v>v>..>>.vv....>.v.v.>.v>vv.>>v..v>.v.v..v.>.>>.v.....>.v...v>.....v....v.v.v.>>....v.v>>>.......>vv.v
...v>v>..v.v.v...>v>.vvv.vv..>..v.>v.>vv.>.>>..v....>.v.....>.v>..>..v>>vv..vv.>....v>>.v>...>.>vv....v>>.>>v>....>.v.v>v>>>>...>....>.>..v
.>>..v.>v..>>>v.v.v>>...>>v...v>....>.v>>...v.>.v.>...v>>vv.vvv>v....v>.v.>v......v.v.>>.>v...v...>vv.v.....>...>.>..vv.v..>..>.v>..>.v>.vv
>..>.>.>>.v.v.>.v.vvv....>.v>v.v..v.v...>...vv..>>.>..>>>...v>.>.v..v.>>.......v.....>.v>vv.>.v..vv>>>>>>v...vvv..vvv>>>.v.>.v..v.v>v>v>..>
v..>.v.vv>>vvvvv.....v>>v...vv....v>.>>v.v.>.>>v.vv....vv..v.>>.v.v.>v>....>....v.v>>>.>v.v.>v>v.v.v..>.>v>v......v.v>...>v.vvv...v>...vv..
>>vv.....v...v......>v.v..v>..v.v>..>>>.>>..>v>.v>>>.>v..>>>>v.>..vvvv.v>...v..vv.>.>v....>v.>>.....v>v....v..>.>.v>v.>.>.>v.v..>v........."""

MAX_COLS = len(INPUT.split('\n')[0])
MAX_ROWS = len(INPUT.split('\n'))


def next_col(coords):
    return coords[0], (coords[1] + 1) % MAX_COLS


def prev_col(coords):
    if coords[1] == 0:
        return coords[0], MAX_COLS - 1
    return coords[0], coords[1] - 1


def next_row(coords):
    return (coords[0] + 1) % MAX_ROWS, coords[1]


def prev_row(coords):
    if coords[0] == 0:
        return MAX_ROWS - 1, coords[1]
    return coords[0] - 1, coords[1]


def step(sc_map):
    cur_e = {k: v for k, v in sc_map.items() if v == '>'}
    cur_s = {k: v for k, v in sc_map.items() if v == 'v'}
    new_e = {next_col(coords): '>' for coords, typ in cur_e.items()}
    new_s = {next_row(coords): 'v' for coords, typ in cur_s.items()}

    new_sc_map = {}
    for coords, typ in new_e.items():
        actual_coords = coords if coords not in sc_map else prev_col(coords)
        new_sc_map[actual_coords] = '>'
    for coords, typ in new_s.items():
        actual_coords = coords if coords not in new_sc_map and coords not in cur_s else prev_row(coords)
        new_sc_map[actual_coords] = 'v'
    return new_sc_map


def to_map(text):
    sc_map = {}
    for row_idx, line in enumerate(text.split('\n')):
        for col_idx, ch in enumerate(line):
            if ch in ('v', '>'):
                sc_map[(row_idx, col_idx)] = ch
    return sc_map


def solve(text, nb_steps):
    sc_map = to_map(text)
    for i in range(nb_steps):
        sc_map = step(sc_map)
    return sc_map


def deadzone(text):
    sc_map = to_map(text)
    i = 1
    while 1:
        new_sc_map = step(sc_map)
        if sc_map == new_sc_map:
            return i
        i += 1
        sc_map = new_sc_map


##########################
if __name__ == '__main__':
    # assert solve(SIMPLE_TEST_0, 0) == to_map(SIMPLE_TEST_0)
    # assert solve(SIMPLE_TEST_0, 1) == to_map(SIMPLE_TEST_1)
    # assert solve(SIMPLE_TEST_0, 2) == to_map(SIMPLE_TEST_2)
    # assert solve(SIMPLE_TEST_0, 3) == to_map(SIMPLE_TEST_3)
    # assert solve(SIMPLE_TEST_3, 1) == to_map(SIMPLE_TEST_4)
    # assert solve(TEST_0, 1) == to_map(TEST_1)
    # assert solve(TEST_0, 2) == to_map(TEST_2)
    # assert solve(TEST_0, 57) == to_map(TEST_57)
    # assert solve(TEST_0, 58) == to_map(TEST_58)
    # assert deadzone(TEST_0) == 58
    print(deadzone(INPUT))
