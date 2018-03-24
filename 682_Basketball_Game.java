/*
https://leetcode.com/problems/baseball-game/
You're now a baseball game point recorder.
Given a list of strings, each string can be one of the 4 following types:
Integer (one round's score): Directly represents the number of points you get in this round.
"+" (one round's score): Represents that the points you get in this round are the sum of the last two valid
round's points.
"D" (one round's score): Represents that the points you get in this round are the doubled data of the last valid
round's points.
"C" (an operation, which isn't a round's score): Represents the last valid round's points you get were invalid
and should be removed.
Each round's operation is permanent and could have an impact on the round before and the round after.
You need to return the sum of the points you could get in all the rounds.

Stack contains scores from previous rounds.
Time - O(n)
Space - O(n)
*/

class Solution {
    public int calPoints(String[] ops) {

        Stack<Integer> st = new Stack<Integer>();

        for (String s : ops) {

            if (s.equals("C"))                  // delete
                st.pop();
            else if (s.equals("D"))             // double previous
                st.push(2 * st.peek());
            else if (s.equals("+")) {           // sum previus two rounds
                int temp = st.pop();
                int points = temp + st.peek();
                st.push(temp);
                st.push(points);
            }
            else
                st.push(Integer.parseInt(s));
        }

        int result = 0;
        while (st.size() > 0)
            result += st.pop();
        return result;
    }
}