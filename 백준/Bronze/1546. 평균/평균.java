import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] A = new int[N];
        //원소 넣기
        for(int i = 0; i < N; i++){
            A[i] = sc.nextInt();
        }
        //최댓값, 합 구하기
        long max = 0;
        long sum = 0;
        
        for(int i = 0; i < A.length; i++){
            if (A[i] >= max){
                max = A[i];
            }
            sum += A[i];
        }
        
        System.out.println(sum*100.0/max/N);
        
    }
}