import java.util.*;
class Solution {
    int result = 0;
    
    public int solution(int[] number) {
        dfs(number, 0, new ArrayList<>());
        return result;
    }
    public void dfs(int[] number, int start, List<Integer> curr){
        if(curr.size() == 3){
            int sum = 0;
            for(int n : curr){
                sum += n;
            }
            if(sum == 0){
                result++;
            }
            
            return;
        }
        for(int i = start; i < number.length; i++){
            curr.add(number[i]);
            dfs(number, i+1, curr);
            curr.remove(curr.size()-1);
        }

    }
}