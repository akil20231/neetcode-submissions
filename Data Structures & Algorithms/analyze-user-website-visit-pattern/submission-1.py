from collections import defaultdict
from itertools import combinations
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        G = defaultdict(list)
        for (t, user, web) in sorted(zip(timestamp, username, website)):
            G[user].append(web)

        score = defaultdict(int)
        for user, web in G.items():
            for pattern in set(combinations(web, 3)):
                score[pattern] += 1
        
        max_pattern, max_cnt = '', 0

        for pattern, cnt in score.items():
            if cnt > max_cnt or (cnt == max_cnt and pattern < max_pattern):
                max_pattern = pattern
                max_cnt = cnt
        
        return list(max_pattern)



        