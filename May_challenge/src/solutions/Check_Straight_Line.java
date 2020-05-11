package solutions;

/**
 * Problem Statement :
 * https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3323/
 * 
 * @author sharadgupta
 *
 */
public class Check_Straight_Line {

	public boolean checkStraightLine(int[][] coordinates) {
		if (coordinates.length == 1) {
			return true;
		}

		if (coordinates[1][0] == coordinates[0][0]) {
			int constX = coordinates[1][0];
			for (int i = 2; i < coordinates.length; i++) {
				if (coordinates[i][0] != constX) {
					return false;
				}
			}
		} else {
			int m = ((coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0]));
			int c = (coordinates[0][1]) - (m * coordinates[0][0]);
			for (int i = 2; i < coordinates.length; i++) {
				if (coordinates[i][1] != ((m * coordinates[i][0]) + c)) {
					return false;
				}
			}
		}

		return true;

	}

	/**
	 * If three points are in line, they will have same slope
	 * 
	 * @param coordinates
	 * @return
	 */
	public boolean checkStraightLine_2(int[][] coordinates) {
		if (coordinates.length == 1) {
			return true;
		}

		int x1 = coordinates[0][0];
		int y1 = coordinates[0][1];
		int x2 = coordinates[1][0];
		int y2 = coordinates[1][1];

		for (int i = 2; i < coordinates.length; i++) {
			int x3 = coordinates[i][0];
			int y3 = coordinates[i][1];
			if ((y2 - y1) * (x3 - x2) != (y3 - y2) * (x2 - x1)) {
				return false;
			}
		}

		return true;

	}

}
