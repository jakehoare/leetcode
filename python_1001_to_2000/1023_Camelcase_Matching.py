_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/camelcase-matching/
# A query word matches a given pattern if we can insert lowercase letters to the pattern so that it equals the query.
# We may insert each character at any position, and may insert 0 characters.
# Given a list of queries, and a pattern, return an answer list of booleans,
# where answer[i] is true if and only if queries[i] matches the pattern.

# For each query, iterate over the pattern and track the index of the next char of query to be matched.
# If the query is upper case and does not match the pattern then they cannot match.
# Move past all the chars in the query that are lower case and do not match the pattern, since they can be inserted.
# If the query ends before all the pattern is matched, return False. Else there is a match.
# Return False if there are any unmatched upper case chars in the pattern after all the query is matched.
# Repeat for each query.
# Time - O(nm) for n queries of length m.
# Space - O(m)

class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        def can_match(query):
            i = 0                                   # index of next char to match in query
            for c in pattern:

                while i < len(query) and c != query[i]:
                    if query[i].isupper():
                        return False
                    i += 1

                if i == len(query):                 # reached end of query with some pattern remaining
                    return False
                i += 1

            return query[i:] == query[i:].lower()   # remainder is all lower case

        return [can_match(query) for query in queries]
