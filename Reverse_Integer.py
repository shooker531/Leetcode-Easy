class Solution:
    def reverse(self, x: int) -> int:
        # Start by placing the integer in a list as its easier to manipulate
        list = [i for i in str(x)]
        # Find the length of the list
        x = len(list)
        if x > 32:
            print("Error, integer too large")
        else:
            # If the last element of that list is 0 then we remove it due to it                
            # being unwanted once we reverse the integer
            if list[x-1] == '0':
                list.pop(x-1)
            # If there is a negative sign then we simply add that to the end of the            
            # list so once it is reversed it will be at the start 
            if list[0] == "-":
                list.pop(0)
                list.append("-")  
            # We reverse the list and then join it into one string before returning              
            # the output
            reverse = list[-1::-1]
            output = ''.join(reverse)
        return(output)
        
        
        
