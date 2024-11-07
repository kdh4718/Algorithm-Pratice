import java.util.*;
import java.io.*;

public class Main {
	static int n, k, l;
	static int[][] graph;
	static List<int[]> turns;
	static int[][] directions = { {0, 1}, {1, 0}, {0, -1}, {-1, 0} };
	static String direction;
	static String[] turn;

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(bf.readLine());
		k = Integer.parseInt(bf.readLine());
		
		graph = new int[n][n];
		turns = new ArrayList<>();
		
		for (int i = 0; i < k; i++) {
		    String[] position = bf.readLine().split(" ");
		    int x = Integer.parseInt(position[0]) - 1;
		    int y = Integer.parseInt(position[1]) - 1;
		    graph[x][y] = 1;
		}
		
		l = Integer.parseInt(bf.readLine());
		
		for (int i = 0; i < l; i++) {
			turn = bf.readLine().split(" ");
			int time = Integer.parseInt(turn[0]);
			direction = turn[1];
			
			turns.add(new int[] {time, direction.equals("D") ? 1: -1});
		}
		System.out.println(bfs());
	}

	static int bfs() {
		Deque<int[]> q = new ArrayDeque<>();
		q.add(new int[] {0, 0});
		graph[0][0] = 2;
		
		int time = 0;
		int cur = 0;
		int turn = 0;
		
		while (true) {
			time++;
            int[] head = q.peekFirst();
            int nx = head[0] + directions[cur][0];
            int ny = head[1] + directions[cur][1];
            
            if (nx < 0 || nx >= n || ny < 0 || ny >= n || graph[nx][ny] == 2) {
                break;
            }
            
            if (graph[nx][ny] == 1) { 
                q.addFirst(new int[] {nx, ny});
                graph[nx][ny] = 2; 
            } else { 
                q.addFirst(new int[] {nx, ny});
                graph[nx][ny] = 2;
                int[] tail = q.removeLast();
                graph[tail[0]][tail[1]] = 0; 
            }
            
            if (turn < turns.size() && turns.get(turn)[0] == time) {
            	cur = (cur + turns.get(turn)[1] + 4) % 4;
            	turn++;
            }
		}
		
		
		return time;
	}
}
