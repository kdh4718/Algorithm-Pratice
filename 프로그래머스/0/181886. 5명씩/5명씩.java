class Solution {
    public String[] solution(String[] names) {
        int n = (names.length % 5 == 0) ? (names.length / 5) : (names.length / 5) + 1;
        String[] answer = new String[n];
        
        for (int i = 0; i < names.length; i += 5){
            int num = (int) (i/5);
            answer[num] = names[i];
        }
        
        return answer;
    }
}