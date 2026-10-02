class Solution {
    public boolean solution(String s) {
        boolean answer = true;
        int count = 0;
        if(s.length() != 4 && s.length() != 6){
            return false;
        }
        for(char c : s.toCharArray()){
            if(!Character.isDigit(c)){return false;}
            
        }
        
        return answer;
    }
}