package String;

import java.util.Scanner;

public class Longest_Palindrom_Sequence {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s = sc.nextLine();
		System.out.println("Longes palindrome : " + longest_palindrome(s));
		sc.close();
	}

	private static void print(int[][] arr) {
		for (int[] i : arr) {
			for (int j : i) {
				System.out.print(j + " ");
			}
			System.out.println();
			
		}
	}

	private static int longest_palindrome(String s) {
		int[][] arr = new int[s.length()][s.length()];
		for (int i = 0; i < s.length(); i++) {
			arr[i][i] = 1;
		}
		int res = longest_palindrome(s, 0, s.length() - 1, arr, 0);
		//print(arr);
		return res;
	}

	private static int longest_palindrome(String s, int i, int j, int[][] mem, int res) {

		if (i > j)
			return res; // invalid input
		if (mem[i][j] != 0) {
			//System.out.println(mem[i][j] + res+" ---- "+i + " -- " + j);
			return mem[i][j] + res;
		}

		if (s.charAt(i) == s.charAt(j)) {
			res = longest_palindrome(s, i + 1, j - 1, mem, 2 + res);
		} else {
			res = Integer.max(longest_palindrome(s, i, j - 1, mem, 0), longest_palindrome(s, i + 1, j, mem, 0));
		}
		mem[i][j] = res;
		return res;
	}
}
