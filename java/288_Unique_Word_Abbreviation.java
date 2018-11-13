/*
https://leetcode.com/problems/unique-word-abbreviation/
An abbreviation of a word follows the form <first letter><number><last letter>.
Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary.
A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

Note that words of length less than 2 are abbreviated to themselves.
Create a map from abbreviations to words.  If an abbreviation has already been used then it is mapped to the empty
String.  New word has unique abbreviation if that abbreviation has not been used or has only been used to abbreviate
that word.
Time - O(n) for constructor, O(1) for isUnique()
Space - O(n)
*/



public class ValidWordAbbr {

    private Map<String, String> map;                // instance variable (adding static could make class variable)

    public ValidWordAbbr(String[] dictionary) {     // constructor
        map = new HashMap<String, String>();

        for (String word : dictionary) {
            String abbreviation = abbreviate(word);

            if (map.containsKey(abbreviation) && !map.get(abbreviation).equals(word))   // .equals() to compare Strings
                map.put(abbreviation, "");
            else
                map.put(abbreviation, word);
        }
    }

    public boolean isUnique(String word) {
        String abbreviation = abbreviate(word);
        return !map.containsKey(abbreviation) || map.get(abbreviation).equals(word);
    }

    public String abbreviate(String word) {
        if (word.length() <= 2)
            return word;
        return word.charAt(0) + Integer.toString(word.length()-2) + word.charAt(word.length()-1);
    }

}
// Your ValidWordAbbr object will be instantiated and called as such:
// ValidWordAbbr vwa = new ValidWordAbbr(dictionary);
// vwa.isUnique("Word");
// vwa.isUnique("anotherWord");
