_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/tag-validator/
# Given a string representing a code snippet, you need to implement a tag validator to parse the code and return
# whether it is valid. A code snippet is valid if all the following rules hold:

# 1) The code must be wrapped in a valid closed tag. Otherwise, the code is invalid.
# 2) A closed tag (not necessarily valid) has exactly the following format : <TAG_NAME>TAG_CONTENT</TAG_NAME>.
# Among them, <TAG_NAME> is the start tag, and </TAG_NAME> is the end tag. The TAG_NAME in start and end tags should
# be the same. A closed tag is valid if and only if the TAG_NAME and TAG_CONTENT are valid.
# 3) A valid TAG_NAME only contain upper-case letters, and has length in range [1,9]. Otherwise, the TAG_NAME
# is invalid.
# 4) A valid TAG_CONTENT may contain other valid closed tags, cdata and any characters (see note1) EXCEPT
# unmatched <, unmatched start and end tag, and unmatched or closed tags with invalid TAG_NAME.
# Otherwise, the TAG_CONTENT is invalid.
# 5) A start tag is unmatched if no end tag exists with the same TAG_NAME, and vice versa. However, you also need to
# consider the issue of unbalanced when tags are nested.
# 6) A < is unmatched if you cannot find a subsequent >. And when you find a < or </, all the subsequent characters
# until the next > should be parsed as TAG_NAME (not necessarily valid).
# 7) The cdata has the following format : <![CDATA[CDATA_CONTENT]]>. The range of CDATA_CONTENT is defined as the
# characters between <![CDATA[ and the first subsequent ]]>.
# 8) CDATA_CONTENT may contain any characters. The function of cdata is to forbid the validator to parse CDATA_CONTENT,
# so even it has some characters that can be parsed as tag (no matter valid or invalid), you should treat it as
# regular characters.

# Iterate over input. status variable tracks whether we are in an opening or closing tag, or in cdata or in text.
# Stack stores open tags.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def isValid(self, code):
        """
        :type code: str
        :rtype: bool
        """
        status = "text"
        tag_stack = []
        upper = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")   # chars allowed in tags
        i = 0

        while i < len(code):
            c = code[i]

            if status == "text":
                if c == "<":
                    if i + 1 < len(code) and code[i + 1] == "/":
                        status = "closing"
                        i += 2
                        tag_start = i       # record starting index in oreedr to check length
                    elif i + 8 < len(code) and code[i + 1:i + 9] == "![CDATA[" and tag_stack:   # must have opened a tag
                        status = "cdata"
                        i += 9
                    else:
                        status = "opening"
                        i += 1
                        tag_start = i
                elif not tag_stack:         # must have opened a tag
                    return False
                else:
                    i += 1

            elif status in ["opening", "closing"]:
                if code[i] == ">":
                    tag = code[tag_start:i]
                    if len(tag) < 1 or len(tag) > 9:
                        return False
                    if status == "opening":
                        tag_stack.append(tag)
                    else:
                        if not tag_stack or tag_stack.pop() != tag:
                            return False
                        if not tag_stack and i != len(code) - 1:    # cannot close all tags if not at end of code
                            return False
                    status = "text"
                elif c not in upper:
                    return False
                i += 1

            elif status == "cdata":
                if i + 2 < len(code) and code[i:i + 3] == "]]>":
                    i += 3
                    status = "text"
                else:
                    i += 1

        return status == "text" and not tag_stack
