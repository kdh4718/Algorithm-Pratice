import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> map = new HashMap<>();
        String answer = "";

        // 참가자 명단을 map에 추가
        for (String p : participant) {
            map.put(p, map.getOrDefault(p, 0) + 1);
        }

        // 완주자 명단을 기반으로 카운트 감소
        for (String c : completion) {
            map.put(c, map.get(c) - 1);
        }

        // 카운트가 1인 사람이 완주하지 못한 사람
        for (String key : map.keySet()) {
            if (map.get(key) != 0) {
                answer = key;
            }
        }

        return answer; 
    }
}