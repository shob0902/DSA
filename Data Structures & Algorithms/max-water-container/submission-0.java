class Solution {
    public int maxArea(int[] h) {
        int l=0;
        int r=h.length-1;
        int ma=0;
        while(l<r){
            int ca=Math.min(h[l],h[r])*(r-l);
            ma=Math.max(ma,ca);
            if(h[l]<h[r]){
                l++;
            }else{
                r--;
            }
        }
        return ma;
    }
}
