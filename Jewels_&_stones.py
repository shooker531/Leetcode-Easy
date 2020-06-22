class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # Start by obtaining a list of all the letters in each string
        newS = [char for char in S]
        newJ = [char for char in set(J)]
        # Ensure that each inputted string does not exceeed 50 characters 
        if len(newS) > 50:
            print("error, character length exceeded for J")
        if len(newJ) > 50:
            print("error, character length exceeded for J")
        # We initialize a count which we will later use to count the number of jewls
        count = 0
        # We then add to this count every time a charcter from J appears in S
        for a in newJ:
            for b in newS:
                if a == b:
                    count += 1
        # We then return the count
        return(count)
        
