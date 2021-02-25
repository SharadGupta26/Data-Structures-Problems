package String;

import java.util.ArrayList;
import java.util.List;

/**
 * https://leetcode.com/problems/zigzag-conversion/
 * 
 * @author sharadgupta
 *
 */
class ZigZag_Conversion {
	public String convert(String s, int n) {
		if (n == 1) {
			return s;
		}
		int len = s.length();
		char[][] arr = new char[n][len];
		int i = 0;
		int j = 0;
		// System.out.println(i +" " + n);
		boolean upward = false;
		for (char c : s.toCharArray()) {
			// System.out.println(row +" " + col);
			arr[i][j] = c;
			if (i == n - 1) {
				upward = true;

			} else if (i == 0) {
				upward = false;
			}
			if (upward) {
				i--;
				j++;
			} else {
				i++;
			}

		}

		String s1 = "";
		for (int k = 0; k < n; k++) {
			for (int l = 0; l < len; l++) {
				if (arr[k][l] == '\u0000') {
					continue;
				}
				s1 = s1 + arr[k][l] + "";
			}
		}
		return s1;
	}

	public String solution_2(String s, int numRows) {

		if (numRows == 1)
			return s;

		List<StringBuilder> rows = new ArrayList<>();
		for (int i = 0; i < Math.min(numRows, s.length()); i++)
			rows.add(new StringBuilder());

		int curRow = 0;
		boolean goingDown = false;

		for (char c : s.toCharArray()) {
			rows.get(curRow).append(c);
			if (curRow == 0 || curRow == numRows - 1)
				goingDown = !goingDown;
			curRow += goingDown ? 1 : -1;
		}

		StringBuilder ret = new StringBuilder();
		for (StringBuilder row : rows)
			ret.append(row);
		return ret.toString();
	}
}