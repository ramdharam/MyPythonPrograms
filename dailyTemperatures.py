class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        if len(temperatures) == 0:
            return []
        l = len(temperatures)
        result = []
        start, end, counter = 0, 0, 0
        while end < l:
            while (start < l - 1 and temperatures[start] > temperatures[start + 1]):
                start += 1
            start +=1
            if temperatures[start] < temperatures[end] and start == l - 1:
                result.append(0)
                end += 1
                continue
            while (end != start):
                result.append(start-end)
                end += 1
        return result


a=[73,74,75,71,69,72,76,73]
obj = Solution()
print(obj.dailyTemperatures(a))