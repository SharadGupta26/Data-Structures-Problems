package solutions;

/**
 * Problem Statement :
 * https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3326/
 * 
 * @author sharadgupta
 *
 */
public class Flood_Fill {
	public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
		int m = image.length;
		int n = image[0].length;
		boolean[][] tracking = new boolean[m][n];
		return floodFill(image, sr, sc, newColor, image[sr][sc], tracking);

	}

	public int[][] floodFill(int[][] image, int r, int c, int newColor, int prevColor, boolean[][] tracking) {
		int m = image.length;
		int n = image[0].length;
		if (r < 0 || c < 0 || r >= m || c >= n) {
			return image;
		}

		if (image[r][c] == prevColor && !tracking[r][c]) {
			image[r][c] = newColor;
			tracking[r][c] = true;
		}

		if (r > 0 && image[r - 1][c] == prevColor && !tracking[r - 1][c]) {
			image = floodFill(image, r - 1, c, newColor, prevColor, tracking);
		}

		if (r + 1 < m && image[r + 1][c] == prevColor && !tracking[r + 1][c]) {
			image = floodFill(image, r + 1, c, newColor, prevColor, tracking);
		}

		if (c > 0 && image[r][c - 1] == prevColor && !tracking[r][c - 1]) {
			image = floodFill(image, r, c - 1, newColor, prevColor, tracking);
		}

		if (c + 1 < n && image[r][c + 1] == prevColor && !tracking[r][c + 1]) {
			image = floodFill(image, r, c + 1, newColor, prevColor, tracking);
		}
		return image;

	}
}
