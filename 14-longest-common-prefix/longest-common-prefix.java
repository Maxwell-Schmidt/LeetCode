class Solution {
    public String longestCommonPrefix(String[] strs) {
        String prefix = "";
        String testPrefix = strs[0];
        for(int i = 0; i < strs[0].length(); i++){
            for(int j = 0; j < strs.length; j++){
                try{
                    char testChar = strs[j].charAt(i);
                    if(testChar != testPrefix.charAt(i)){
                        return prefix;
                    }
                } catch(IndexOutOfBoundsException e) {
                    return prefix;
                }
            }
            prefix = testPrefix.substring(0,i+1);
        }
        return prefix;
    }
}