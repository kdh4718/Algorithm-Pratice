import java.util.*;

public class Main {
	static int n, m;
	static char[][] graph;
	static int[] redLoc = new int[2];
	static int[] blueLoc = new int[2];
	static int[] dx = {1, -1, 0, 0};
	static int[] dy = {0, 0, 1, -1};
	static int count = Integer.MAX_VALUE;
	static Set<String> visited = new HashSet<>();
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		sc.nextLine();
		graph = new char[n][m];
		
		for (int i = 0; i < n; i++) {
			graph[i] = sc.nextLine().toCharArray();
		}
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (graph[i][j] == 'R') {
					redLoc[0] = i;
					redLoc[1] = j;
				}
				if (graph[i][j] == 'B') {
					blueLoc[0] = i;
					blueLoc[1] = j;
				}
			}
		}
		
		bfs();
		System.out.println(count <= 10 ? count: -1);
	}
	
	static void bfs() {
		Queue<int[][]> q = new LinkedList<>();
		q.add(new int[][] {redLoc, blueLoc, {0}});
		
		while(!q.isEmpty()) {
			int[][] current = q.poll();
			int[] red = current[0];
			int[] blue = current[1];
			int time = current[2][0];
			
			if (time > 10) {
				continue;
			}
			
			for (int i = 0; i < 4; i++) {
				Location redLoc = move(red[0], red[1], i);
				Location blueLoc = move(blue[0], blue[1], i);
				
				if (redLoc.x == blueLoc.x && redLoc.y == blueLoc.y) {
					if (red[0]*dx[i] + red[1]*dy[i] > blue[0]*dx[i] + blue[1]*dy[i]) {
						blueLoc.x -= dx[i];
						blueLoc.y -= dy[i];
					}else {
						redLoc.x -= dx[i];
						redLoc.y -= dy[i];
					}
				}
				
				if (blueLoc.flag) continue;
				if (redLoc.flag) count = Math.min(count, time+1);
				
				String state = redLoc.x + "," + redLoc.y + "," + blueLoc.x + "," + blueLoc.y;
				if (!visited.contains(state)) {
					visited.add(state);
					q.add(new int[][] {{redLoc.x, redLoc.y}, {blueLoc.x, blueLoc.y}, {time+1}});
				}
			}
		}
	}
	
	static Location move(int x, int y, int d) {
		boolean flag = false;
		
		while(true) {
			x += dx[d];
			y += dy[d];
			
			if (graph[x][y] == '#') {
				x -= dx[d];
				y -= dy[d];
				break;
			}
			
			if (graph[x][y] == 'O') {
				flag = true;
				break;
			}
		}
		
		return new Location(x, y, flag);
	}

	static class Location {
		int x, y;
		boolean flag;
		
		public Location(int x, int y, boolean flag){
			this.x = x;
			this.y = y;
			this.flag = flag;
		}
	}
}
