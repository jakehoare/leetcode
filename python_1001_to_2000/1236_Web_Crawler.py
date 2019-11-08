_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/web-crawler/
# Given a url startUrl and an interface HtmlParser,
# implement a web crawler to crawl all links that are under the same hostname as startUrl.
# Return all urls obtained by your web crawler in any order.
# Your crawler should:
# Start from the page: startUrl
# Call HtmlParser.getUrls(url) to get all urls from a webpage of given url.
# Do not crawl the same link twice.
# Explore only the links that are under the same hostname as startUrl.

# Find the hostname from startUrl.
# Depth-first search the web by checking is a url has not been seen and had the correct hostname.
# If so, add it to the result and recurse for all links.
# Time - O(m + n) for m links and n urls.
# Space - O(m + n)

class Solution(object):
    def crawl(self, startUrl, htmlParser):
        """
        :type startUrl: str
        :type htmlParser: HtmlParser
        :rtype: List[str]
        """
        PREFIX = "http://"
        n = len(PREFIX)

        def get_host_and_path(url):
            suffix = url[n:]
            if "/" not in suffix:
                return [suffix, ""]
            return suffix.split("/", 1)

        start_host, _ = get_host_and_path(startUrl)
        results = set()

        def dfs(url):
            if url in results:
                return

            host, path = get_host_and_path(url)
            if host != start_host:
                return

            results.add(url)
            for next_url in htmlParser.getUrls(url):
                dfs(next_url)

        dfs(startUrl)
        return list(results)



