import java.util.*;
class Solution {
    public String solution(String s) {
        char[] s_chararray = s.toCharArray();
        Arrays.sort(s_chararray);
        String answer = new StringBuilder(new String(s_chararray)).reverse().toString();
        return answer;
    }
}