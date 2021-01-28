package Trie;

public class TrieDriver {

	public static void main(String[] args) {
		TrieNode root = new TrieNode();
		TrieBuilder builder = new TrieBuilder();
		builder.insert(root, "aman");
		builder.insert(root, "sharad");
		builder.insert(root, "ameena");
		builder.insert(root, "shades");
		builder.insert(root, "flowers");
		builder.insert(root, "lights");
		builder.insert(root, "share");
		builder.insert(root, "ameen");
		builder.insert(root, "aman");
		builder.insert(root, "flow");
		
		
		System.out.println(builder.findWord(root, "shaam"));
		System.out.println(builder.findWord(root, "flower"));
		System.out.println(builder.findWord(root, "flowers"));
		System.out.println(builder.findWord(root, "shades"));
		System.out.println(builder.findWord(root, "flow"));
		
	}
}
