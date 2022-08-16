# Trie Tree
This section explains some basic concepts of tires trees first and will give some ideas of how to insert, search and delete keys from a trie tree
## Table of  contents
- [Concept](#Concept)
- [Insertion](#Insertion)
- [Deletion](#Deletion)
- [Search](#Search)

### Concept
In the previous section, we covered several common types of trees like Red-Black trees, 2-3 trees, etc.

Now, we are going to look at a tree-like data structure that proves to be really efficient while solving programming problems related to strings.

This data structure is called a trie and is also known as a Prefix Tree. We will soon find out why.

The tree trie is derived from “retrieval.” As you can guess, the main purpose of using this structure is to provide fast retrieval. Tries are mostly used in dictionary word searches, search engine auto-suggestions, and IP routing as well.

**Structure**
![image](https://github.com/lyb1234567/CS_Self_Study/blob/master/Data%20Structre%20and%20Algorithm/Trie/image/Tire.PNG?raw=true)
### Insertion
The basic idea of insertion is about three different cases

**Case 1: No Common Prefix**
If we are going to insertion a word that doesn't exist in the existing tree, then it is quite stargitforwar, we just simply insert all the letters that we want to add in the tree

**Case 2: Common Prefix**
This occurs when a portion of the starting characters of your word already in the trie starting from the root node.

For example, if we want to insert a new word **there** in the trie which consists of a word **their**, the path till **the** already exists. After that, we need to insert two nodes for **r** and **e** as shown below.

**Case 3: Word Exists**
This occurs if your word is a substring of another word that already exists in the trie.

For example, if we want to insert a word **the** in the trie which already contains **their**, **the** path for the already exists. Therefore, we simply need to set the value of isEndWord to **true** at e in order to represent the end of the word for the as shown below.

```python
def insert(self, key):
        if key is None:
            return False  # None key

        key = key.lower()  # Keys are stored in lowercase
        current = self.root

        # Iterate over each letter in the key
        # If the letter exists, go down a level
        # Else simply create a TrieNode and go down a level
        for letter in key:
            index = self.get_index(letter)

            if current.children[index] is None:
                current.children[index] = TrieNode(letter)
                print(letter, "inserted")

            current = current.children[index]

        current.is_end_word = True
        print("'" + key + "' inserted")

```
### Deletion
Same for the insertion
```python
def delete_helper(self, key, current, length, level):
        deleted_self = False

        if current is None:
            print("Key does not exist")
            return deleted_self

        # Base Case:
        # We have reached at the node which points
        # to the alphabet at the end of the key
        if level is length:
            # If there are no nodes ahead of this node in
            # this path, then we can delete this node
            print("Level is length, we are at the end")
            if current.children.count(None) == len(current.children):
                print("- Node", current.char, ": has no children, delete it")
                current = None
                deleted_self = True

            # If there are nodes ahead of current in this path
            # Then we cannot delete current. We simply unmark this as leaf
            else:
                print("- Node", current.char, ": has children, don't delete \
                it")
                current.is_end_word = False
                deleted_self = False

        else:
            index = self.get_index(key[level])
            print("Traverse to", key[level])
            child_node = current.children[index]
            child_deleted = self.delete_helper(
                key, child_node, length, level + 1)
            # print( "Returned from", key[level] , "as",  child_deleted)
            if child_deleted:
                # Setting children pointer to None as child is deleted
                print("- Delete link from", current.char, "to", key[level])
                current.children[index] = None
                # If current is a leaf node then
                # current is part of another key
                # So, we cannot delete this node and it's parent path nodes
                if current.is_end_word:
                    print("- - Don't delete node", current.char, ": word end")
                    deleted_self = False

                # If child_node is deleted and current has more children
                # then current must be part of another key
                # So, we cannot delete current Node
                elif current.children.count(None) != len(current.children):
                    print("- - Don't delete node", current.char, ": has \
                    children")
                    deleted_self = False

                # Else we can delete current
                else:
                    print("- - Delete node", current.char, ": has no children")
                    current = None
                    deleted_self = True

            else:
                deleted_self = False

        return deleted_self

```
### Search
Just scan the whole tree
```python
 if key is None:
            return False  # None key

        key = key.lower()
        current = self.root

        # Iterate over each letter in the key
        # If the letter doesn't exist, return False
        # If the letter exists, go down a level
        # We will return true only if we reach the leafNode and
        # have traversed the Trie based on the length of the key

        for letter in key:
            index = self.get_index(letter)
            if current.children[index] is None:
                return False
            current = current.children[index]

        if current is not None and current.is_end_word:
            return True

        return False

```


