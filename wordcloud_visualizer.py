"""
Word Cloud Visualizer Module
Handles the generation and display of word clouds.
"""

import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
import random
from typing import Dict, Any, Optional
from config_module import Config


class WordCloudVisualizer:
    """
    Generates and displays word cloud visualizations.
    """
    
    def __init__(self):
        self.config = Config()
        self.width = self.config.DEFAULT_WIDTH
        self.height = self.config.DEFAULT_HEIGHT
        self.color_schemes = self.config.COLOR_SCHEMES
        self.wordcloud_settings = self.config.WORDCLOUD_SETTINGS
    
    def get_color_function(self, scheme: str = 'random'):
        """
        Create a color function for the word cloud.
        """
        if scheme not in self.color_schemes or scheme == 'random':
            return None  # Use WordCloud default
        
        colors = self.color_schemes[scheme]
        
        def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
            """Return a random color from the chosen scheme"""
            return random.choice(colors)
        
        return color_func
    
    def create_word_cloud(self, word_count: Dict[str, int], color_scheme: str = 'random', 
                          background_color: str = 'white', mask_image_path: Optional[str] = None,max_words: int = 50, fill_canvas: bool = False) -> Optional[WordCloud]:
        """
        Create the word cloud visualization using the wordcloud library.
        """
        if not word_count:
            print("No words to display!")
            return None
        
        # mask = None
        if mask_image_path:
            try:
                from PIL import Image
                mask_image = Image.open(mask_image_path).convert("L")  # Grayscale
                # Binarize: everything above 128 becomes 255 (white), else 0 (black)
                mask_image = mask_image.point(lambda x: 255 if x > 128 else 0, mode='L')
                mask = np.array(mask_image)
                print(f"Using custom shape from {mask_image_path}")
                # if mask is not None:
                    # print(f"Mask shape: {mask.shape}, dtype: {mask.dtype}, unique values: {np.unique(mask)}")
            except Exception as e:
                print(f"Could not load mask image: {e}")
                print("Using default rectangular shape")
                mask = None
        
        print(f"Creating word cloud with {len(word_count)} unique words...")
        
        settings = self.wordcloud_settings.copy()
        
        if fill_canvas:
            settings['relative_scaling'] = 1
            settings['min_font_size'] = 5
            settings['max_font_size'] = None  # Let it scale up
            settings['margin'] = 0
            settings['prefer_horizontal'] = 0.5
            max_words = max(max_words, 200)  # Ensure more words if possible
            
        settings.pop('background_color', None)
        settings.pop('max_words', None)
        wordcloud = WordCloud(
            width=self.width,
            height=self.height,
            background_color=background_color,
            mask=mask,
            max_words=max_words,
            color_func=self.get_color_function(color_scheme),
            **settings
        ).generate_from_frequencies(word_count)
        
        # Create the plot
        plt.figure(figsize=(self.width/100, self.height/100), facecolor=background_color)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')  # Remove axes for cleaner look
        plt.title('Word Cloud', fontsize=16, pad=20)
        plt.tight_layout(pad=0)
        plt.gca().set_facecolor(background_color)  # Set axes background
        
        # Show the plot
        plt.show()
        
        plt.savefig('wordcloud.png', bbox_inches='tight', pad_inches=0, transparent=True)
        
        return wordcloud
    
    def save_word_cloud(self, wordcloud: WordCloud, filename: str = 'wordcloud.png') -> bool:
        """
        Save the word cloud to a file.
        """
        if wordcloud is None:
            print("No word cloud to save!")
            return False
        
        try:
            wordcloud.to_file(filename)
            print(f"Word cloud saved as '{filename}'")
            return True
        except Exception as e:
            print(f"Error saving word cloud: {e}")
            return False
    
    def get_word_cloud_info(self, wordcloud: WordCloud) -> Dict[str, Any]:
        """
        Get information about the generated word cloud.
        """
        if wordcloud is None:
            return {"error": "No word cloud available"}
        
        layout = wordcloud.layout_
        
        info = {
            'total_words_displayed': len(layout),
            'image_size': (wordcloud.width, wordcloud.height),
            'words_with_positions': layout[:self.config.UI_SETTINGS['max_display_words']] if layout else []  # Show top N
        }
        
        return info


