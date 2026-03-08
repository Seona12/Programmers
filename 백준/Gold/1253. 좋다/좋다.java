import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int A[] = new int[N];
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i++){
            A[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(A);
        
        int count = 0;
        for(int k = 0; k < N; k++){
            long find = A[k];
            int i = 0; //A 배열의 시작
            int j = N-1; // 배열의 끝
            
            while(i < j){
                if(A[i]+ A[j] == find){
                    if(i!=k && j !=k){
                        count++;
                        break;
                    }
                    else if(i==k){
                        i++;
                    }
                    else if(j==k){
                        j--;
                    }
                }
                else{
                    if(A[i] + A[j] < find)
                    {
                        i++;
                    }
                    else{
                        j--;
                    }
                }
            }
        }
        System.out.println(count);
  
    }
}