import java.util.*;

class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        ArrayList<Integer> arrayList = new ArrayList<>();
        for(String str : intStrs){
            int a = Integer.parseInt(str.substring(s,s+l));
            if (a > k){
                arrayList.add(a);
            }
            
        }
        int[] answer = new int[arrayList.size()];
        for(int i = 0; i < arrayList.size(); i++){
            answer[i] = arrayList.get(i);
        }

        return answer;
    }
}