class Solution {
    public int removeDuplicates(int[] nums) {
        int lastNum = -101;
        int startInd = 0;
        for(int i = 0; i<nums.length;i++){
            if(nums[i] == lastNum){
                nums[i]= -1;
            }else{
                lastNum = nums[i];
                nums[startInd] = nums[i];
                startInd++;
            }
            System.out.println(lastNum);
        }
        return startInd;
    }
}