# Last updated: 8/13/2026, 8:19:41 PM
class Solution(object):
    def haveConflict(self, event1, event2):
        return event1[0] <= event2[1] and event2[0] <= event1[1]