import java.util.*;
import java.io.*;

public class Main {
	static int[][] graph;

	public static void main(String args[]) throws IOException {
		graph = new int[9][9];

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		for (int i = 0; i < 9; i++) {
			char[] c = br.readLine().toCharArray();

			for (int j = 0; j < 9; j++) {
				graph[i][j] = c[j] - '0';
			}
		}

		sudoku(0, 0);
	}

	static boolean check(int x, int y, int num) {
		for (int i = 0; i < 9; i++) {
			if (graph[x][i] == num) {
				return false;
			}
		}

		for (int i = 0; i < 9; i++) {
			if (graph[i][y] == num) {
				return false;
			}
		}

		int nx = (x / 3) * 3;
		int ny = (y / 3) * 3;

		for (int i = nx; i < nx + 3; i++) {
			for (int j = ny; j < ny + 3; j++) {
				if (graph[i][j] == num) {
					return false;
				}
			}
		}

		return true;
	}

	static void sudoku(int x, int y) {
		if (y == 9) {
			x += 1;
			y = 0;
		}
		if (x == 9) {
			for (int[] row : graph) {
				for (int n : row) {
					System.out.print(n);
				}
				System.out.println();
			}
			System.exit(0);
		}

		if (graph[x][y] != 0) {
			sudoku(x, y + 1);
		} else {
			for (int i = 1; i < 10; i++) {
				if (check(x, y, i)) {
					graph[x][y] = i;
					sudoku(x, y + 1);
					graph[x][y] = 0;
				}
			}
		}
	}
}
