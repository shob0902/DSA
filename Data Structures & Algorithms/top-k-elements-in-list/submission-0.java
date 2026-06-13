class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer,Integer> map=new HashMap<>();
        for(int n:nums){
            map.put(n,map.getOrDefault(n,0)+1);
        }
        PriorityQueue<Map.Entry<Integer, Integer>> max=new PriorityQueue<>((a,b)->b.getValue()-a.getValue());
        max.addAll(map.entrySet());
        int[] top=new int[k];
        for(int i=0;i<k&&!max.isEmpty();i++){
            top[i]=max.poll().getKey();
        }
        return top;
    }
}
