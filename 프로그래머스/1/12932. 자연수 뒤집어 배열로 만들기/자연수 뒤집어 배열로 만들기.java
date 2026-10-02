class Solution {
    public int[] solution(long n) {
        String str = String.valueOf(n);
        char[] answer_new = new char[str.length()];
        
        for(int i = 0; i < str.length(); i++){
            char c = str.charAt(i);
            answer_new[i] = c;
        }
        
        int idx = 0;
        int[] answer = new int[answer_new.length];
        for(int j = answer_new.length - 1 ; j >= 0; j--){
            answer[idx] = answer_new[j] - '0';
            idx++;
        }
        return answer;
    }
}