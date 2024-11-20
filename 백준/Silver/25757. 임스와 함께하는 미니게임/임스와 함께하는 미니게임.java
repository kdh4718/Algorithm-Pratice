import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static String gameType;
    static String[] players;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        gameType = st.nextToken();
        
        players = new String[n];
        for (int i = 0; i < n; i++) {
            players[i] = br.readLine();
        }

		int result = calc();
        System.out.println(result);
    }

    static int calc() {
        int playerLimit = 0;
        
        switch (gameType) {
            case "Y":
                playerLimit = 1;
                break;
            case "F":
                playerLimit = 2;
                break;
            case "O":
                playerLimit = 3;
                break;
            default:
                
        }

        java.util.HashSet<String> uniquePlayers = new java.util.HashSet<>();
        for (String player : players) {
            uniquePlayers.add(player);
        }
        return uniquePlayers.size() / playerLimit;
    }
}
