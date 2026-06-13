class Solution {
    public int maxProfit(int[] pr) {
        int b=pr[0];
        int p=0;
        for(int i=1;i<pr.length;i++){
            if(b>pr[i]){
                b=pr[i];
            }
            p=Math.max(p,pr[i]-b);
        }
        return p;
    }
}
