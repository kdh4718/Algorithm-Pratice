import java.io.*;
import java.util.*;

public class Main {
    static int n, score, p;
    static Integer[] scores;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        n = Integer.parseInt(st.nextToken());
        score = Integer.parseInt(st.nextToken());
        p = Integer.parseInt(st.nextToken());

        if (n > 0) {
            scores = new Integer[n];
            st = new StringTokenizer(bf.readLine());
            for (int i = 0; i < n; i++) {
                scores[i] = Integer.parseInt(st.nextToken());
            }
            Arrays.sort(scores, Collections.reverseOrder());
        } else {
            scores = new Integer[0];
        }

        if (n == p && n > 0 && score <= scores[scores.length - 1]) {
            System.out.print(-1);
        } else {
            int rank = 1;
            for (int i = 0; i < scores.length; i++) {
                if (score < scores[i]) {
                    rank++;
                } else {
                    break;
                }
            }
            System.out.print(rank);
        }
    }
}
