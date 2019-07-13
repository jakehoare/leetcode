_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/distribute-candies-to-people/
# We distribute some number of candies, to a row of n = num_people people in the following way:
# We then give 1 candy to the first person, 2 candies to the second person,
# and so on until we give n candies to the last person.
# Then, we go back to the start of the row, giving n + 1 candies to the first person,
# n + 2 candies to the second person, and so on until we give 2 * n candies to the last person.
# This process repeats (with us giving one more candy each time, and moving to the start of the row
# after we reach the end) until we run out of candies.
# The last person will receive all of our remaining candies (not necessarily one more than the previous gift).
# Return an array (of length num_people and sum candies) that represents the final distribution of candies.

# The total number of candies distributed for n people = n * (n + 1) // 2.
# Invert this to find the number of people served given the candies (ignoring cycle back to beginning).
# The first person gets 1 + (1 + num_people) + (1 + 2 * num_people) + .... where the sum of the num_people
# series is a base amount which is the same for every person.
# After adding candies for the completed cycles, add candies until one remain.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        people_served = int(((1 + 8 * candies) ** 0.5 - 1) / 2)     # people who get their full portion
        cycles = people_served // num_people                        # complete cycles of num_people

        result = [0] * num_people
        if cycles != 0:
            base = num_people * (cycles - 1) * cycles // 2          # same for every person
            for i in range(num_people):
                result[i] += base + cycles * (i + 1)                # for each cycle, add index + 1

        last_candies = cycles * num_people
        candies -= sum(result)
        for i in range(num_people):                                 # incomplete final cycle
            if candies <= 0:
                break
            result[i] += min(candies, last_candies + i + 1)
            candies -= last_candies + i + 1

        return result