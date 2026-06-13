class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        int ml = 0;
        Map<Character, Integer> map = new HashMap<>();
        int l = 0;
        
        for (int r = 0; r < n; r++) {
            char c = s.charAt(r);
            if (map.containsKey(c) && map.get(c) >= l) {
                l = map.get(c) + 1;
            }
            map.put(c, r);
            ml = Math.max(ml, r - l + 1);
        }
        
        return ml;
    }
}