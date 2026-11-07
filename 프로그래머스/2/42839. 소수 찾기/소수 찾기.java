import java.util.*;
class Solution {
    //리스트 초기화
    Set<Integer> ans = new HashSet<>();
    public int solution(String numbers) {
        char[] numbers_charArray = numbers.toCharArray();
        boolean[] visited = new boolean[numbers_charArray.length];
        // dfs 선언자리
        dfs(numbers_charArray, 0, visited);
        int answer = ans.size();
        return answer;
    }
    public void dfs(char[] numbers_charArray, int current, boolean[] visited){
            for(int i = 0; i < numbers_charArray.length; i++){
                if(!visited[i]){
                    int num = current * 10 + (numbers_charArray[i]-'0');
                    visited[i] = true;
                    if(isPrime(num)){
                        ans.add(num);
                    }
                    dfs(numbers_charArray, num, visited);
                    visited[i] = false;
                }
                
                
            }
        
        
    }
    public boolean isPrime(int num){
        if(num < 2){
            return false;
        }
        for(int i = 2; i < num; i++){
            if(num % i == 0){
                return false;
            }
        } // for문이 끝났다는 것 : 소수가 하나도 발견되지 않았다는 뜻이므로 true 리턴
        return true;
    }
}