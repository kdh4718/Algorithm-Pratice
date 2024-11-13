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
                if (st.hasMoreTokens()) {
                    medals[i][j] = Integer.parseInt(st.nextToken());
                } else {
                    System.out.println("Error: Insufficient data for country " + num);
                    return;
                }
            }
            medals[i][3] = num;
        }

        Arrays.sort(medals, (a, b) -> {
            if (b[0] != a[0]) return Integer.compare(b[0], a[0]); 
            if (b[1] != a[1]) return Integer.compare(b[1], a[1]); 
            return Integer.compare(b[2], a[2]); 
        });

        for (int i = 0; i < n; i++) {
            if (medals[i][3] == m) {
                System.out.println(i);
                break;
            }
        }
    }
}
