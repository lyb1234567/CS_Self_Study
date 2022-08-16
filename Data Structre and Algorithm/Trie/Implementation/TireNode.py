class TrieNode:
    def __init__(self, char=''):
        self.children = [None] * 26  
        self.is_end_word = False 
        self.char = char  