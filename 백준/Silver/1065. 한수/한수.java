import java.util.Scanner;
import java.util.Arrays;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		int count = 0;
		
		if(num < 100) {
			count = num;
		}else {
			count = 99;
			for(int i = 100; i <= num; i++) {
				String[] num_str = Integer.toString(i).split(""); 
				if((Integer.parseInt(num_str[0])-Integer.parseInt(num_str[1]))==
						(Integer.parseInt(num_str[1])-Integer.parseInt(num_str[2]))) {
					count++;
				}
			}
		}
		
		System.out.println(count);

		sc.close();
	}

}