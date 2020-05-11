package solutions;

/**
 * Problem Statement :
 * https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3324/
 * 
 * @author sharadgupta
 *
 */
public class Valid_Perfect_Square {

	public boolean isPerfectSquare(int num) {
		if (num == 1 || num == 0) {
			return true;
		}
		long t = num / 2;

		while (t * t > num) {
			t = (t + (num / t)) / 2;
		}
		if (t * t == num) {
			return true;
		}
		return false;
	}
}
