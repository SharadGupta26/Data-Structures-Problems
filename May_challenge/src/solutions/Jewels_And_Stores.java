package solutions;

/**
 * Problem Statement :
 * https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3317/
 * 
 * @author sharadgupta
 *
 */
public class Jewels_And_Stores {
	public int numJewelsInStones(String J, String S) {
		char[] s_arr = S.toCharArray();
		int[] s_count = new int[256];
		for (char c : s_arr) {
			s_count[(int) c]++;
		}

		char[] j_arr = J.toCharArray();
		int count = 0;
		for (char c : j_arr) {
			count += s_count[(int) c];
		}
		return count;
	}
}
