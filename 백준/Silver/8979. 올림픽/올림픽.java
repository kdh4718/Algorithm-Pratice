import java.io.*;
import java.util.*;

public class Main {
    static int n, m;
    static int[][] medals;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        medals = new int[n][4];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(bf.readLine());
            int num = Integer.parseInt(st.nextToken());

            for (int j = 0; j < 3; j++) {
                medals[i][j] = Integer.parseInt(st.nextToken());
            }
            medals[i][3] = num;
        }

        Arrays.sort(medals, (a, b) -> {
            if (b[0] != a[0]) return Integer.compare(b[0], a[0]); // 금메달 내림차순
            if (b[1] != a[1]) return Integer.compare(b[1], a[1]); // 은메달 내림차순
            return Integer.compare(b[2], a[2]); // 동메달 내림차순
        });

        int targetGold = 0, targetSilver = 0, targetBronze = 0;
        int rank = 1;

        // m번 국가의 메달 정보를 찾기
        for (int i = 0; i < n; i++) {
            if (medals[i][3] == m) {
                targetGold = medals[i][0];
                targetSilver = medals[i][1];
                targetBronze = medals[i][2];
                rank = i + 1; // 1부터 시작하는 순위
                break;
            }
        }

        // m번 국가와 같은 메달 수를 가진 국가의 순위 찾기
        for (int i = 0; i < n; i++) {
            if (medals[i][0] == targetGold && medals[i][1] == targetSilver && medals[i][2] == targetBronze) {
                System.out.println(i + 1); // 1부터 시작하는 순위
                break;
            }
        }
    }
}
