import java.io.*;

public class Main {
    static String word;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            word = bf.readLine();

            if (word.equals("end")) break;

            String quality = check(word) ? "is acceptable." : "is not acceptable.";
            System.out.println("<" + word + "> " + quality);
        }
    }

    static boolean check(String word) {
        if (!containsVowel(word)) return false;

        if (hasThreeConsecutive(word)) return false;

        if (hasDoubleLetter(word)) return false;

        return true;
    }

    static boolean containsVowel(String word) {
        for (char ch : word.toCharArray()) {
            if (isVowel(ch)) return true;
        }
        return false;
    }

    static boolean hasThreeConsecutive(String word) {
        int vowelCount = 0, consonantCount = 0;

        for (char ch : word.toCharArray()) {
            if (isVowel(ch)) {
                vowelCount++;
                consonantCount = 0;
            } else {
                consonantCount++;
                vowelCount = 0;
            }

            if (vowelCount >= 3 || consonantCount >= 3) return true;
        }
        return false;
    }

    static boolean hasDoubleLetter(String word) {
        for (int i = 1; i < word.length(); i++) {
            char prev = word.charAt(i - 1);
            char curr = word.charAt(i);

            if (prev == curr && !(prev == 'e' || prev == 'o')) {
                return true;
            }
        }
        return false;
    }

    static boolean isVowel(char ch) {
        return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u';
    }
}
