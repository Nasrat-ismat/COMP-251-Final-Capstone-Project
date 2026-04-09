class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.words = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word.lower():
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
        if word not in node.words:
            node.words.append(word)

    def autocomplete(self, prefix):
        node = self.root
        for ch in prefix.lower():
            if ch not in node.children:
                return []
            node = node.children[ch]

        results = []
        self._collect_words(node, results)
        return sorted(results)

    def _collect_words(self, node, results):
        if node.is_end:
            results.extend(node.words)
        for child_node in node.children.values():
            self._collect_words(child_node, results)
