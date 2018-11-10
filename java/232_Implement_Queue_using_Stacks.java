/*
https://leetcode.com/problems/implement-queue-using-stacks/
Implement the following operations of a queue using stacks.
push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.

Use stackA to push and stackB to pop.  If stackB is empty then transfer all of stackA to stackB (inverts order).
Time - O(1) to push, O(n) (best case is O(1)) to pop and peek.
Space - O(n)
*/

class MyQueue {

    private Stack<Integer> stackA = new Stack<Integer>();
    private Stack<Integer> stackB = new Stack<Integer>();

    // Push element x to the back of queue.
    public void push(int x) {
        stackA.push(x);
    }

    // Removes the element from in front of queue.
    public void pop() {
        if (stackB.isEmpty())
            while (!stackA.isEmpty())
                stackB.push(stackA.pop());
        int x = stackB.pop();
    }

    // Get the front element.
    public int peek() {
        if (stackB.isEmpty())
            while (!stackA.isEmpty())
                stackB.push(stackA.pop());
        return stackB.peek();
    }

    // Return whether the queue is empty.
    public boolean empty() {
        return stackA.isEmpty() && stackB.isEmpty();
    }
}
