package solutions;

/**
 * Problem Statement :
 * https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3318/
 * 
 * @author sharadgupta
 *
 */
public class Ransom_Note {

	public boolean canConstruct(String ransomNote, String magazine) {
		char[] r_arr = ransomNote.toCharArray();
		char[] m_arr = magazine.toCharArray();
		int[] r_count = new int[256];
		int[] m_count = new int[256];

		for (char c : m_arr) {
			m_count[(int) c]++;
		}

		for (char c : r_arr) {
			r_count[(int) c]++;
		}

		for (char c : r_arr) {
			if (r_count[(int) c] > m_count[(int) c]) {
				return false;
			}
		}
		return true;

	}
}
