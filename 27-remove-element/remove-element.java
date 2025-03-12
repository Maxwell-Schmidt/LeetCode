class Solution {
    public int removeElement(int[] nums, int val) {
        int numBack = nums.length-1;
        int countRemoved = 0;
        for(int i = 0; i<nums.length; i++){
            System.out.println(nums[i]);
            if(nums[i] == val){
                int end = nums[numBack];
                nums[i] = end;
                nums[numBack] = -1;
                countRemoved++;
                numBack--;
                i--;
            }
        }
        return nums.length-countRemoved;
    }
}