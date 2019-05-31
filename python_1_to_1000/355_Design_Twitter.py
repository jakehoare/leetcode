_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/design-twitter/
# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to
# see the 10 most recent tweets in the user's news feed. Your design should support the following methods:
# - postTweet(userId, tweetId): Compose a new tweet.
# - getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
# - follow(followerId, followeeId): Follower follows a followee.
# - unfollow(followerId, followeeId): Follower unfollows a followee.

# Map users to set of followers and list of tweets with timestamps.  getNewsFeed by creating a heap of the most recent
# tweet from each followed (including self).
# Time - O(1) for init, postTweet, follow and unfollow. O(n) where n is nb followed to getNewsFeed
# Space - O(max(u**2), t) where u is nb users who could potentially all folow each other, t is nb tweets

from collections import defaultdict
import heapq

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.tweets[userId].append([-self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by
        users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        self.followers[userId].add(userId)                          # always follow self (even if unfollowed earlier)
        following = {u for u in self.followers[userId] if self.tweets[u]}   # list of people followed who have tweeted
        last_tweet_i = {u : len(self.tweets[u]) - 1 for u in following}     # mapping from followed user to index of last tweet
        tweet_heap = [self.tweets[u][last_tweet_i[u]] + [u] for u in following]     # most recent tweet from each followed
        heapq.heapify(tweet_heap)
        feed = []
        while following and len(feed) < 10:             # stop if 10 tweets or no more from followed
            _, tweetId, u = heapq.heappop(tweet_heap)   # uses included so can update with next most recent tweet
            feed.append(tweetId)
            last_tweet_i[u] -= 1
            if last_tweet_i[u] == -1:
                following.remove(u)     # no more tweets
            else:
                heapq.heappush(tweet_heap, self.tweets[u][last_tweet_i[u]] + [u])

        return feed

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.followers[followerId].discard(followeeId)