_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/design-log-storage-system/
# You are given several logs that each log contains a unique id and timestamp. Timestamp is a string that has the
# following format: Year:Month:Day:Hour:Minute:Second, for example, 2017:01:01:23:59:59.
# All domains are zero-padded decimal numbers.
# Design a log storage system to implement the following functions:
#   void Put(int id, string timestamp): Given a log's unique id and timestamp, store the log in your storage system.
#   int[] Retrieve(String start, String end, String granularity): Return the id of logs whose timestamps are within the
#    range from start to end. Start and end all have the same format as timestamp. However, granularity means the time
#    level for consideration. For example, start = "2017:01:01:23:59:59", end = "2017:01:02:23:59:59",
#    granularity = "Day", it means that we need to find the logs within the range from Jan. 1st 2017 to Jan. 2nd 2017.

# Store ids and timestamps in list. Retrieve by matching timestamp prefix up to gra.
# Time - O(1) for put, O(n) for retrieve.
# Space - O(n)
# Alternatively create a tree (similar to a prefix trie) where each node stores all ids with a specific prefix. Tree
# has 6 levels. Nodes are created as required by put(). Retrieve by finding all ids greater than or equal to start that
# are also less than or equal to end. Faster to retrieve because does not have string comparison with all ids.

class LogSystem(object):
    def __init__(self):
        self.prefixes = {"Year": 4, "Month": 7, "Day": 10, "Hour": 13, "Minute": 16, "Second": 19}
        self.logs = []

    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: void
        """
        self.logs.append((id, timestamp))

    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        result = []
        pref = self.prefixes[gra]
        s_prefix, e_prefix = s[:pref], e[:pref]

        for id, timestamp in self.logs:
            if s_prefix <= timestamp[:pref] <= e_prefix:
                result.append(id)

        return result


# Alternative solution
class LogNode(object):
    def __init__(self, nb_children):
        self.ids = set()
        self.children = [None for _ in range(nb_children)]

class LogSystem2(object):
    def __init__(self):
        self.periods = ["Year", "Month", "Day", "Hour", "Minute", "Second"]
        self.nb_children = {"Year": 13, "Month": 32, "Day": 24, "Hour": 60, "Minute": 60, "Second": 0}
        self.root = LogNode(18)

    def put(self, id, timestamp):
        timelist = timestamp.split(":")
        timelist[0] = int(timelist[0]) - 2000
        node = self.root

        for t, period in zip(timelist, self.periods):
            if not node.children[int(t)]:
                node.children[int(t)] = LogNode(self.nb_children[period])
            node = node.children[int(t)]
            node.ids.add(id)

    def retrieve(self, s, e, gra):
        s_list, e_list = s.split(":"), e.split(":")
        s_list[0], e_list[0] = int(s_list[0]) - 2000, int(e_list[0]) - 2000
        s_node, e_node = self.root, self.root

        later, earlier = set(), set()
        for i in range(len(s_list)):    # find all ids later or eqaul to start

            s_val = int(s_list[i])      # get time period value
            s_child = s_node.children[s_val]  # could be None
            for node in s_node.children[s_val + 1:]:    # all later nodes
                if not node:
                    continue
                later |= node.ids
            if not s_child:
                break
            if gra == self.periods[i]:  # add terminal node ids
                later |= s_child.ids
                break

            s_node = s_child

        for i in range(len(e_list)):    # find all ids earlier or eqaul to end

            e_val = int(e_list[i])
            e_child = e_node.children[e_val]  # could be None
            for node in e_node.children[:e_val]:
                if not node:
                    continue
                earlier |= node.ids
            if not e_child:
                break
            if gra == self.periods[i]:
                earlier |= e_child.ids
                break

            e_node = e_child

        return list(earlier & later)    # set intersection

