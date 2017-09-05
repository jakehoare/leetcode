_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/encode-and-decode-tinyurl/
# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and
# it returns a short URL such as http://tinyurl.com/4e9iAk.
# Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode
# algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be
# decoded to the original URL.

# Encode as a random selection of 6 letters and digits. If encoding already used, repeat.
# Time - O(1) average if load factor sufficiently low
# Space - O(nk) for n URLs of max length k

import random

class Codec:
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"  # class variable

    def __init__(self):
        self.map = {}       # shortUrl to longUrl

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        :type longUrl: str
        :rtype: str
        """
        encoding = []
        for i in range(6):
            encoding.append(self.letters[random.randint(0, 61)])
        encoding = "".join(encoding)

        if encoding in self.map:    # repeat if collision
            encoding = self.encode(longUrl)

        self.map[encoding] = longUrl
        return encoding

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        :type shortUrl: str
        :rtype: str
        """
        return self.map[shortUrl]