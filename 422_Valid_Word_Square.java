/*
https://leetcode.com/problems/valid-word-square/
Given a sequence of words, check whether it forms a valid word square.
A sequence of words forms a valid word square if the kth row and column read the exact same string,
where 0 ≤ k < max(numRows, numColumns).

For each row i, check if anything in column i with row >= len(row[i]). Then for column j = i + 1 onwards, check if any
letter is in column i, row j and if so that is sam as row i, column j.
Time - O(mn)
Space - O(1)
*/

public class Solution {
    public boolean validWordSquare(List<String> words) {

        for (int i = 0; i < words.size(); ++i) {

            int rowLen = words.get(i).length();
            // test if anything in col i at or after row rowLen
            for (int row = rowLen; row < words.size(); ++row)   // each row beyond length of current word
                if (words.get(row).length() > i)                // check ith column
                    return false;

            for (int j = i + 1; j < words.get(i).length(); ++j) {   // start after diagonal

                if (j >= words.size() || i >= words.get(j).length())    // no jth row or ith column
                    return false;
                if (words.get(i).charAt(j) != words.get(j).charAt(i))
                    return false;
            }
        }
        return true;
    }
}