import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args)throws IOException{
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int A[] = new int[N];
        for(int i = 0; i < N; i++){
            A[i] = sc.nextInt();
        }
        Stack<Integer> stack = new Stack<>();
        
        int num = 1;
        boolean result = true;
        StringBuffer bf = new StringBuffer();
        for(int i = 0; i < A.length; i++){
            int su = A[i];
            if(su >= num){
                while(su >= num){
                    stack.push(num++);
                    bf.append("+\n");
                    
                }
                stack.pop(); //똑같아졌을 때는 pop
                bf.append("-\n");
            }
            else{
                int n = stack.pop();
                if(n > su){//현재 수열에 있는 값이 마지막에 있는 스택에 있는 값보다 크다. == 절대 수열은 완성되지 못한다.
                    System.out.println("NO");
                    result = false;
                    break;
                    
                }else{ //두 개의 수가 똑같을 때는
                    bf.append("-\n");
                }
            }
        }
        if(result) System.out.println(bf.toString());
    }
}