import java.util.*;
import java.io.*;

public class Main {
	static int n, m, countW, countB, count;
	static char[][] graph;

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());

		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());

		count = Integer.MAX_VALUE;
		graph = new char[n][m];

		for (int i = 0; i < n; i++) {
			graph[i] = bf.readLine().toCharArray();
		}

		for (int i = 0; i < n - 7; i++) {
			for (int j = 0; j < m - 7; j++) {
				count = Math.min(count, check(i, j));
			}
		}
		
		System.out.println(count);
	}
	
	static int check(int x, int y) {
		countW = 0;
		countB = 0;
		
		for (int i = 0; i < 8; i++) {
			for (int j = 0; j < 8; j++) {
				if ((i + j) % 2 == 0) {
					if (graph[x + i][y + j] == 'W') countB++;
					else countW++;
				}else {
					if (graph[x + i][y + j] == 'W') countW++;
					else countB++;
				}
			}
		}

		return Math.min(countW, countB);
	}

}
