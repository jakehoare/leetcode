/*
https://leetcode.com/problems/self-dividing-numbers/
A self-dividing number is a number that is divisible by every digit it contains.
For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
Also, a self-dividing number is not allowed to contain the digit zero.
Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds
if possible.

Iterate over nums. For each num, find the remainder from dividing by 10 and if zero or num is not divisible by
remainder then do not add to result. If division by 10 can be repeated until num is zero, add to result.
Time - O(n * ln right)
Space - O(n)
*/

class Solution {
    private boolean isSelfDividing(int num) {
        int copy = num;
        int digit;
        while (copy > 0) {
            digit = copy % 10;
            copy = copy / 10;
            if (digit == 0 || num % digit != 0)
                return false;
        }
        return true;
    }

    public List<Integer> selfDividingNumbers(int left, int right) {
        List<Integer> result = new LinkedList<>();
        for (int num = left; num <= right; ++num) {
            if (isSelfDividing(num))
                result.add(num);
        }
        return result;
    }
}
