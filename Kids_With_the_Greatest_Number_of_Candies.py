class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int):
        
        # Include error checks which apply to the constarints of the problem
        if len(candies) not in range(2,101):
            return "ERROR"
        for i in range(len(candies)):
            if candies[i] not in range(1,101):
                return "ERROR"
        if extraCandies not in range(51):
            return "ERROR"
        
        # Include a one line list comprehension to return the output
        return [item + extraCandies >= max(candies) for item in candies]
        
