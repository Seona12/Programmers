import java.util.*;

class Solution {
    public String[] solution(String[] strings, int n) {
        String[] answer = {};
        // 정렬 기준 세우기(람다식 활용)
        Arrays.sort(strings, (a,b) -> {
                if (a.charAt(n) == b.charAt(n)){
                    return a.compareTo(b);
                } else{
                    return Character.compare(a.charAt(n), b.charAt(n));
                }
                
            
        });
        
        return strings;
    }
}