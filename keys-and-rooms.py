class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        d = {}
        def helper(n):
            d[n] = 1
            if not rooms[n]:
                return
            for r in rooms[n]:
                if r not in d:
                    helper(r)
        helper(0)
        return len(d) == len(rooms)