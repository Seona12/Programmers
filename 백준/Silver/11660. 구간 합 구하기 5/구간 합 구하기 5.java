import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args)throws IOException{
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        
        //배열 크기, 질의 수 저장하기
        int N = Integer.parseInt(stringTokenizer.nextToken());
        int M = Integer.parseInt(stringTokenizer.nextToken());
        
        //원본 배열 저장
        int A[][] = new int[N+1][N+1];
        for(int i = 1; i <= N; i++){
            stringTokenizer = new StringTokenizer(bufferedReader.readLine());
            for(int j = 1; j <= N; j++){
                A[i][j] = Integer.parseInt(stringTokenizer.nextToken());
            }
        }
        
        //합 배열 저장
        int D[][] = new int[N+1][N+1];
         for(int i = 1; i <= N; i++){
            for(int j = 1; j <= N; j++){
                D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j];
            }
        }
        
        //질의 계산 및 출력
        for(int q = 0; q < M; q++){
            stringTokenizer = new StringTokenizer(bufferedReader.readLine());
            int x1 = Integer.parseInt(stringTokenizer.nextToken());
            int y1 = Integer.parseInt(stringTokenizer.nextToken());
            int x2 = Integer.parseInt(stringTokenizer.nextToken());
            int y2 = Integer.parseInt(stringTokenizer.nextToken());
            
            int result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1];
            
            System.out.println(result);
        }
        
        
        
    }
}