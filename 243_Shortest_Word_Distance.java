/*
https://leetcode.com/problems/shortest-word-distance/
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Store that last index of each word. Update result with min of index difference and previous result.
Time - O(n)
Space - O(1)
*/

public class Solution {
    public int shortestDistance(String[] words, String word1, String word2) {

        int last1 = -1;
        int last2 = -1;
        int minDist = words.length;     // both words are present so minDist must be < length

        for (int i = 0; i < words.length; ++i) {

            if (words[i].equals(word1)) {
                last1 = i;
                if (last2 != -1)
                    minDist = Math.min(minDist, Math.abs(last1 - last2));
            }

            if (words[i].equals(word2)) {
                last2 = i;
                if (last1 != -1)
                    minDist = Math.min(minDist, Math.abs(last1 - last2));
            }
        }
        return minDist;
    }
}