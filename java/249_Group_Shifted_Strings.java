/*
https://leetcode.com/problems/group-shifted-strings/
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd".
We can keep "shifting" to form a sequence.
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Shift each string so the rirst char is 'a'.  Map each such shifted string to a list of original unshifted strings.
Return the map values.
Time - O(n), where n is the total length in chars of all strings
Space - O(n)
*/

public class Solution {
    public List<List<String>> groupStrings(String[] strings) {

        List<List<String>> groups = new ArrayList<List<String>>();
        Map<String, List<String>> equivalents = new HashMap<String, List<String>>();

        for (String s : strings) {

            int shift = s.charAt(0) - 'a';                      // number of shifts to make first char 'a'
            StringBuilder shifted = new StringBuilder("a");     // first char is always 'a'

            for (int i = 1; i < s.length(); ++i) {              // shift each char
                int c = s.charAt(i) - shift;
                if (c < 'a')                                    // mod 26
                    c += 26;
                shifted.append((char) c);
            }

            String shiftString = shifted.toString();
            if (!equivalents.containsKey(shiftString))
                equivalents.put(shiftString, new ArrayList<String>());
            equivalents.get(shiftString).add(s);                // add to mapping

        }

        for (String shiftString : equivalents.keySet())
            groups.add(equivalents.get(shiftString));

        return groups;
    }
}
