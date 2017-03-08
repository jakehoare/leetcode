/*
https://leetcode.com/problems/moving-average-from-data-stream/
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Add the numbers to an array of size k with a pointer to indicate the next index to be replaced.
Track the sum and count.
Time - O(k) for constructor, O(1) for next()
Space - O(k)
*/

public class MovingAverage {
        public int sum = 0;
        public int count = 0;
        public int i = 0;
        public int[] window;

    /** Initialize your data structure here. */
    public MovingAverage(int size) {
        this.window = new int[size];
    }

    public double next(int val) {
        this.sum += val - this.window[i];
        this.window[i] = val;
        ++this.i;
        this.count = Math.max(this.count, this.i);
        this.i %= window.length;
        return this.sum / (double) this.count;
    }
}