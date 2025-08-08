import java.util.*;

class Solution {
    private String norm(String s) {
    StringBuilder sb = new StringBuilder(s.length());
    for (int i = 0; i < s.length(); i++) {
        char ch = s.charAt(i);
        if (i + 1 < s.length() && s.charAt(i + 1) == '#') {
            sb.append(Character.toLowerCase(ch)); 
            i++; 
        } else {
            sb.append(ch); 
        }
    }
    return sb.toString();
    }
    
    private int toMin(String hhmm) {
    String[] t = hhmm.split(":");
    return Integer.parseInt(t[0]) * 60 + Integer.parseInt(t[1]);
    }

    private String buildPlayed(String sheetNorm, int duration) {
    StringBuilder sb = new StringBuilder(duration + sheetNorm.length());
    int n = sheetNorm.length();
    if (n == 0 || duration <= 0) return "";

    for (int i = 0; sb.length() < duration; i++) {
        sb.append(sheetNorm.charAt(i % n));
    }
    
    if (sb.length() > duration) sb.setLength(duration);
    return sb.toString();
    }

    
    public String solution(String m, String[] musicinfos) {
    String[][] music = new String[musicinfos.length][4];
    String answer = "(None)";

    int bestDur = -1;
    int bestIdx = -1;

    String target = norm(m);

    for (int i = 0; i < musicinfos.length; i++) {
        music[i] = musicinfos[i].split(","); 

        String start = music[i][0];
        String end   = music[i][1];
        String title = music[i][2];
        String sheet = music[i][3];

        int dur = toMin(end) - toMin(start);
        String played = buildPlayed(norm(sheet), dur);

        if (played.indexOf(target) >= 0) {
            if (dur > bestDur) {
                bestDur = dur;
                bestIdx = i;     
                answer = title;  
            }
               
        }
    }

    return answer;
    }
}