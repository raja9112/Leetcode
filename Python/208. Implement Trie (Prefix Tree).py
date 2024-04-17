# 208. Implement Trie (Prefix Tree)

# Medium

# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

# Example 1:

# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]

# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
 

# Constraints:

# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 104 calls in total will be made to insert, search, and startsWith.

# class Trie:        225ms

#     def __init__(self):
#         self.store = []

#     def insert(self, word: str) -> None:
#         self.store.append(word)

#     def search(self, word: str) -> bool:
#         if word in self.store:
#             return True
#         return False

#     def startsWith(self, prefix: str) -> bool:
#         n = len(prefix)-1
#         for i in self.store:
#             if i[0:n+1] == prefix:
#                 return True
#         return False

class trieNode:
    def __init__(self):
        self.child = {}
        self.endofword = False

class Trie:

    def __init__(self): 
        self.root = trieNode()
        
    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.child:
                cur.child[c] = trieNode()
            cur = cur.child[c]

        cur.endofword = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.child:
                return False
            cur = cur.child[c]
        return cur.endofword

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.child:
                return False
            cur = cur.child[c]
        return True

# This Python program is an implementation of a Trie (also known as a Prefix Tree), a tree-like data structure that is used to store a collection of strings. Tries are particularly useful for operations like prefix-based search.

# Here’s a breakdown of the code:

# trieNode class: This is a helper class that represents a node in the Trie. Each node has a dictionary child to store its child nodes and a boolean endofword to indicate whether this node is the end of a word in the Trie.
# Trie class: This class represents the Trie itself. It has a root node and three methods: insert, search, and startsWith.
# insert: This method takes a string word and inserts it into the Trie. It starts from the root and for each character in the word, it checks if the character is already a child of the current node. If not, it creates a new node and adds it as a child. Finally, it marks the last node as the end of a word.
# search: This method takes a string word and checks if it is in the Trie. It starts from the root and for each character in the word, it moves to the corresponding child node. If at any point the character is not a child of the current node, it returns False. If it successfully traverses the entire word, it checks if the last node is marked as the end of a word and returns this value.
# startsWith: This method takes a string prefix and checks if there is any word in the Trie that starts with this prefix. It is similar to the search method, but it doesn’t need to check the endofword value of the last node.
# This Trie implementation is efficient for operations like insert, search, and startsWith, with a time complexity of O(n), where n is the length of the word or prefix. The space complexity is O(m), where m is the total number of characters in all words stored in the Trie.


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

