import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());
        int[] A = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i++){
            A[i] = Integer.parseInt(st.nextToken());
        }
       Arrays.sort(A);
       int count = 0;
       int i = 0; //A[0] -> MIN
       int j = N-1; //A[N-1] -> MAX
        
       while(i < j){ //두 개의 포인터가 겹쳐지는 순간 반복문 종료
           if(A[i] + A[j] < M) i++;
           else if(A[i] + A[j] > M)j--;
           else{
               count++;
               i++; j--;
           }
       }
        System.out.println(count);
    }
}