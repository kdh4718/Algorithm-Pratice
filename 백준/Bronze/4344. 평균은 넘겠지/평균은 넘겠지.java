import java.util.Scanner;
import java.util.Arrays;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int case_num, num, count;
		double aver;
		
		case_num = sc.nextInt();
		for(int i = 0 ; i < case_num ; i++) {
			
			num = sc.nextInt();
			int[] score = new int[num];
			for(int j = 0; j < num ; j++) {
				score[j] = sc.nextInt();				
			}
			
			aver = ((double)Arrays.stream(score).sum()/score.length);
			double a = 0;
			for(int j = 0; j < num ; j++) {
				if(score[j]> aver) {
					a++;
				}				
			}
			a = ((double)a/score.length)*100;
			System.out.println(String.format("%.3f", a)+"%");
		}		
		sc.close();
	}
}