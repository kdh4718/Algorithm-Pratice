import java.util.*;
import java.io.*;

public class Main {
	static int n;
	static boolean[][] graph = new boolean[101][101];
	static int[] dx = { 1, 0, -1, 0 }; // 오른쪽, 위, 왼쪽, 아래 순
	static int[] dy = { 0, -1, 0, 1 };

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(bf.readLine());

		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(bf.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			int d = Integer.parseInt(st.nextToken());
			int g = Integer.parseInt(st.nextToken());

			dragonCurve(x, y, d, g);
		}

		System.out.println(countSquares());
	}

	public static void dragonCurve(int x, int y, int d, int g) {
        List<Integer> d_list = new ArrayList<>();
        d_list.add(d);

        for (int i = 1; i <= g; i++) {
            for (int j = d_list.size() - 1; j >= 0; j--) {
                d_list.add((d_list.get(j) + 1) % 4);
            }
        }

        graph[y][x] = true;
        for (Integer direction : d_list) {
            x += dx[direction];
            y += dy[direction];
            graph[y][x] = true;
        }
    }

	static int countSquares() {
		int count = 0;
		for (int i = 0; i < 100; i++) {
			for (int j = 0; j < 100; j++) {
				if (graph[i][j] && graph[i + 1][j] && graph[i][j + 1] && graph[i + 1][j + 1]) {
					count++;
				}
			}
		}
		return count;
	}
}
