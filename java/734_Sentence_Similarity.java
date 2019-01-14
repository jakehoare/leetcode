/*
https://leetcode.com/problems/sentence-similarity/
Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs,
determine if two sentences are similar.
For example, "great acting skills" and "fine drama talent" are similar, if the similar word pairs are
pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]].
Note that the similarity relation is not transitive. For example, if "great" and "fine" are similar, and "fine" and
"good" are similar, "great" and "good" are not necessarily similar.
However, similarity is symmetric. For example, "great" and "fine" being similar is the same as "fine" and
"great" being similar.
Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"],
pairs = [] are similar, even though there are no specified similar word pairs.
Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"]
can never be similar to words2 = ["doubleplus","good"].

Create mapping from first word of every pair to set of similar words. For each pair of words from words1 and words2,

Time - O(m + n), number of pairs plus length of sentence
Space - O(m)
*/

class Solution {
    public boolean areSentencesSimilar(String[] words1, String[] words2, String[][] pairs) {

        if (words1.length != words2.length)         // early return
            return false;

        Map<String, Set> words = new HashMap<>();   // mapping from word to set of similar words

        for (int i = 0; i < pairs.length; ++i) {

            String w1 = pairs[i][0];
            String w2 = pairs[i][1];

            Set set = words.getOrDefault(w1, new HashSet<String>());
            set.add(w2);
            words.put(w1, set);
        }

        for (int i = 0; i < words1.length; ++i) {

            if (words1[i].equals(words2[i]))        // words always similar to self
                continue;

            Set set = words.get(words1[i]);         // check if words2[i] is similar to words1[i]
            if (set != null && set.contains(words2[i]))
                continue;

            set = words.get(words2[i]);             // check if words1[i] is similar to words2[i]
            if (set == null || !set.contains(words1[i]))
                return false;
        }

        return true;
    }
}
