import java.util.*;
import java.io.*;

public class Main {
	static int n;
	static int[] t, p, dp;

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());

		n = Integer.parseInt(st.nextToken());
		t = new int[n + 1];
		p = new int[n + 1];
		dp = new int[n + 1];

		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(bf.readLine());
			t[i] = Integer.parseInt(st.nextToken());
			p[i] = Integer.parseInt(st.nextToken());
		}

		for (int i = t.length - 2; i > -1; i--) {
			if (t[i] + i <= n) {
				dp[i] = Math.max(p[i] + dp[i + t[i]], dp[i + 1]);
			} else {
				dp[i] = dp[i + 1];
			}
		}
		
		System.out.print(dp[0]);
	}
}