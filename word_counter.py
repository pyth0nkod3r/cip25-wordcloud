"""
Word Counter Module
"""

from typing import List, Dict


class WordCounter:
    """
    Counts the frequency of words and provides methods to retrieve top words.
    """

    def count_word_frequencies(
        self, words: List[str], max_words: int = 50
    ) -> Dict[str, int]:
        """
        Count frequency of each word and return the top N words.
        """
        if not words:
            return {}

        word_count = {}  # Initialize empty dictionary

        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

        # Return only the top words
        return dict(sorted_words[:max_words])
