package Array;

/**
 * Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.


 * @author sharadgupta
 *
 */
class Median_Of_Two_Sorted_Array {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int i =0 ;
        int j=0;
        int k=0;
        double res = 0.0;
        int[] arr = new int[nums1.length + nums2.length];
        while(i<nums1.length && j<nums2.length) {
            if(nums1[i] == nums2[j]) {
                arr[k] = nums1[i];
                i++;
                k++;
                arr[k] = nums2[j];
                k++;
                j++;
            } else if(nums1[i] < nums2[j]) {
                arr[k] = nums1[i];
                i++;
                k++;
            } else {
                arr[k] = nums2[j];
                k++;
                j++;
            }
        }
        
        while(i<nums1.length) {
            arr[k] = nums1[i];
                i++;
                k++;
        }
        
        while(j<nums2.length) {
            arr[k] = nums2[j];
                k++;
                j++;
        }
        
        int l = arr.length;
        if(l %2 == 0) {
            res = arr[l/2] + arr[(l-1)/2];
            res = res/2.0;
        } else {
            res = arr[l/2];
        }
        return res;
    }
}