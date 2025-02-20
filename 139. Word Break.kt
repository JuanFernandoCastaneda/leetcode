fun main() {
    println(wordBreak("leetcode", listOf("leet","code")))
    println(wordBreak("applepenapple", listOf("apple","pen")))
    println(wordBreak("catsandog", listOf("cats","dog","sand","and","cat")))
}

fun wordBreak(s: String, wordDict: List<String>): Boolean {
    val plausible = Array<Boolean>(s.length) { false }
    for (i in 0..s.lastIndex) {
        val subWord = s.slice(0..i)
        // Base case. The whole sub-word is a word.
        if (subWord in wordDict) {
            plausible[i] = true
        // Recursive case. Check if the end is there.
        } else {
            for (word in wordDict) {
                if (subWord.takeLast(word.length) == word && plausible[i-word.length]) {
                    plausible[i] = true
                    break
                }
            }
        }
    }
    return plausible.last()
}