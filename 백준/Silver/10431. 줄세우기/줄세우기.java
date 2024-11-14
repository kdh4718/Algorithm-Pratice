import java.io.*;
import java.util.*;

public class Main {
	static int n;
	static int[] line;

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());

		n = Integer.parseInt(st.nextToken());

		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(bf.readLine());
			int num = Integer.parseInt(st.nextToken());

			line = new int[20];
			int count = 0;

			for (int j = 0; j < 20; j++) {
				line[j] = Integer.parseInt(st.nextToken());
			}

			for (int j = 0; j < 20; j++) {
				for (int k = 0; k < j; k++) {
					if (line[k] > line[j])
						count++;
				}
			}

			System.out.println(num + " " + count);
		}
	}
}