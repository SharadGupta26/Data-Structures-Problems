package Array;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

/**
 * Given an array of 1 to N, prints all unique sets of the array
 * @author sharadgupta
 *
 */
public class Sets_of_N {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		System.out.println(sets(1, n));
		sc.close();
	}

	private static List<List<Integer>> sets(int start, int end) {
		List<List<Integer>> resultSet = new ArrayList<List<Integer>>();
		if (start > end) {
			resultSet.add(Collections.emptyList());
			return resultSet;
		}
		List<List<Integer>> temp = sets(start + 1, end);
		resultSet.addAll(temp);
		for (List<Integer> list : temp) {
			List<Integer> l = new ArrayList<>(list);
			l.add(start);
			resultSet.add(l);
		}

		return resultSet;
	}
}
