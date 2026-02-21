import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        // 10만개의 긴 입력은 int로 입력받기 힘드므로 StringTokenizer 사용
        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        //StringTokenizer는 String으로 입력받기 때문에 int형으로 변경 필요
        int suNo = Integer.parseInt(stringTokenizer.nextToken());
        int quizNo = Integer.parseInt(stringTokenizer.nextToken());
        
        //합배열 만들기
        //숫자형 데이터 다룰 때는 계산 오류를 막기 위해 long형이 좋음.
        long[] S = new long[suNo +1]; //0번째 인덱스를 무시하기 위해
        stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        for(int i = 1; i <= suNo ; i++){
            S[i] = S[i-1] + Integer.parseInt(stringTokenizer.nextToken());
        }
        
        //i,j 입력 받아 구간합 구하기
        for(int q = 0; q < quizNo; q++){
            stringTokenizer = new StringTokenizer(bufferedReader.readLine());
            int i = Integer.parseInt(stringTokenizer.nextToken());
            int j = Integer.parseInt(stringTokenizer.nextToken());
            
            System.out.println(S[j]-S[i-1]);
        }
    }
}