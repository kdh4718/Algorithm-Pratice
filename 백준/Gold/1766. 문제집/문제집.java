import java.util.*;

public class Main {
	static int n, m;
	static int[] degree;
	static ArrayList<ArrayList<Integer>> graph;
	static StringBuilder answer;
	static PriorityQueue<Integer> pq;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();

		graph = new ArrayList<>();
		for (int i = 0; i < n+1; i++) {
			graph.add(new ArrayList<>());
		}
		
		degree = new int[n + 1];
		pq = new PriorityQueue<>();
		answer = new StringBuilder();
		
		for (int i = 0; i < m; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			
			graph.get(a).add(b);
			degree[b] += 1;
		}
		
		for (int i = 1; i < n+1; i++) {
			if (degree[i] == 0) {
				pq.add(i);
			}
		}
		
		while(!pq.isEmpty()) {
			int now = pq.poll();
			answer.append(now).append(" ");
			
			for (int next : graph.get(now)) {
				degree[next] -= 1;
				if (degree[next] == 0) {
					pq.add(next);
				}
			}
		}
		
		System.out.println(answer.toString());
	}
}