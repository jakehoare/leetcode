/*
https://leetcode.com/problems/longest-word-in-dictionary/
Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one
character at a time by other words in words. If there is more than one possible answer, return the longest word with
the smallest lexicographical order. If there is no answer, return the empty string.

Convert words to a set. For each word, if it is better than current longest then update longest if the set contains
all prefixes of the word.
Time - O(n**2), for each string examine possible all other strings
Space - O(n)
*/

class Solution {
    public String longestWord(String[] words) {

        String longest = "";
        Set<String> wordSet = new HashSet(Arrays.asList(words));

        for (String candidate:wordSet) {
            // candidate is longer or same length and lexicographically before longest
            if (candidate.length() > longest.length() || (candidate.length() == longest.length() && candidate.compareTo(longest) < 0)) {
                // check if all prefixes are in wordSet
                boolean allPrefixes = true;
                for (int i = 1; i <= candidate.length(); ++i) {
                    if (!wordSet.contains(candidate.substring(0, i))) {
                        allPrefixes = false;
                        break;
                    }
                }
                if (allPrefixes)
                    longest = candidate;
            }
        }

        return longest;
    }
}
