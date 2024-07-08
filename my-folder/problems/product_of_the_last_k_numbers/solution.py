class ProductOfNumbers:

    def __init__(self):
        self.queue = deque() # It is preferred over a list in the cases where we need quicker append and pop operations from both the ends of the container.
        self.count_of_one = 0

    def add(self, num: int) -> None:
        # adding elements in the queue
        self.queue.append(num)
        if num == 1:
            self.count_of_one += 1

    def getProduct(self, k: int) -> int:
        if self.count_of_one == len(self.queue):
            return 1
        else:
            product = 1
            lst = []
            while k > 0:
                q = self.queue.pop()
                product *= q
                lst.append(q) 
                k -= 1
            lst = lst[::-1] # Reverse

            for i in lst:
                self.queue.append(i)
        return product

        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)