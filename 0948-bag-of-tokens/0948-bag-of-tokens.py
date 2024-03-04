class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        tokens.sort()
        queue = deque(tokens)
        score = 0
        while queue and P >= queue[0]:
            while queue and P >= queue[0]:
                P -= queue.popleft()
                score += 1
            if score > 0 and len(queue) > 1:
                P += queue.pop()
                score -= 1
        return score
        