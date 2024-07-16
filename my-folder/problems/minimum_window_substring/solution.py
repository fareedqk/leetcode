class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or t == "": # base case
            return ""
        count_t, window = {}, {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        have, need = 0, len(count_t)
        res, res_len = [-1, -1], float('inf')
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in count_t and window[c] == count_t[c]:
                have += 1
            
            while have == need:
                # update our result
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                # pop from left of the window
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if res_len != float("inf") else ""

            

        