import java.util.*;
import java.io.*;

public class Main {
	static int n, m, answer;
	static int[][] graph;
	static int[] dx = { 1, -1, 0, 0 };
	static int[] dy = { 0, 0, 1, -1 };

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());

		m = Integer.parseInt(st.nextToken());
		n = Integer.parseInt(st.nextToken());
		graph = new int[n][m];

		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(bf.readLine());
			for (int j = 0; j < m; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		answer = bfs();

		System.out.println(answer);
	}

	public static int bfs() {
		Queue<int[]> q = new ArrayDeque();
		int count = check();

		if (count > 0)
			return 0;

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (graph[i][j] == 1) {
					q.add(new int[] { i, j });
				}
			}
		}

		while (!q.isEmpty()) {
			int[] loc = q.poll();
			int x = loc[0];
			int y = loc[1];

			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];

				if (0 <= nx && nx < n && 0 <= ny && ny < m) {
					if (graph[nx][ny] == 0) {
						graph[nx][ny] = graph[x][y] + 1;
						q.add(new int[] { nx, ny });
					}
				}
			}
		}

		count = check();
		if (count > 0) {
			return count - 1;
		} else {
			return -1;
		}
	}

	public static int check() {
		int num = 0;

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (graph[i][j] == 0) {
					return -1;
				} else {
					num = Math.max(num, graph[i][j]);
				}
			}
		}
		return num;
	}
}
