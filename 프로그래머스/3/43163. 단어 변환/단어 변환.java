import java.util.*;

class Solution {
    static int answer;
    static boolean[] visited;
    
    static class Node {
        String word;
        int count;
        
        Node(String word, int count){
            this.word = word;
            this.count = count;
        }
    }

    public void bfs(String begin, String target, String[] words){
        Queue<Node> queue = new LinkedList<>();
        queue.offer(new Node(begin, 0));
        
        while(!queue.isEmpty()){
            Node cur = queue.poll();
            
            if (cur.word.equals(target)){
                answer = cur.count;
                break;
            }
            
            for (int i = 0; i < words.length; i++){
                if (!visited[i] && transForm(cur.word, words[i])){
                    visited[i] = true;
                    queue.offer(new Node(words[i], cur.count + 1));
                }
            }
        }
    }
    
    public boolean transForm(String a, String b){
        int count = 0;
        
        for (int i = 0; i < a.length(); i++){
            if (a.charAt(i) != b.charAt(i)){
                count += 1;
            }
        }
        
        return count == 1 ? true : false;
    }
    
    public int solution(String begin, String target, String[] words) {
        answer = 0;
        visited = new boolean[words.length];
        
        bfs(begin, target, words);
        
        return answer;
    }
}