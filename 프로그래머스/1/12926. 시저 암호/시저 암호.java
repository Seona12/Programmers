class Solution {
    public String solution(String s, int n) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        
        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if(c == ' '){
                sb.append(" ");
            }
            else{
                char cn = (char)(s.charAt(i) + n);
                if (c >= 'A' && c <= 'Z') {
                // 대문자인 경우
                    if (cn > 'Z'){
                        sb.append((char)(cn-26));
                    } else{
                        sb.append((char)(cn));
                    }
                    
                } else if (c >= 'a' && c <= 'z') {
                    if(cn > 'z'){
                        sb.append((char)(cn-26));
                    } else{
                        sb.append((char)(cn));
                    }
                    
                }
                

            }
            
            
        }
        
        return sb.toString();
        
    }
}