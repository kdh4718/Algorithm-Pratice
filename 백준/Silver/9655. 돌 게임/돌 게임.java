import java.util.*;
import java.io.*;

public class Main {
	static int n;
	
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());
		
		n = Integer.parseInt(st.nextToken());
		
		if (n % 2 == 0) {
			System.out.println("CY");
		}else {
			System.out.println("SK");
		}
	}
}