class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        wordParts = ["",""]

        for word in words:
            # Collects the first half of the word
            wordParts[0] = word[0:int(len(word)/2)]

            # Checks to see if the word is odd. If so, adds one as to skip middle letter
            # Also reverses the second half of the word to attempt to match the first
            if len(word)%2 == 1:
                wordParts[1] = word[int(len(word)/2)+1:len(word)]
                wordParts[1] = wordParts[1][::-1]
            else:
                wordParts[1] = word[int((len(word)/2)):len(word)]
                wordParts[1] = wordParts[1][::-1]
            
            # If both parts of the word match, returns the word
            if wordParts[0] == wordParts[1]:
                return word
            


        return ""
            
        