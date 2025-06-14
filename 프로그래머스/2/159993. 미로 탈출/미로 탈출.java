import java.util.*;

class Solution {
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};

    static class Node {
        int x, y, dist;

        Node(int x, int y, int dist) {
            this.x = x;
            this.y = y;
            this.dist = dist;
        }
    }

    static int bfs(String[] maps, int startX, int startY, char target) {
        int n = maps.length;
        int m = maps[0].length();
        boolean[][] visited = new boolean[n][m];
        Queue<Node> queue = new LinkedList<>();
        queue.offer(new Node(startX, startY, 0));
        visited[startX][startY] = true;

        while (!queue.isEmpty()) {
            Node cur = queue.poll();

            if (maps[cur.x].charAt(cur.y) == target) {
                return cur.dist;
            }

            for (int i = 0; i < 4; i++) {
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];

                if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
                if (visited[nx][ny] || maps[nx].charAt(ny) == 'X') continue;

                visited[nx][ny] = true;
                queue.offer(new Node(nx, ny, cur.dist + 1));
            }
        }

        return -1;  
    }

    public int solution(String[] maps) {
        int n = maps.length;
        int m = maps[0].length();
        int startX = 0, startY = 0;
        int leverX = 0, leverY = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                char ch = maps[i].charAt(j);
                if (ch == 'S') {
                    startX = i;
                    startY = j;
                } else if (ch == 'L') {
                    leverX = i;
                    leverY = j;
                }
            }
        }

        int toLever = bfs(maps, startX, startY, 'L');
        if (toLever == -1) return -1;

        int toExit = bfs(maps, leverX, leverY, 'E');
        if (toExit == -1) return -1;

        return toLever + toExit;
    }
}