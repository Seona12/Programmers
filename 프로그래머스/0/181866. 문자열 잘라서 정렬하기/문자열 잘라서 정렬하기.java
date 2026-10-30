import java.util.*;

class Solution {
    public String[] solution(String myString) {
        String[] arr = myString.split("x");
        ArrayList<String> arrlist = new ArrayList<>();
        for(String s : arr){
            if(!s.isEmpty()){
                arrlist.add(s);}
            
        }
        Collections.sort(arrlist);
        return arrlist.toArray(new String[0]);
    }
}