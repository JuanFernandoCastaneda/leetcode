import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

/*
 * Tried to use a lot of constructs to learn features of the language 
 */
class P2942 {
    public List<Integer> findWordsContaining(String[] words, char x) {
        return IntStream.range(0, words.length).boxed().filter(i -> words[i].contains(Character.toString(x)))
                .collect(Collectors.toList());
    }

    public static void main(String[] args) {
        P2942 solution = new P2942();
        System.out.println(solution.findWordsContaining(new String[] { "leet", "code" }, 'e'));
        System.out.println(solution.findWordsContaining(new String[] { "abc", "bcd", "aaaa", "cbc" }, 'a'));
        System.out.println(solution.findWordsContaining(new String[] { "abc", "bcd", "aaaa", "cbc" }, 'z'));
    }
}