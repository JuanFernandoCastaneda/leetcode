import kotlin.math.max
import kotlin.math.min

fun main() {
    val t1 = arrayOf(intArrayOf(-2,-3,3), intArrayOf(-5,-10,1), intArrayOf(10,30,-5))
    println("t1 " + calculateMinimumHP(t1))
    val t2 = arrayOf(intArrayOf(0))
    println("t2 " + calculateMinimumHP(t2))
}

fun calculateMinimumHP(dungeon: Array<IntArray>): Int {
    val minMatrix = Array(dungeon.size) { Array(dungeon[0].size) {Double.POSITIVE_INFINITY} }
    return minHp(dungeon, Pair(0, 0), minMatrix).toInt()
}

fun minHp(dungeon: Array<IntArray>, cell: Pair<Int, Int>, minMatrix: Array<Array<Double>>): Double {
    val (cellRow, cellCol) = cell
    val cellValue = dungeon[cellRow][cellCol].toDouble()
    val downCellValue: Double = if (cellRow+1 in 0..dungeon.lastIndex) {
        if (minMatrix[cellRow+1][cellCol] == Double.POSITIVE_INFINITY) {
            minHp(dungeon, Pair(cellRow + 1, cellCol), minMatrix)
        } else {
            minMatrix[cellRow+1][cellCol]
        }
    } else Double.POSITIVE_INFINITY
    val rightCellValue: Double = if (cellCol+1 in 0..dungeon[0].lastIndex) {
        if (minMatrix[cellRow][cellCol+1] == Double.POSITIVE_INFINITY) {
            minHp(dungeon, Pair(cellRow, cellCol+1), minMatrix)
        } else {
            minMatrix[cellRow][cellCol+1]
        }
    } else Double.POSITIVE_INFINITY
    val hpNeeded: Double =
        if (cellRow == dungeon.lastIndex && cellCol == dungeon[0].lastIndex) {
            -cellValue + 1
        } else {
            min(downCellValue, rightCellValue) - cellValue
        }
    minMatrix[cellRow][cellCol] = if (hpNeeded < 1) 1.toDouble() else hpNeeded
    return minMatrix[cellRow][cellCol]
}