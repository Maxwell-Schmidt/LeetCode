class Solution {
    public int removeDuplicates(int[] nums) {
        int startInd = 1;
        for(int i = 1; i<nums.length;i++){
            if(nums[i] != nums[i-1]){
                nums[startInd]= nums[i];
                startInd++;
            }
        }
        return startInd;
    }
}