package Array;

/**
 * 
 * https://leetcode.com/problems/container-with-most-water/
 * @author sharadgupta
 *
 */
class Container_With_Most_Water {
    public int maxArea(int[] height) {
        int i=0, j=height.length-1,max=0;
        while(  i<j ) {
            int area = Integer.min(height[i], height[j]) * (j-i);
            if(area > max) {
                max = area;
            }
            
            if(height[i] < height[j]) {
                i++;
            } else {
                j--;
            }
        }
        return max;
    }
}