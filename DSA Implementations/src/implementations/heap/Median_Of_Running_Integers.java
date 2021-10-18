package implementations.Heap;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Median_Of_Running_Integers {
    public static void main(String[] args) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        int median = -1;
        Scanner sc = new Scanner(System.in);
        
        for (int i = 0; i < 10; i++) {
            int x = sc.nextInt();

            //push element in correct heap
            if (x < median) {
                maxHeap.add(x);
            } else {
                minHeap.add(x);
            }

            //rebalncing heaps such that difference of both heap size is not more than 1
            if(maxHeap.size() > minHeap.size() + 1) {
                minHeap.add(maxHeap.poll());
            } else if (minHeap.size() > maxHeap.size() + 1) {
                maxHeap.add(minHeap.poll());
            }
            //Calculating median
            if(minHeap.size() == maxHeap.size()) {
                median = (minHeap.peek() + maxHeap.peek()) / 2;
            } else if (minHeap.size() > maxHeap.size()) {
                median = minHeap.peek();
            } else {
                median = maxHeap.peek();
            }

            System.out.println("Median = " + median);

        }
        sc.close();
    }
}
