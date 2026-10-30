class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        String[] words = {"aya", "ye", "woo", "ma"};
        
        
        for(String str : babbling){
            //1. bool값 리스트 생성, 서로 다른 문자열에서는 같은 문자열을 사용할 수 있으므로 for문 안에 배치
            boolean[] words_bool = new boolean[4];
            while(!str.isEmpty()){
                boolean found = false;
                for(int i =0; i < words.length; i++){
                    if(words_bool[i] == false && str.startsWith(words[i])){
                        
                        words_bool[i] = true;
                        str = str.substring(words[i].length());
                        found = true;
                        break;
                    }
                    
                }
                if(found==false){
                    break;
                }
            }
            if (str.isEmpty()){
                answer++;
            }
        }
        return answer;
    }
}