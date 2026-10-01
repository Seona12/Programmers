import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        ArrayList<Integer> stk_arr = new ArrayList<>();
        int i = 0;
        while(i < arr.length){
            if(stk_arr.size() == 0){
                stk_arr.add(arr[i]);
                i++;
            } else if(stk_arr.get(stk_arr.size() - 1) < arr[i]){
                stk_arr.add(arr[i]);
                i++;
                
            } else if(stk_arr.get(stk_arr.size() - 1)>= arr[i]){
                stk_arr.remove(stk_arr.size() - 1);
            }
        }
            
        int[] stk = new int[stk_arr.size()];
        
        for(int j = 0; j < stk_arr.size(); j++){
            stk[j] = stk_arr.get(j);
        }
        return stk;
    
    }
}