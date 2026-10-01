import java.util.*;
class Solution {
    public int[] solution(int[] arr) {
        int[] answer = {};
        ArrayList<Integer> arrayList = new ArrayList<>();
        int i = 0;
        while(i < arr.length){
            if(arrayList.isEmpty()){
                arrayList.add(arr[i]);
                i++;
            }
            else if(arrayList.get(arrayList.size()-1) == arr[i]){
                arrayList.remove(arrayList.size()-1);
                i++;
            }
            else if(arrayList.get(arrayList.size()-1) != arr[i]){
                arrayList.add(arr[i]);
                i++;
            }
        }
        if(arrayList.isEmpty()){
            return new int[]{-1};
        }
        int[] stk = new int[arrayList.size()];
        for(int j = 0; j < arrayList.size(); j++)
        {
            stk[j] = arrayList.get(j);
        }
        return stk;
    }
    
}