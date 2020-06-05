# object initialization runtime: O(n) since we go through the entire list
# object initialization space complexity: O(n) additional space

# pickIndex runtime: O(log n) because of binary search
# pickIndex space complexity: O(1) additional space
class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []
        p_sum = 0
        for weight in w:
            p_sum += weight
            self.prefix_sum.append(p_sum)
        
        self.total_sum = p_sum
        

    def pickIndex(self) -> int:
        random_num = self.total_sum * random.random()
        low, high = 0, len(self.prefix_sum)
        while low < high:
            mid = low + (high - low) // 2
            if random_num > self.prefix_sum[mid]:
                low = mid + 1
            else:
                high = mid
        
        return low
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()