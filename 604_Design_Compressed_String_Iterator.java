/*
https://leetcode.com/problems/design-compressed-string-iterator/
Design and implement a data structure for a compressed string iterator.
It should support the following operations: next and hasNext.
The given compressed string will be in the form of each letter followed by a positive integer representing the
number of this letter existing in the original uncompressed string.
next() - if the original string still has uncompressed characters, return the next letter; Otherwise return a space.
hasNext() - Judge whether there is any letter needs to be uncompressed.

Trach the current character and count of remaining instances. When count falls to zero, parse next character and count.
Time - O(n)
Space - O(1)
*/

class StringIterator {

    private int next = 0;
    private int count = 0;
    private String compressed;
    private char c;

    public StringIterator(String compressedString) {
        compressed = compressedString;
    }

    public char next() {

        if (!hasNext())
            return ' ';

        if (count > 0) {
            --count;
            return c;
        }

        c = compressed.charAt(next);
        count = Character.getNumericValue(compressed.charAt(next + 1));
        next += 2;
        while (next < compressed.length() && Character.isDigit(compressed.charAt(next)))
            count = count * 10 + Character.getNumericValue(compressed.charAt(next++));

        --count;
        return c;
    }

    public boolean hasNext() {
        return !(count == 0 && next >= compressed.length());
    }
}