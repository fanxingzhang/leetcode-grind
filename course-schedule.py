class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        sched = collections.defaultdict(set)
        
        def bfs(graph, child, parent):
            q = collections.deque()
            q.append(child)
            while q:
                node = q.popleft()
                if node == parent:
                    return True
                for next_child in graph[node]:
                    q.append(next_child)

            return False

        for pair in prerequisites:
            parent, child = pair
            if child in sched and bfs(sched, child, parent):
                return False
            sched[parent].add(child)

        return True