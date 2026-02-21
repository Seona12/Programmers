import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args)throws IOException{
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());

        int N = Integer.parseInt(stringTokenizer.nextToken());

        int count = 1;
        int start_index = 1;
        int end_index = 1;
        int sum = 1;

        while(end_index!=N){
            if (sum == N){
                count += 1;
                end_index +=1;
                sum += end_index;
            }
            else if(sum > N){
                sum -= start_index;
                start_index += 1;

            }
            else if(sum < N){
                end_index += 1;
                sum += end_index;
            }
        }
        System.out.println(count);
    }
}