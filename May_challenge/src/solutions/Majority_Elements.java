package solutions;

import java.util.HashMap;
import java.util.Map;

/**
 * Problem Statement :
 * https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3321/
 * 
 * @author sharadgupta
 *
 */
public class Majority_Elements {

	public int majorityElement(int[] nums) {
		Map<Integer, Integer> map = new HashMap<>();
		for (int i : nums) {
			map.put(i, map.getOrDefault(i, 0) + 1);
		}
		for (int i : map.keySet()) {
			if (map.get(i) > nums.length / 2) {
				return i;
			}
		}
		return -1;
	}
}
