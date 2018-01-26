_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/number-of-atoms/
# Given a chemical formula (given as a string), return the count of each atom.
# An atomic element always starts with an uppercase character, then zero or more lowercase letters,
# representing the name.
# 1 or more digits representing the count of that element may follow if the count is greater than 1. If the count
# is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.
# Two formulas concatenated together produce another formula. For example, H2O2He3Mg4 is also a formula.
# A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2)
# and (H2O2)3 are formulas.
# Given a formula, output the count of all elements as a string in the following form: the first name
# (in sorted order), followed by its count (if that count is more than 1), followed by the second name
# (in sorted order), followed by its count (if that count is more than 1), and so on.

# Iterate over formula. If start of a new element, add previous element to counts. If bracket, find counts from
# within bracket and multiply by number after bracket.
# Time - O(n)
# Space - O(n)

from collections import defaultdict

class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """

        def count_atoms(start):
            counts = defaultdict(int)
            element = None
            element_count = 0
            i = start

            while i < len(formula):
                c = formula[i]

                if "A" <= c <= "Z":         # start new atom
                    if element:             # add previous atom to counts
                        counts[element] += element_count if element_count != 0 else 1
                        element_count = 0
                    element = c

                elif "a" <= c <= "z":       # add to name of current atom
                    element += c

                elif "0" <= c <= "9":       # increase count of current atom
                    element_count = int(c) + (element_count * 10 if element_count != 0 else 0)

                elif c == "(":
                    bracket_count, i = count_atoms(i + 1)   # get atom counts until closing bracket
                    bracket_multiplier = 0
                    while i + 1 < len(formula) and "0" <= formula[i + 1] <= "9":    # multiplier of bracket
                        bracket_multiplier = bracket_multiplier * 10 + int(formula[i + 1])
                        i += 1
                    for el, num in bracket_count.items():
                        counts[el] += num * (bracket_multiplier if bracket_multiplier > 0 else 1)

                else:                       # closing bracket
                    if element:             # add final element to counts
                        counts[element] += element_count if element_count != 0 else 1
                    return [counts, i]

                i += 1

            return [counts, i]

        formula = "(" + formula + ")"
        counts = count_atoms(0)[0]
        return "".join([atom + (str(count) if count > 1 else "") for atom, count in sorted(counts.items())])