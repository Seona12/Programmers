import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args)throws IOException{
        BufferedReader buffredReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(buffredReader.readLine());
        int N = Integer.parseInt(stringTokenizer.nextToken());

        stringTokenizer = new StringTokenizer(buffredReader.readLine());
        int M = Integer.parseInt(stringTokenizer.nextToken());

        stringTokenizer = new StringTokenizer(buffredReader.readLine());
        int A[] = new int[N];
        for(int i = 0; i < N; i++){

            A[i] = Integer.parseInt(stringTokenizer.nextToken());
        }
        Arrays.sort(A); //배열 오름차순 정렬

        int start_index = 0;
        int end_index = N-1;
        int count = 0;

        while(start_index < end_index){
            int sum = A[start_index] + A[end_index];
            if(sum == M){
                count++;
                start_index++;
                end_index--;

            }
            else if(sum < M){
                start_index++;
            }else{
                end_index--;
            }
        }
        System.out.println(count);

    }
}