import java.util.*;
import java.io.*;

public class Main {
    static int t, n, k, a, b, w;
    static int[] time, dp, indegree;
    static ArrayList<Integer>[] children;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        t = Integer.parseInt(bf.readLine());

        for (int i = 0; i < t; i++) {
            st = new StringTokenizer(bf.readLine());
            n = Integer.parseInt(st.nextToken());
            k = Integer.parseInt(st.nextToken());

            time = new int[n + 1];
            dp = new int[n + 1];
            indegree = new int[n + 1];
            children = new ArrayList[n + 1];
            for (int j = 1; j <= n; j++) {
                children[j] = new ArrayList<>();
            }

            st = new StringTokenizer(bf.readLine());
            for (int j = 1; j <= n; j++) {
                time[j] = Integer.parseInt(st.nextToken());
            }

            for (int j = 0; j < k; j++) {
                st = new StringTokenizer(bf.readLine());
                a = Integer.parseInt(st.nextToken());
                b = Integer.parseInt(st.nextToken());
                children[a].add(b);
                indegree[b]++;
            }

            w = Integer.parseInt(bf.readLine());
            System.out.println(acm(w));
        }
    }

    static int acm(int target) {
        Queue<Integer> q = new ArrayDeque<>();

        for (int i = 1; i <= n; i++) {
            dp[i] = time[i];
            if (indegree[i] == 0) {
                q.add(i);
            }
        }

        while (!q.isEmpty()) {
            int current = q.poll();

            for (int next : children[current]) {
                dp[next] = Math.max(dp[next], dp[current] + time[next]);
                indegree[next]--;

                if (indegree[next] == 0) {
                    q.add(next);
                }
            }
        }

        return dp[target];
    }
}
