import java.util.*;

class Solution {
    // treeset은 중복 허용
    Set<Integer> ans = new TreeSet<>();
    
    public int[] solution(int[] numbers) {
        //자기 자신은 더하면 안되므로 visited 배열 선언
        boolean[] visited = new boolean[numbers.length];
        //dfs 선언
        dfs(numbers, 0, visited, 0);
        //stream으로 출력형식 맞추기
        return ans.stream().mapToInt(Integer::intValue).toArray();
        
    }
    public void dfs(int[] numbers, int current, boolean[] visited, int depth){
        if(depth == 2){
            ans.add(current);
            return; //dfs 종료
        }
        for(int i = 0; i < numbers.length; i++){
            if(!visited[i]){
                visited[i] = true;
                int next = current + numbers[i];
                dfs(numbers, next, visited, depth + 1);
                visited[i] = false;
            }
            
        }
        
    }
}