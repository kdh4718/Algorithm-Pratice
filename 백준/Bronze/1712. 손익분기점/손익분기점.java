import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// 1712
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt(); int b = sc.nextInt(); int c = sc.nextInt();
		int point = 0;
		
		if(b >= c) {
			System.out.println(-1);
		}else {
			point = (a/(c-b))+1;
			System.out.println(point);
		}
		
		sc.close();
	}

}