class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Creating a dict to store the values of each number, allowing for easier access
        romNums = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }

        # Creates an int to hold the sum of the roman numeral sequence
        numSum = 0

        for index in range(0,len(s)):
            # Checks to see if the string is at its end. If so automatically adds the number to sum
            if index == len(s)-1:
                numSum += romNums[s[index]]
            # If that is not the case, ensures that the number following the current is not larger than it as
            # if so, the program must subtract from the sum rather than add to it
            elif (romNums[s[index+1]]) > (romNums[s[index]]):
                numSum -= romNums[s[index]]
            # If neither of the previous cases are true, the number can simply be added to the sum
            else:
                numSum += romNums[s[index]]
        
        # Returns the created sum
        return numSum



        