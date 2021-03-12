package Array;
import java.util.*;

/**
 * Problem Statement 
 * https://www.hackerrank.com/challenges/java-1d-array/problem
 * @author sharadgupta
 *
 */
public class Leap_Game {

    public static boolean canWin(int leap, int[] game) {
        return solve(game, leap, 0);
    }
    
    private static boolean solve(int[] a, int m, int i) {
        if(i < 0 || a[i] == 1) {
            return false;
        }
        int n = a.length;
        if(i + 1 >= n || i + m >= n ) {
            return true;
        }
        
        a[i] = 1;
        return solve(a, m ,i+1) || solve (a, m, i-1) || solve(a, m , i+m);
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int q = scan.nextInt();
        while (q-- > 0) {
            int n = scan.nextInt();
            int leap = scan.nextInt();
            
            int[] game = new int[n];
            for (int i = 0; i < n; i++) {
                game[i] = scan.nextInt();
            }

            System.out.println( (canWin(leap, game)) ? "YES" : "NO" );
        }
        scan.close();
    }
}
