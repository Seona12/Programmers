import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visited = new boolean[n];
        for(int i = 0; i < n; i++){
            if(!visited[i]){
                bfs(i,computers,visited);
                answer++;
            }
        }
        return answer;
    }
    void bfs(int start, int[][] computers, boolean[] visited){
        Queue<Integer> queue = new ArrayDeque<>();
        queue.offer(start);
        visited[start] = true;
        
        while(!queue.isEmpty()){
            int cur = queue.poll();
            
            for(int nxt = 0; nxt < computers.length; nxt++){
                if(computers[cur][nxt] == 1 && !visited[nxt]){
                    queue.offer(nxt);
                    visited[nxt] = true;
                }
            }
        }
    }
}