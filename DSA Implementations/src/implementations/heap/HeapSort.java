package implementations.Heap;
import java.util.Arrays;
import java.util.Scanner;

/**
 * Construct heap using given array.
 * Largeest element will be on top. swap it with last element.
 * Call heapify.reducesize by 1. Reapeat this process unitll size > 0.
 * 
 
 */
public class HeapSort {
    int[] heap = new int[10];
    int size = 0;
    public static void main(String[] args) {
        HeapSort sort = new HeapSort();
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < 10; i++) {
            sort.insert(sc.nextInt());
        }

        System.out.println(Arrays.toString(sort.heap));

        sort.sort();

        System.out.println(Arrays.toString(sort.heap));
        sc.close();
     }

     private void swap(int a, int b) {
         int x = heap[a];
         heap[a] = heap[b];
         heap[b] = x;
     }
     private void insert(int x) {
        heap[size] = x;
        int temp = size;
        while(heap[temp] > heap[temp / 2]) {
            this.swap(temp, temp/2);
            temp = temp / 2;
        }
        size++;
     }

     private void heapify(int pos) {
         int l = 2*pos+1;
         int r = 2*pos+2;
         int x = pos;
          
        if(l < size && heap[x] < heap[l]) {
            x = l;
        }

        if(r < size && heap[x] < heap[r]) {
            x = r;
        }
        if(pos != x) {
            this.swap(pos, x);
            this.heapify(x);
        }
    }
     private void sort() {
       //  int tempSize = size;
        while(size > 0) {
            this.swap(0, size-1);
            size--;
            heapify(0);
        }
     }
}

