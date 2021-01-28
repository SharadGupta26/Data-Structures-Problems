package Trie;

import java.util.HashMap;
import java.util.Map;

public class TrieNode {
	public Map<Character, TrieNode> childs = new HashMap<>();
	public boolean isWord = false;
}
