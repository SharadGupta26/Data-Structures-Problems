package String;

import java.util.Scanner;
import java.util.regex.Pattern;

public class IP_Regax {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s = sc.nextLine();
		String pattern = "(([0-9]{1,2}|[0,1][0-9]{1,2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]{1,2}|[0,1][0-9]{1,2}|2[0-4][0-9]|25[0-5])";

		System.out.println(Pattern.matches(pattern, s));
		sc.close();
	}
}
