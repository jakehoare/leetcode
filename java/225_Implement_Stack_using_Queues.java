/*
https://leetcode.com/problems/implement-stack-using-queues/
Implement the following operations of a stack using queues.
    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    empty() -- Return whether the stack is empty.

When pushing, cycle round all previous items (pop then push) so newest is always at front of queue.
Time - O(n) to push, O(1) to pop and peek.
Space - O(n)
*/

class MyStack {

    private Queue<Integer> queue = new LinkedList<>();

    // Push element x onto stack.
    public void push(int x) {
        int length = queue.size();
        queue.add(x);
        for (int i = 0; i < length; ++i) {
            queue.add(queue.poll());
        }
    }

    // Removes the element on top of the stack.
    public void pop() {
        queue.poll();
    }

    // Get the top element.
    public int top() {
        return queue.peek();
    }

    // Return whether the stack is empty.
    public boolean empty() {
        return queue.isEmpty();
    }
}
