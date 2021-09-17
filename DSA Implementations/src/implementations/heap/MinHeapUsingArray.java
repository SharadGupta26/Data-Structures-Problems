package implementations.heap;

import java.util.Arrays;

public class MinHeapUsingArray {

	public static void main(String[] args) {
		MinHeap heap = new MinHeap(10);
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

class MinHeap {
	int maxSize = 0;
	int[] heap;
	int size = 0;

	public MinHeap(int size) {
		maxSize = size;
		heap = new int[size+1];
	}

	private int right(int pos) {
		return 2 * pos + 2;
	}

	private int parent(int pos) {
		return pos / 2;
	}

	private int left(int pos) {
		return 2 * pos + 1;
	}

	private void heapify(int pos) {
		if (heap[pos] > heap[left(pos)] || heap[pos] < heap[right(pos)]) {
			if (heap[left(pos)] < heap[right(pos)]) {
				swap(pos, left(pos));
				heapify(left(pos));
			} else {
				swap(pos, right(pos));
				heapify(right(pos));
			}
		}
	}

	private void swap(int a, int b) {
		int t = heap[a];
		heap[a] = heap[b];
		heap[b] = t;
	}

	public int peek() {
		return heap[0];
	}

	public void insert(int data) {
		heap[size] = data;
		int cur = size;
		while (heap[cur] < heap[parent(cur)]) {
			swap(cur, parent(cur));
			cur = parent(cur);
		}
		size++;
	}

	public int pop() {
		int data = heap[0];
		heap[0] = heap[1];
		heapify(0);
		return data;
	}

	public void print() {
		for (int i = 0; i < size / 2; i++) {
			System.out.println(heap[2 * i + 1] + "<---" + heap[i] + "--->" + heap[2 * i + 2]);
		}
		System.out.println(Arrays.toString(heap));
		System.out.println();
		System.out.println();
	}
}
