package solutions;

/**
 * Problem Statement :
 * https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3325/
 * 
 * @author sharadgupta
 *
 */
public class Find_The_Town_Judge {
	public int findJudge(int N, int[][] trust) {
		boolean[] arr = new boolean[N + 1];
		for (int[] t : trust) {
			arr[t[0]] = true;
		}

		int judge = -1;
		for (int i = 1; i < arr.length; i++) {
			if (!arr[i]) {
				if (judge != -1) {
					return -1;
				}
				judge = i;
			}
		}
		if (judge == -1) {
			return -1;
		}
		arr = new boolean[N + 1];
		for (int[] t : trust) {
			if (t[1] == judge) {
				arr[t[0]] = true;
			}
		}

		for (int i = 1; i < arr.length; i++) {
			if (i == judge) {
				continue;
			}

			if (!arr[i]) {
				judge = -1;
			}

		}

		return judge;
	}
}
