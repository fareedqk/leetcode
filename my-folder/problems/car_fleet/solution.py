class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        stack = []
        
        for x in range(len(speed)):
            pairs.append([position[x], speed[x]])
        
        pairs = sorted(pairs)[::-1]
        
        for p, s in pairs:
            # Calculate time to reach the target for the current car
            time = (target - p) / s
            
            stack.append(time)
            
            # Check if there are at least two cars in the stack and the current car
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        
        return len(stack)