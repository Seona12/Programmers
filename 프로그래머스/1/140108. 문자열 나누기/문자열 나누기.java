class Solution {
    public int solution(String s) {
        int answer = 0;
        char[] array = s.toCharArray();
        char x = array[0];
        int x_num = 0;
        int other_num = 0;
        for(int i = 0; i < s.length(); i++){
            
            if(x_num == 0 && other_num==0){
                x = array[i];
            }
            if(x == array[i]){
                x_num++;
            }
            else{
                other_num++;
            }
            
            if(x_num==other_num){
                answer++;
                x_num = 0;
                other_num = 0; 
                
            }
            
            
            
            
        }
        if (x_num > 0 || other_num > 0){
                answer++;
            }
        return answer;
    }
}