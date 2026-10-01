import java.util.*;

class Solution {
    public int[] solution(int l, int r) {
        ArrayList<Integer> arr = new ArrayList<>();
        
        for(int i = l; i <= r; i++){
            String s = String.valueOf(i);
            boolean check = true;
            for(int j = 0; j < s.length(); j++){
                if (s.charAt(j) != '5' && s.charAt(j) != '0'){
                    check = false;
                    break;
                }
            }
            if (check){
                arr.add(i);
            }
        }
        int[] answer = new int[arr.size()];
        if (arr.size() == 0){return new int[]{-1};}
        for(int i = 0; i < arr.size(); i++){
           answer[i] = arr.get(i); 
        }
        return answer;
    }
}