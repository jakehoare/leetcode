/*
https://leetcode.com/problems/bulls-and-cows/
You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to
guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits
in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits
match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses
and hints to eventually derive the secret number.
Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls
and B to indicate the cows. Please note that both secret number and friend's guess may contain duplicate digits.
You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.

Array digits contains the balance of count of that digit seen so far in secret - count of that digit seen so far in
guess.  Incrementing over the strings and provided digit is not a bull, if digits[s] is negative than we have seen this
digit already in guess so have a cow.  Likewise if digits[g] is positive then we have seen this digit already in
secret so have a cow.
Time - O(n)
Space - O(1)
*/

public class Solution {
    public String getHint(String secret, String guess) {
        int bulls = 0;
        int cows = 0;
        int digits[] = new int[10];     // balance of secret - guess (excluding bulls)

        for (int i = 0; i < secret.length(); ++i) {
            int g = Character.getNumericValue(guess.charAt(i));
            int s = Character.getNumericValue(secret.charAt(i));

            if (s == g)
                bulls++;
            else {
                if (digits[s] < 0)
                    cows++;
                if (digits[g] > 0)
                    cows++;
                digits[s]++;
                digits[g]--;
            }
        }

        return Integer.toString(bulls) + "A" + Integer.toString(cows) + "B";

    }
}
