package implementations.Heap;

import java.util.Arrays;
import java.util.Scanner;
/**
 * In this we fir create max heap of k elements.
 * top element of max heap will be kth minimum till now.
 * now for remaining (n-k) elements, we replace top element of max heap if element is smaller than top.
 * and call heapify after each replacement.
 * 
 * Finally we will have kth min at top of max heap.
 * 
 * arr = [1,2,3,4,5]
 * k=5
 * max heap = [5,4,2,3,1]
 * 
 * 1 is first min
 * 2 is 2nd min
 * 3 is 3rd min
 * 4 is 4th min
 * 5 is 5th min
 * 
 * Logical explaination : in a group of k distinct elements, biggest elements is kth min element.
 */
public class KthMin_MaxHeap {
    static int[] heap;
    static int size = 0;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);    
        int[] arr = new int[10];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }

        System.out.println("enter k");
        int k = sc.nextInt();
        buildHeap(arr, k);
        for (int i = k; i < arr.length; i++) {
            if(arr[i] < peek()) {
                updateHeap(arr[i]);
            }
        }
        System.out.println(Arrays.toString(heap));
        System.out.println("kth min is : " + peek());
        sc.close();
    }

    private static void updateHeap(int i) {
        heap[0] = i;
        heapify(0);
    }

    private static int peek() {
        return heap[0];
    }

    /**
     * When you are building heap using arr,
     * you need to heapify whole array.
     * SO we run heap for all parents starting from i/2
     * 
     * When we insert data in heap, data is already heapified till last element, and we only need to heapify last inserted element.
     * @param arr
     */
    private static void buildHeap(int[] arr, int k) {
        heap = new int[k];
        for (int i = 0; i < k; i++) {
            heap[i] = arr[i];
            size++;
        }
       int x = (size-1) / 2;
       while(x>=0) { 
            heapify(x);
            x --;
       }
        
    }

    /**
     * max heapify
     */
    private static void heapify(int i) {
        int l = 2*i+1;
        int r = 2*i + 2;
        int x = i;
        if(l < size && heap[x] < heap[l]) {
            x = l;
        }

        if(r < size && heap[x] < heap[r]) {
            x = r;
        }

        if(i != x) {
            swap(i, x);
            heapify(x);
        }
    }

    private static void swap(int a, int b) {
        int t = heap[a];
        heap[a] = heap[b];
        heap[b] = t;
    }
}
