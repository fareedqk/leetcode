class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # pair: [temp, idx]
        res = [0] * len(temperatures)

        # for i in range(len(temperatures)):
        #     while stack and temperatures[i] > temperatures[stack[-1]]:
        #         idx = stack.pop()
        #         res[idx] = i - idx
        #     stack.append(i)
        
        for i , t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackIdx = stack.pop()
                res[stackIdx] = (i - stackIdx)
            stack.append([t, i])
            
        return res