# Runtime Complexity: O(n^2) - O(n log n) for the inplace sort with comparator, O(n) for the for loop on line 8, O(n) for python list.insert() function
# space complexity: O(n) additional space for storing the final result
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # sort the people descending by heigh and increasing by k
        people.sort(key=lambda x: (-x[0], x[1]))
        result = []
        
        for p in people:
            result.insert(p[1], p)
        
        return result
            
        