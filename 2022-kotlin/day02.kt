import day2_data.INPUT_TXT
import day2_data.SAMPLE_TXT

typealias OutcomeHash = HashMap<String, List<Int>>

val OUTCOMES1: OutcomeHash = hashMapOf(
    "A X" to listOf(1, 3),
    "B X" to listOf(1, 0),
    "C X" to listOf(1, 6),
    "A Y" to listOf(2, 6),
    "B Y" to listOf(2, 3),
    "C Y" to listOf(2, 0),
    "A Z" to listOf(3, 0),
    "B Z" to listOf(3, 6),
    "C Z" to listOf(3, 3)
)

val OUTCOMES2: OutcomeHash = hashMapOf(
    "A X" to listOf(3, 0),
    "B X" to listOf(1, 0),
    "C X" to listOf(2, 0),
    "A Y" to listOf(1, 3),
    "B Y" to listOf(2, 3),
    "C Y" to listOf(3, 3),
    "A Z" to listOf(2, 6),
    "B Z" to listOf(3, 6),
    "C Z" to listOf(1, 6)
)

private fun part1(txt: String): Int{
    return eitherPart(txt, OUTCOMES1)
}

private fun part2(txt: String): Int {
    return eitherPart(txt, OUTCOMES2)
}

private fun eitherPart(txt: String, outcomeHash: OutcomeHash): Int{
    return txt.lines().sumOf { outcomeHash[it]!!.sum() }
}

fun main() {
    assert(part1(SAMPLE_TXT) == 15)
    println(part1(INPUT_TXT))
    assert(part2(SAMPLE_TXT) == 12)
    println(part2(INPUT_TXT))
}