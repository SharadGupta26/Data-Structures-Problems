package implementations.Heap;
import java.util.Arrays;
import java.util.Scanner;

/**
 * In this approach we build MinHeap of n elements. 
 * And then remove k elements from heap.
 * The top element will be kth min element.
 */
public class KthMin_MinHeap {
    static int[] heap;
    static int size = 0;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[10];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }

        buildHeap(arr);
        System.out.println(Arrays.toString(heap));
        int k = sc.nextInt();
        for (int i = 1; i < k; i++) {
            pop();
        }
        System.out.println(Arrays.toString(heap));
        System.out.println("kth min element is : " + heap[0]);
        sc.close();
    }

    /**
     * When you are building heap using arr,
     * you need to heapify whole array.
     * SO we run heap for all parents starting from i/2
     * 
     * When we insert data in heap, data is already heapified till last element, and we only need to heapify last inserted element.
     * @param arr
     */
    private static void buildHeap(int[] arr) {
        heap = arr;
        size = arr.length;
        int x = (size - 1) / 2;
        while (x>=0) {
            minHeapiy(x);
            x--;
        }

    }

    private static int pop() {
        int x = heap[0];
        heap[0] = heap[size-1];
        minHeapiy(0);
        size--;
        return x;
    }

    private static void minHeapiy(int i) {
        int l = 2*i+1;
        int r = 2*i+2;
        int x = i;

        if (l < size && heap[x] > heap[l]) {
            x = l;
        }

        if (r < size && heap[x] > heap[r]) {
            x = r;
        }

        if (x != i) {
            swap(x, i);
            minHeapiy(x);
        }
    }

    private static void swap(int a, int b) {
        int tmp = heap[a];
        heap[a] = heap[b];
        heap[b] = tmp;
    }
}
