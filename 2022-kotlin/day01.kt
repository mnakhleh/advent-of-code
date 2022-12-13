import day1_data.INPUT_TXT
import day1_data.SAMPLE_TXT


private fun part1(txt: String): Int {
    return getSortedCalories(txt)[0]
}

private fun part2(txt: String): Int {
    return getSortedCalories(txt).take(3).sum()
}


private fun getSortedCalories(txt: String): List<Int>{
    val elfCalories = txt.split("\n\n").map{sumOfCalories(it.lines())}
    return elfCalories.sortedDescending()
}

private fun sumOfCalories(elfCalories: List<String>): Int{
    return elfCalories.sumOf { it.toInt() }
}


fun main() {
    assert(part1(SAMPLE_TXT) == 24000)
    assert(part2(SAMPLE_TXT) == 45000)
    println(part1(INPUT_TXT))
    println(part2(INPUT_TXT))
}
