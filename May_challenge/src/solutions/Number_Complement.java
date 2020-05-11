package solutions;

/**
 * Problem Statement :
 * https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3319/
 * 
 * @author sharadgupta
 *
 */
public class Number_Complement {
	public int findComplement(int num) {
		int bits = Integer.toBinaryString(num).length();
		int mask = (1 << bits) - 1;
		int res = num ^ mask;
		return res;
	}
}
