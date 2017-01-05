/*
https://leetcode.com/problems/flip-game/
You are playing the following Flip Game with your friend: Given a string that contains only these two
characters: + and -, you and your friend take turns to flip two consecutive "++" into "--".
The game ends when a person can no longer make a move and therefore the other person will be the winner.
Write a function to compute all possible states of the string after one valid move.

Check for consecutive pair of '+' chars.
Time - O(n**2)
Space - O(n**2)
*/

public class Solution {
    public List<String> generatePossibleNextMoves(String s) {

        List<String> nextMoves = new ArrayList<String>();

        for (int i = 1; i < s.length(); ++i) {
            if (s.charAt(i-1) == '+' && s.charAt(i) == '+')     // compare primitives with ==
                nextMoves.add(s.substring(0, i-1) + "--" + s.substring(i+1));
        }
        return nextMoves;
    }
}