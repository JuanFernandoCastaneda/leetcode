import java.io.File
import java.io.InputStream
import java.util.LinkedList
import java.util.Queue
import kotlin.math.abs
import kotlin.math.min

fun main() {
    val elevation = mutableListOf<Int>()
    val inputStream: InputStream = File(".\\tests.txt").inputStream()
    inputStream.bufferedReader().forEachLine { line ->
        line.split(",").forEach { number ->
            elevation.add(number.toInt())
        }
    }
    test1(elevation)
}

fun test1(elevation: List<Int>) {
    val t1 = mutableListOf(0,1,0,2,1,0,1,3,2,1,2,1)
    println(twoArgmax(t1, 0..t1.lastIndex ))
    println(elevation.maxOrNull() ?: 0)
    println(twoArgmax(elevation, 0..elevation.lastIndex))
    println(rainQueue(t1))
    println(rainQueue(elevation))
}

fun rainQueue(elevation: List<Int>): Int {
    val queue: Queue<Pair<Int, Int>> = LinkedList()
    queue.add(Pair(0, elevation.lastIndex))
    var trappedRain: Int = 0
    while (queue.isNotEmpty()) {
        val (beginning, end) = queue.remove()
        // Si acabo de poppear algo que está pegado. Tipo 0-1 o 0-0. Retorno porque no me interesa calcular nada.
        if (end-beginning <= 1) continue
        val (imax, imax2) = twoArgmax(elevation, beginning..end)
        val minImax: Int = min(imax, imax2)
        val maxImax: Int = minImax + abs(imax-imax2)
        for (i in minImax+1..maxImax-1) {
            trappedRain += (min(elevation[imax], elevation[imax2]) - elevation[i])
        }
        queue.add(Pair(beginning, minImax))
        queue.add(Pair(maxImax, end))
    }
    return trappedRain
}

class TrappedWater(var quantity: Int = 0) {
}
tailrec fun rainRecursive(elevation: List<Int>, trappedWater: TrappedWater) {
    if (elevation.size <= 2) return;
    val (imax, imax2) = twoArgmax(elevation, 0..elevation.lastIndex)
    val minImax: Int = min(imax, imax2)
    val maxImax: Int = minImax + abs(imax-imax2)
    for (i in minImax+1..<maxImax) {
        trappedWater.quantity += (min(elevation[imax], elevation[imax2]) - elevation[i])
    }
    rainRecursive(elevation.slice(0..minImax), trappedWater)
    rainRecursive(elevation.slice(maxImax..elevation.lastIndex), trappedWater)
}

fun twoArgmax(list: List<Int>, indices: IntRange): Pair<Int, Int> {
    var imax = mutableListOf<Int>()
    var imax2 = mutableListOf<Int>()
    for (i in indices) {
        if(imax.isEmpty() || list[i] == list[imax[0]]) {
            imax.add(i)
        } else if (list[i] > list[imax[0]]) {
            imax2 = imax
            imax = mutableListOf(i)
        } else if (imax2.isEmpty() || list[i] > list[imax2[0]]) {
            imax2 = mutableListOf(i)
        } else if (list[i] == list[imax2[0]]) {
            imax2.add(i)
        }
    }
    if (imax.size > 1) {
        return Pair(imax.min(), imax.max())
    } else if (abs(imax[0]-imax2.max()) > abs(imax[0] - imax2.min())) {
        return Pair(imax[0], imax2.max())
    } else {
        return Pair(imax[0], imax2.min())
    }
}