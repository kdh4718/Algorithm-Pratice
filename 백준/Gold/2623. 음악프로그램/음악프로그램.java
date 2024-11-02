import java.util.*;
import java.io.*;

class Main {
    static int n, m, num;
    static ArrayList<Integer>[] child;
    static int[] degree, order;
    static Queue<Integer> q;
    static ArrayList<Integer> answer;
    
    public static void main(String[] args) throws IOException  {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        child = new ArrayList[n+1];
        q = new ArrayDeque<>();
        answer = new ArrayList<>();
        degree = new int[n+1];

        for (int i = 1; i < n+1; i++){
            child[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++){
            st = new StringTokenizer(bf.readLine());
            num = Integer.parseInt(st.nextToken());
            order = new int[num];

            for (int j = 0; j < num; j++){
                order[j] = Integer.parseInt(st.nextToken());
            }

            for (int j = 0; j < num-1; j++){
                child[order[j]].add(order[j+1]);
                degree[order[j+1]]++;
            }
        }

        for (int i = 1; i <= n; i++) {
            if (degree[i] == 0) {
                q.add(i);
            }
        }

        while (!q.isEmpty()) {
            int x = q.poll();
            answer.add(x);

            for (int num : child[x]) {
                degree[num]--;
                if (degree[num] == 0) {
                    q.add(num);
                }
            }
        }

        if (answer.size() < n) {
            System.out.println(0);
        } else {
            for (int a : answer) {
                System.out.println(a);
            }
        }
    }
}