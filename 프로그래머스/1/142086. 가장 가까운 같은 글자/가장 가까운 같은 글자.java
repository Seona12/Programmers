class Solution {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];
        for(int i = 0; i < s.length(); i++){
            int count = 0;
            for(int j = i-1; j >= 0 ; j--){ //현재 문자 바로 앞에 있는 문자부터 검사해야하므로 i-1부터 검사, 거꾸로
                if(s.charAt(i) == s.charAt(j)){
                    answer[i] = i-j;
                    count++;
                    break;
                }
                
            }
            if(count==0){
                answer[i] = -1;
            }
            
        }
        return answer;
    }
}