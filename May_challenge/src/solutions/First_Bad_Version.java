package solutions;

/**
 * Problem statement :
 * https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3316/
 * 
 * @author sharadgupta
 *
 */
public class First_Bad_Version extends VersionControl {
	public int firstBadVersion(int n) {
		return findBadVersion(1, n);
	}

	public int findBadVersion(int min, int max) {

		if (min == max) {
			return min;
		}
		if (max - min == 1) {
			if (isBadVersion(min)) {
				return min;
			}
			return max;
		}

		int mid = min + (max - min) / 2;
		if (isBadVersion(mid)) {
			max = mid;
		} else {
			min = mid + 1;
		}
		return findBadVersion(min, max);
	}

}

class VersionControl {
	int n = 0;

	public boolean isBadVersion(int a) {
		return a == n;
	}
}
