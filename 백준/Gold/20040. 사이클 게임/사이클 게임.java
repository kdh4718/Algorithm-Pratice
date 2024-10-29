import java.util.*;

public class Main {
	static int n, m;
	static int[] parent;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();

		parent = new int[n];
		for (int i = 0; i < n; i++) {
			parent[i] = i;
		}

		for (int i = 0; i < m; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();

			if (find(a) != find(b)) {
				union(a, b);
			} else {
				System.out.println(i + 1);
				return;
			}
		}

		System.out.println(0);
	}

	static int find(int x) {
		if (x == parent[x]) {
			return x;
		}

		return parent[x] = find(parent[x]);
	}

	static void union(int a, int b) {
		int rootA = find(a);
		int rootB = find(b);
		
		if (rootA > rootB) {
			parent[rootA] = rootB;
		}else {
			parent[rootB] = rootA;
		}
	}
}
