from collections import Counter
from dataclasses import dataclass, field


@dataclass
class Node:
    children: dict = field(default_factory=dict)
    children_lengths: Counter = field(default_factory=Counter)


class Trie:
    def __init__(self, words):
        self._root = Node()
        
        for word in words:
            cur = self._root
            remain_length = len(word)
            for char in word:
                if char not in cur.children:
                    cur.children[char] = Node()
                cur.children_lengths[remain_length] += 1
                remain_length -= 1
                cur = cur.children[char]
    
    def match(self, query):
        cur = self._root
        static = query.replace('?', '')
        
        if len(query) not in cur.children_lengths:
            return 0
        
        for char in static:
            if char in cur.children:
                cur = cur.children[char]
            else:
                return 0

        return cur.children_lengths[len(query) - len(static)]

def solution(words, queries):
    t1, t2 = Trie(words), Trie(w[::-1] for w in words)
    return [t2.match(q[::-1]) if q[0] == '?' else t1.match(q) for q in queries]
