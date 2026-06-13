class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set=new HashSet<>();
        for(int n:nums){
            set.add(n);
        }
        int ls=0;
        for(int n:set){
            if(!set.contains(n-1)){
            int cn=n;
            int cs=1;
            while(set.contains(cn+1)){
                cn++;
                cs++;
            }
            ls=Math.max(ls,cs);
        }
    }
    return ls;
    }
}