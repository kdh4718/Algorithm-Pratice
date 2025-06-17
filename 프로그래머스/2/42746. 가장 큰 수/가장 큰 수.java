import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        StringBuilder answer = new StringBuilder();
        String[] numStr = new String[numbers.length];
        
        for (int i = 0; i < numbers.length; i++) {
            numStr[i] = String.valueOf(numbers[i]);
        }
        
        Arrays.sort(numStr, new Comparator<String>() {
            public int compare(String o1, String o2){
                return (o2 + o1).compareTo(o1 + o2);
            }
        });
        
        if (numStr[0].equals("0")) {
            return "0";
        }

        for (String s : numStr) {
            answer.append(s);
        }

        return answer.toString();
    }
}