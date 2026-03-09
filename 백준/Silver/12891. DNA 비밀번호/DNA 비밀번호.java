import java.io.*;
import java.util.*;

public class Main{
    //전역변수 설정
    static int myArr[];
    static int checkArr[];
    static int checkSecret;
    
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int S = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());
        
        int Result = 0;
        
        checkArr = new int[4];
        myArr = new int[4]; //현재 내 부분문자열의 상태
        char A[] = new char[S];
        checkSecret = 0; // 몇 개의 문자가 개수 조건을 충족했는지 나타내는 변수, 이 변수가 4가 되면 count를 ++해주면 됨
        
        A = br.readLine().toCharArray();
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < 4; i++){
            checkArr[i] = Integer.parseInt(st.nextToken());
            if (checkArr[i] == 0)
                checkSecret++;
        }
        for(int i = 0; i < P; i++){ //부분문자열 처음 받을 때 세팅
            Add(A[i]);
        }
        if(checkSecret == 4) Result++;
        
        //슬라이딩 윈도우(오른쪽으로 한칸 슬라이딩 한 상태에서 시작)
        for(int i = P; i < S; i++){
            int j = i-P;
            Add(A[i]);
            Remove(A[j]);
            if(checkSecret == 4) Result++;
        }
        System.out.println(Result);
        br.close();
    } 
    private static void Add(char c){
        switch(c){
            case 'A':
                myArr[0]++;
                if(myArr[0] == checkArr[0]) checkSecret++;
                break;
            case 'C':
                myArr[1]++;
                if(myArr[1] == checkArr[1]) checkSecret++;
                break;
            case 'G':
                myArr[2]++;
                if(myArr[2] == checkArr[2]) checkSecret++;
                break;
            case 'T':
                myArr[3]++;
                if(myArr[3] == checkArr[3]) checkSecret++;
                break;
        }
    }
    private static void Remove(char c){
        switch(c){
            case 'A':
                if(myArr[0] == checkArr[0]) checkSecret--;
                myArr[0]--;
                break;
            case 'C':
                if(myArr[1] == checkArr[1]) checkSecret--;
                myArr[1]--;
                break;
            case 'G':
                if(myArr[2] == checkArr[2]) checkSecret--;
                myArr[2]--;
                break;
            case 'T':
                if(myArr[3] == checkArr[3]) checkSecret--;
                myArr[3]--;
                break;
        }
    }
}
