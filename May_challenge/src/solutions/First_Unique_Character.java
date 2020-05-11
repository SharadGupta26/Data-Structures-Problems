package solutions;

import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;

/**
 * Problem Statment :
 * https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3320/
 * 
 * @author sharadgupta
 *
 */
public class First_Unique_Character {
	public int firstUniqChar(String s) {
		char[] arr = s.toCharArray();
		Map<Character, Integer> map = new LinkedHashMap<>();
		Map<Character, Integer> ind = new HashMap<>();
		int i = 0;
		for (char c : arr) {
			if (map.containsKey(c)) {
				int i1 = map.get(c);
				map.put(c, i1 + 1);
			} else {
				map.put(c, 1);
			}

			if (!ind.containsKey(c)) {
				ind.put(c, i);
			}
			i++;
		}

		for (char c : map.keySet()) {
			if (map.get(c) == 1) {
				return ind.get(c);
			}

		}
		return -1;
	}
	
	public int firstUniqChar_2(String s) {
		char[] arr = s.toCharArray();
		Map<Character, Integer> map = new LinkedHashMap<>();
		for (char c : arr) {
			if (map.containsKey(c)) {
				int i1 = map.get(c);
				map.put(c, i1 + 1);
			} else {
				map.put(c, 1);
			}
		}

		for(int i = 0 ; i<s.length() ; i++) {
			if (map.get(s.charAt(i)) == 1) {
				return i;
			}
		}
		return -1;
	}
}
