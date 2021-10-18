package implementations.Heap;
import java.util.Arrays;

public class MaxHeapUsingArray {
	public static void main(String[] args) {
		MaxHeap heap = new MaxHeap(10);
		heap.insert(500);
		heap.insert(200);
		heap.insert(150);
		heap.insert(175);
		heap.insert(185);
		heap.insert(186);
		heap.insert(187);
		heap.insert(10101010);
		heap.insert(167);
		heap.insert(168);
		//heap.print();
		System.out.println(heap.peek());
		//System.out.println(heap.pop());

		heap.print();

		
	}
}

class MaxHeap {

	int maxSize = 0;
	int size = 0;
	int[] heap;
	int top = 0;

	public MaxHeap(int maxSize) {
		this.maxSize = maxSize;
		heap = new int[maxSize + 1];
		//heap[0] = Integer.MIN_VALUE;
	}

	private int parent(int pos) {
		return (pos) / 2;
	}

	private int leftChild(int pos) {
		return 2 * pos + 1;
	}

	private int rightChild(int pos) {
		return 2 * pos + 2;
	}

	private void heapify(int pos) {
		if (pos < size) {
			if (heap[pos] < heap[leftChild(pos)] || heap[pos] < heap[rightChild(pos)]) {
				if (heap[leftChild(pos)] > heap[rightChild(pos)]) {
					swap(pos, leftChild(pos));
					heapify(leftChild(pos));
				} else {
					swap(pos, rightChild(pos));
					heapify(rightChild(pos));
				}
			}
		}
	}

	private void swap(int a, int b) {
		int tmp = heap[a];
		heap[a] = heap[b];
		heap[b] = tmp;
	}

	public int peek() {
		if (size == 0) {
			throw new RuntimeException();
		}
		return heap[top];
	}

	public void insert(int data) {
		if (size == maxSize) {
			throw new RuntimeException();
		}
		
		heap[size] = data;
		//size++;
		int child = size;
		while (heap[child] > heap[parent(child)]) {
			swap(child, parent(child));
			child = parent(child);
		}
		size++;
	}

	public int pop() {
		if (size == 0) {
			throw new RuntimeException();
		}
		int data = heap[top];
		heap[top] = heap[size--];
		heapify(top);
		return data;

	}

	public void print() {
		for (int i = 0; i < size/2; i++) {
			System.out.println(heap[2*i+1] + "<---" + heap[i] + "--->" + heap[2*i+2]);
		}
		System.out.println(Arrays.toString(heap));
		System.out.println();
		System.out.println();
	}
}
