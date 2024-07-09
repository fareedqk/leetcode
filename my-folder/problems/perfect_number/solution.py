class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        sum_divisors = 1
        # half_num = num // 2
        sqrt_num = int(num ** 0.5) # math.sqrt
        for i in range(2, sqrt_num + 1):
            if num % i == 0:
                sum_divisors += i
                if i != num // i:
                    sum_divisors += num // i
        return sum_divisors == num