/*
https://leetcode.com/problems/judge-route-circle/
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle,
which means it moves back to the original place.
The move sequence is represented by a string. And each move is represent by a character.
The valid robot moves are R (Right), L (Left), U (Up) and D (down).
The output should be true or false representing whether the robot makes a circle.

Steps left must be opposite of steps right and steps up must be opposite of steps down.
Time - O(n)
Space - O(2)
*/

class Solution {
    public boolean judgeCircle(String moves) {

        int vertical = 0;
        int horizontal = 0;

        for (int i = 0; i < moves.length(); ++i) {
            if (moves.charAt(i) == 'U')
                ++vertical;
            else if (moves.charAt(i) == 'D')
                --vertical;
            else if (moves.charAt(i) == 'R')
                ++horizontal;
            else if (moves.charAt(i) == 'L')
                --horizontal;
        }
        return vertical == 0 && horizontal == 0;
    }
}
