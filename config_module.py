"""
Configuration Module
Contains all configuration constants and settings for the Word Cloud Generator.
"""

import os


class Config:
    """
    Configuration class containing all application settings.
    """

    # Text processing settings
    DEFAULT_MAX_WORDS = 50
    MIN_WORD_LENGTH = 3

    # Visualization settings
    DEFAULT_WIDTH = 800
    DEFAULT_HEIGHT = 600
    DEFAULT_COLOR_SCHEME = "random"
    DEFAULT_BACKGROUND_COLOR = "white"

    # File settings
    SAMPLE_DIRECTORY = "samples"
    DEFAULT_SAVE_FORMAT = "png"

    # Stop words - common words to exclude from word clouds
    STOP_WORDS = {
        "the",
        "and",
        "or",
        "but",
        "in",
        "on",
        "at",
        "to",
        "for",
        "of",
        "with",
        "by",
        "a",
        "an",
        "as",
        "are",
        "was",
        "were",
        "be",
        "been",
        "being",
        "have",
        "has",
        "had",
        "do",
        "does",
        "did",
        "will",
        "would",
        "should",
        "could",
        "can",
        "may",
        "might",
        "must",
        "shall",
        "is",
        "am",
        "this",
        "that",
        "these",
        "those",
        "i",
        "you",
        "he",
        "she",
        "it",
        "we",
        "they",
        "me",
        "him",
        "her",
        "us",
        "them",
        "my",
        "your",
        "his",
        "its",
        "our",
        "their",
        "mine",
        "yours",
        "hers",
        "ours",
        "theirs",
        "myself",
        "yourself",
        "himself",
        "herself",
        "itself",
        "ourselves",
        "yourselves",
        "themselves",
    }

    # Color schemes for word clouds
    COLOR_SCHEMES = {
        "random": None,  # WordCloud default random colors
        "blue": ["#0066CC", "#0080FF", "#3399FF", "#66B2FF", "#99CCFF"],
        "warm": ["#FF6B35", "#F7931E", "#FFD23F", "#EE4B2B", "#C21807"],
        "nature": ["#228B22", "#32CD32", "#90EE90", "#006400", "#9ACD32"],
        "purple": ["#800080", "#9932CC", "#BA55D3", "#DA70D6", "#DDA0DD"],
        "ocean": ["#006994", "#0892A5", "#13A5B7", "#1FB8C8", "#2ECBD9"],
        "sunset": ["#FF6B6B", "#FF8E53", "#FF6B35", "#C44536", "#8B2635"],
        "forest": ["#2D5016", "#3E7B27", "#4F9A31", "#6AB04C", "#9DC209"],
        "monochrome": ["#2C3E50", "#34495E", "#7F8C8D", "#95A5A6", "#BDC3C7"],
    }

    # Sample text files content
    SAMPLE_FILES = {
        "shakespeare.txt": """
        To be or not to be, that is the question: Whether 'tis nobler in the mind to suffer
        the slings and arrows of outrageous fortune, or to take arms against a sea of troubles
        and by opposing end them. To die—to sleep, no more; and by a sleep to say we end
        the heart-ache and the thousand natural shocks that flesh is heir to: 'tis a consummation
        devoutly to be wish'd. To die, to sleep; to sleep, perchance to dream—ay, there's the rub:
        for in that sleep of death what dreams may come, when we have shuffled off this mortal coil,
        must give us pause—there's the respect that makes calamity of so long life.
        For who would bear the whips and scorns of time, the oppressor's wrong, the proud man's contumely,
        the pangs of despised love, the law's delay, the insolence of office, and the spurns
        that patient merit of the unworthy takes, when he himself might his quietus make
        with a bare bodkin? Who would fardels bear, to grunt and sweat under a weary life,
        but that the dread of something after death, the undiscovered country from whose bourn
        no traveler returns, puzzles the will, and makes us rather bear those ills we have
        than fly to others that we know not of?
        """,
        "technology.txt": """
        Artificial intelligence is transforming the world in unprecedented ways. Machine learning
        algorithms are becoming more sophisticated, enabling computers to perform tasks that once
        required human intelligence. Deep learning neural networks are revolutionizing image
        recognition, natural language processing, and decision making. Cloud computing provides
        scalable infrastructure for AI applications. Data science combines statistics, programming,
        and domain expertise to extract insights from big data. Robotics and automation are
        changing manufacturing, healthcare, and service industries. Blockchain technology offers
        new possibilities for secure, decentralized systems. Quantum computing promises exponential
        improvements in computational power. Internet of Things connects everyday devices to
        create smart environments. Cybersecurity becomes increasingly important as our digital
        footprint expands. Virtual and augmented reality are creating immersive experiences.
        The future of technology lies in the intersection of AI, robotics, and human creativity.
        """,
        "nature.txt": """
        The forest whispers secrets through rustling leaves. Ancient trees stand as silent
        guardians of time, their roots deep in earth's embrace. Sunlight filters through
        the canopy, creating dancing patterns on the forest floor. Birds sing melodies
        that echo through the woodland. Streams babble over smooth stones, carrying
        life-giving water to all creatures. The cycle of seasons brings constant change
        yet eternal continuity. Spring awakens dormant life with gentle warmth. Summer
        blazes with abundant growth and vibrant colors. Autumn paints the landscape in
        gold and crimson before winter's peaceful slumber. Mountains reach toward the
        sky, their peaks crowned with snow. Valleys cradle meadows filled with wildflowers.
        Oceans pulse with ancient rhythms, waves crashing against weathered shores.
        Nature teaches us about resilience, beauty, and the interconnectedness of all
        living things. Every element plays a vital role in the grand symphony of life.
        """,
        "literature.txt": """
        Literature has the power to transport readers across time and space, into the minds
        and hearts of characters both real and imagined. Great novels explore the human
        condition through compelling narratives that resonate across generations. Poetry
        distills emotion and experience into carefully crafted verses that speak to the soul.
        Classic works by authors like Shakespeare, Dickens, Austen, and Tolstoy continue
        to captivate readers centuries after their creation. Contemporary literature reflects
        modern society's complexities, challenges, and aspirations. Short stories capture
        moments of truth in concentrated form. Memoirs and biographies reveal the fascinating
        lives of remarkable individuals. Science fiction imagines possible futures while
        fantasy creates entirely new worlds. Mystery novels challenge readers to solve
        puzzles alongside clever detectives. Romance stories celebrate the power of love
        and human connection. Literary criticism helps us understand deeper meanings and
        cultural significance. Reading expands our vocabulary, enhances our empathy, and
        broadens our understanding of the world and ourselves.
        """,
    }

    # WordCloud library-specific settings
    WORDCLOUD_SETTINGS = {
        "relative_scaling": 0.5,
        "min_font_size": 10,
        "max_font_size": 100,
        "prefer_horizontal": 0.7,
        "random_state": 42,
        "collocations": False,
        "background_color": DEFAULT_BACKGROUND_COLOR,
    }

    # User interface settings
    UI_SETTINGS = {"menu_width": 60, "separator_char": "=", "max_display_words": 10}

    @classmethod
    def get_sample_file_path(cls, filename):
        return os.path.join(cls.SAMPLE_DIRECTORY, filename)

    @classmethod
    def get_color_scheme_names(cls):
        return list(cls.COLOR_SCHEMES.keys())

    @classmethod
    def get_color_scheme_colors(cls, scheme_name):
        return cls.COLOR_SCHEMES.get(scheme_name, None)

    @classmethod
    def is_stop_word(cls, word):
        return word.lower() in cls.STOP_WORDS

    @classmethod
    def add_stop_words(cls, words):
        if isinstance(words, str):
            cls.STOP_WORDS.add(words.lower())
        elif isinstance(words, (list, set)):
            cls.STOP_WORDS.update(word.lower() for word in words)

    @classmethod
    def remove_stop_words(cls, words):
        if isinstance(words, str):
            cls.STOP_WORDS.discard(words.lower())
        elif isinstance(words, (list, set)):
            for word in words:
                cls.STOP_WORDS.discard(word.lower())
