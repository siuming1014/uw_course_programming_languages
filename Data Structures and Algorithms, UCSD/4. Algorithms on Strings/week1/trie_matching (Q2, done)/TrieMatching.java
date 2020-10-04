import java.io.*;
import java.util.*;

public class TrieMatching implements Runnable {

	class Node
	{
		public static final int Letters =  4;
		public static final int NA      = -1;
		public int next [];

		Node ()
		{
			next = new int [Letters];
			Arrays.fill (next, NA);
		}
	}

	int letterToIndex (char letter)
	{
		switch (letter)
		{
			case 'A': return 0;
			case 'C': return 1;
			case 'G': return 2;
			case 'T': return 3;
			default: assert (false); return Node.NA;
		}
	}

	List<Map<Character, Integer>> buildTrie(String[] patterns) {
        List<Map<Character, Integer>> trie = new ArrayList<Map<Character, Integer>>();

        // write your code here
        trie.add(new HashMap<Character, Integer>());
        for (String pattern: patterns) {
            int curPos = 0;
            for (char symbol: pattern.toCharArray()) {
                Integer nextPos = trie.get(curPos).get(symbol);
                if (nextPos == null) {
                    nextPos = trie.size();
                    trie.add(new HashMap<Character, Integer>());
                    trie.get(curPos).put(symbol, nextPos);
                }
                curPos = nextPos;
            }
        }
        return trie;
	}
	
	boolean prefixTrieMatching(List<Map<Character, Integer>> trie, String text) {
		// System.out.println(trie.toString());
		int curPos = 0;
		for (char symbol: text.toCharArray()) {
			Integer nextPos = trie.get(curPos).get(symbol);
			if (nextPos == null) {
				// mismatch
				return false;
			}
			if (trie.get(nextPos).isEmpty()) {
				// we are at leaf!
				return true;
			}
			curPos = nextPos;
		}
		return false;
	}

	List <Integer> solve (String text, int n, List <String> patterns) {
		List <Integer> result = new ArrayList <Integer> ();

		// write your code here
		List<Map<Character, Integer>> trie = buildTrie(patterns.toArray(new String[0]));
		for (int i = 0; i < text.length(); i++) {
			if (prefixTrieMatching(trie, text.substring(i))) {
				result.add(i);
			}
		}
		return result;
	}

	public void run () {
		try {
			BufferedReader in = new BufferedReader (new InputStreamReader (System.in));
			String text = in.readLine ();
		 	int n = Integer.parseInt (in.readLine ());
		 	List <String> patterns = new ArrayList <String> ();
			for (int i = 0; i < n; i++) {
				patterns.add (in.readLine ());
			}

			List <Integer> ans = solve (text, n, patterns);

			for (int j = 0; j < ans.size (); j++) {
				System.out.print ("" + ans.get (j));
				System.out.print (j + 1 < ans.size () ? " " : "\n");
			}
		}
		catch (Throwable e) {
			e.printStackTrace ();
			System.exit (1);
		}
	}

	public static void main (String [] args) {
		new Thread (new TrieMatching ()).start ();
	}
}
