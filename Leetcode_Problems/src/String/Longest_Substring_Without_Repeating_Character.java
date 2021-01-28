package String;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;



class Longest_Substring_Without_Repeating_Character {
    public int lengthOfLongestSubstring(String s) {
        int max =0;
        for(int i=0 ; i<s.length();i++) {
            max = Integer.max(max, len(s.substring(i)));
        }
        
       
        return max;
    }
    
    private int len(String s) {
        Set<Character> set = new HashSet<>();
        int i=0;
        for(char c : s.toCharArray()) {
            if(set.contains(c)) {
                return i;
            }
            set.add(c);
            i++;
        }
        return i;
    }
    
    //better 
    //sliiding wall approach
    private int approach2(String s) {
    	int max = 0;
    	Map<Character, Integer> map = new HashMap<>();
    	char[] arr = s.toCharArray();
    	for(int i=0, j=0 ; i< arr.length ; i++) {
    		if(map.containsKey(arr[i])) {
    			j = Integer.max(map.get(arr[i]), j);
    		}
    		max = Integer.max(max, i-j+1);
    		map.put(arr[i], i+1);
    	}
    	return max;
    }
    
   
}

