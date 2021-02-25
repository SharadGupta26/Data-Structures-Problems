package Array;

import java.util.Scanner;
import java.util.stream.Stream;

public class SearchingAlgos {

	public static void main(String[] ar) {
		Scanner sc = new Scanner(System.in);
		int x = sc.nextInt();
		sc.nextLine();
		int[] arr = Stream.of(sc.nextLine().split("\\s+")).mapToInt(Integer::parseInt).toArray();
		sc.close();
		System.out.println("Linear search : " + linearSearch(arr, x));
		System.out.println("binary search : " + binarySearch(arr, 0, arr.length - 1, x));
	}

	// O(n)
	private static int linearSearch(int[] arr, int x) {
		for (int i = 0; i < arr.length; i++) {
			if (arr[i] == x) {
				return i;
			}
		}
		return -1;
	}

	// O(logn)
	private static int binarySearch(int[] arr, int low, int high, int x) {
		if (low >= arr.length || high < 0) {
			return -1;
		}
		int mid = (low + high) / 2;
		if (arr[mid] == x) {
			return mid;
		}
		if (x < arr[mid]) {
			return binarySearch(arr, low, mid - 1, x);
		} else {
			return binarySearch(arr, mid + 1, high, x);
		}
	}
}
