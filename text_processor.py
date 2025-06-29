"""
Text Processor Module
Handles all text cleaning, processing, and preparation for word cloud generation.
"""

import re
import string
from typing import List

from config_module import Config


class TextProcessor:
    """
    Processes raw text for word cloud generation.

    This class handles:
    - Text cleaning and normalization
    - Tokenization (splitting into words)
    - Stop word removal
    - Custom filtering options
    """

    def __init__(self):
        """Initialize the text processor with configuration."""
        self.config = Config()
        self.stop_words = (
            self.config.STOP_WORDS.copy()
        )  # Create a copy for customization
        self.min_word_length = self.config.MIN_WORD_LENGTH

    def process_text(self, text: str) -> List[str]:
        """
        Complete text processing.
        """
        if not text or not text.strip():
            return []

        # Step 1: Clean the text
        cleaned_text = self.clean_text(text)

        # Step 2: Tokenize into words
        words = self.tokenize_text(cleaned_text)

        # Step 3: Filter words
        filtered_words = self.filter_words(words)

        return filtered_words

    def clean_text(self, text: str) -> str:
        """
        Clean and normalize text for processing.
        """
        if not text:
            return ""

        # Convert to lowercase for consistency
        text = text.lower()

        # Remove most punctuation but keep apostrophes in contractions
        text = re.sub(r"[^\w\s']", " ", text)

        # Handle contractions by removing apostrophes after processing
        text = text.replace("'", "")

        # Normalize whitespace (multiple spaces become single space)
        text = " ".join(text.split())

        return text

    def tokenize_text(self, text: str) -> List[str]:
        """
        Split text into individual words (tokens).
        """
        if not text:
            return []

        # Split on whitespace
        words = text.split()

        # Additional cleaning of individual words
        cleaned_words = []
        for word in words:
            # Remove any remaining non-alphabetic characters from ends
            word = word.strip(string.punctuation + string.digits)

            if word:  # Only keep non-empty words
                cleaned_words.append(word)
        return cleaned_words

    def filter_words(self, words: List[str]) -> List[str]:
        """
        Remove stop words and words shorter than min_word_length.
        """
        return [
            word
            for word in words
            if word not in self.stop_words and len(word) >= self.min_word_length
        ]
