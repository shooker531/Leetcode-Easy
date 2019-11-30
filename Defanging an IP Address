class Solution:
    def defangIPaddr(self, address: str) -> str:
        # Start by creating an empty string to later add to 
        newstring = ''
        # For every character from the string that passes into the function, if "." is found then it is replaced with "[.]"
        # and added to the new string
        # If it is not found then the original charcter is simply added to the new string
        for charc in address:
            if charc == "." :
                newstring += "[.]"
            else:
                newstring += charc
        # The new string is then returned
        return(newstring)
                
