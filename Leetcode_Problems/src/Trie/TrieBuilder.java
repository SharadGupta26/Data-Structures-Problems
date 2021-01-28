package Trie;

public class TrieBuilder {

	/**
	 * Returns true if insertion was successful. Returns false if word already exist
	 */
	public boolean insert(TrieNode n, String word) {
		boolean inserted = false;
		TrieNode temp = n;
		for (char c : word.toCharArray()) {
			if (!temp.childs.containsKey(c)) {
				temp.childs.put(c, new TrieNode());
				inserted = true;
			}
			temp = temp.childs.get(c);
		}
		temp.isWord = true;
		return inserted;
	}
	
	public boolean findWord(TrieNode n, String word) {
		for(char c : word.toCharArray()) {
			if(!n.childs.containsKey(c)) {
				return false;
			} else {
				n = n.childs.get(c);
			}
		}
		return n.isWord;
	}
}
