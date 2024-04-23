import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int a, b, c, reward;
		
		Scanner dice = new Scanner(System.in);
		a = dice.nextInt();
		b = dice.nextInt();
		c = dice.nextInt();
		
		if(a == b && b == c) {
			reward = 10000 + (a*1000);
		}else if(a == b || b == c) {
			reward = 1000 + (b*100);
		}else if(a == c) {
			reward = 1000 + (a*100);
		}else {
			reward = Math.max(a, Math.max(b, c))*100;
		}
			
		System.out.println(reward);
	}

}
