import java.io.*;
import java.util.*;

public class Main {
    static int n, m, v;
    static boolean[][] graph;
    static boolean[] visited_bfs;
    static boolean[] visited_dfs;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        v = Integer.parseInt(st.nextToken());

        graph = new boolean[n + 1][n + 1];
        visited_bfs = new boolean[n + 1];
        visited_dfs = new boolean[n + 1];

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(bf.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            graph[a][b] = true;
            graph[b][a] = true;
        }

        dfs(v);
        System.out.println();
        bfs(v);
    }

    static void dfs(int v) {
        visited_dfs[v] = true;
        System.out.print(v + " ");

        for (int i = 1; i <= n; i++) {
            if (!visited_dfs[i] && graph[v][i]) {
                dfs(i);
            }
        }
    }

    static void bfs(int v) {
        Queue<Integer> q = new ArrayDeque<>();
        q.add(v);
        visited_bfs[v] = true;

        while (!q.isEmpty()) {
            int x = q.poll();
            System.out.print(x + " ");

            for (int i = 1; i <= n; i++) {
                if (!visited_bfs[i] && graph[x][i]) {
                    q.add(i);
                    visited_bfs[i] = true;
                }
            }
        }
    }
}
