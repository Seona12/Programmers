class Solution {
    public String solution(String s) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        boolean isOdd = true;
        
        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            
            if(c == ' '){
                sb.append(" ");
                isOdd = true;
                
            }
            else if(isOdd){
                sb.append(Character.toUpperCase(c));
                isOdd = false;
            }
            else{
                sb.append(Character.toLowerCase(c));
                isOdd = true;
            }
        }
        return sb.toString();
    }
}