/*
 * Tried to use a lot of constructs to learn features of the language 
 */
public class P38 {
    public static String countAndSay(int n) {
        String lastResult = "1";
        for (int i = 1; i < n; i++) {
            String newResult = "";
            Character lastChar = lastResult.charAt(0);
            int lastCharCounter = 1;
            for (int indexInLastResult = 1; indexInLastResult <= lastResult.length(); indexInLastResult++) {
                if (indexInLastResult == lastResult.length()) {
                    newResult += String.format("%d%c", lastCharCounter, lastChar);
                } else if (lastChar != lastResult.charAt(indexInLastResult)) {
                    newResult += String.format("%d%c", lastCharCounter, lastChar);
                    lastChar = lastResult.charAt(indexInLastResult);
                    lastCharCounter = 1;

                } else {
                    lastCharCounter++;
                }
            }
            lastResult = newResult;
        }
        return lastResult;
    }

    public static void main(String[] args) {
        System.out.println(countAndSay(1));
        System.out.println(countAndSay(4));
    }
}
