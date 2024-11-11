import java.util.*;
import java.io.*;

public class Main {
	static int n, m;
	static int[] dx = { 1, -1, 0, 0 };
	static int[] dy = { 0, 0, 1, -1 };
	static char[][] graph;
	static Queue q;

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());

		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());

		graph = new char[n][m];
		for (int i = 0; i < n; i++) {
			graph[i] = bf.readLine().toCharArray();
		}

		bfs();

		System.out.print("IMPOSSIBLE");
	}

	static void bfs() {
		q = new ArrayDeque<int[]>();

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (graph[i][j] == 'J') {
					q.add(new int[] { i, j, 1 });
				}
			}
		}

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (graph[i][j] == 'F') {
					q.add(new int[] { i, j, 1 });
				}
			}
		}

		while (!q.isEmpty()) {
			int[] out = (int[]) q.poll();
			if (graph[out[0]][out[1]] == 'J') {
				check(out[0], out[1], out[2]);
				moveJ(out[0], out[1], out[2]);
			} else {
				moveF(out[0], out[1], out[2]);
			}
		}
	}

	static void moveJ(int x, int y, int c) {
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (0 <= nx && nx < n && 0 <= ny && ny < m) {
				if (graph[nx][ny] == '.') {
					graph[nx][ny] = 'J';
					q.add(new int[] { nx, ny, c + 1 });
				}
			}
		}
	}

	static void moveF(int x, int y, int c) {
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (0 <= nx && nx < n && 0 <= ny && ny < m) {
				if (graph[nx][ny] == '.' || graph[nx][ny] == 'J') {
					graph[nx][ny] = 'F';
					q.add(new int[] { nx, ny, c + 1 });
				}
			}
		}
	}

	static void check(int x, int y, int c) {
		if (x == 0 || x == n - 1 || y == 0 || y == m - 1) {
			System.out.println(c);
			System.exit(0);
		}
	}
}
