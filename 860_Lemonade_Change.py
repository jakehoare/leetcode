_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/lemonade-change/
# At a lemonade stand, each lemonade costs $5.
# Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills).
# Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.
# You must provide the correct change to each customer, so that the net transaction is that the customer pays $5.
# Note that you don't have any change in hand at first.
# Return true if and only if you can provide every customer with correct change.

# Maintain a count of the number of 5 and 10 dollar notes held. For $5 paid, no change is given and for $10 paid
# we must give $5 change. For $20 given, try to use $10 in change if possible since there is no other use for $10.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        fives, tens = 0, 0          # no need to record twnetys, since they can never be used for change

        for bill in bills:

            if bill == 5:           # no change required
                fives += 1

            elif bill == 10:        # must have $5 change
                if fives == 0:
                    return False
                fives -= 1
                tens += 1

            elif bill == 20:        # try to use $10 + $5
                if tens >= 1 and fives >= 1:
                    tens -= 1
                    fives -= 1
                elif fives >= 3:    # else try 3 * $5
                    fives -= 3
                else:
                    return False

        return True