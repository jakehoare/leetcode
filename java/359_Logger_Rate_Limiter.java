/*
https://leetcode.com/problems/logger-rate-limiter/
Design a logger system that receive stream of messages along with its timestamps, each message should be printed if
and only if it is not printed in the last 10 seconds.  Given a message and a timestamp (in seconds granularity),
return true if the message should be printed in the given timestamp, otherwise returns false.

Store the last printed time of each message.  Print if not seen before or last seen at least 10 seconds ago.
Alternatively, use a heap to store only messages in the last 10 seconds, which avoids excess memory use.
Time - O(1)
Space - O(n)
*/

public class Logger {

    HashMap<String, Integer> lastPrinted;

    /** Initialize your data structure here. */
    public Logger() {
        lastPrinted = new HashMap<String, Integer>();
    }

    /** Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity. */
    public boolean shouldPrintMessage(int timestamp, String message) {
        if (!lastPrinted.containsKey(message) || timestamp - lastPrinted.get(message) >= 10) {
            lastPrinted.put(message, timestamp);
            return true;
        }
        return false;
    }
}
