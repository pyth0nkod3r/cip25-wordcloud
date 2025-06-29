#!/usr/bin/env python3
"""
Word Cloud Generator - Main Program
"""

import sys

from config_module import Config
from file_manager import FileManager
from text_processor import TextProcessor
from user_interface import UserInterface
from word_counter import WordCounter
from wordcloud_visualizer import WordCloudVisualizer


class WordCloudApp:
    """
    Main application class that orchestrates all components.

    This class follows the Controller pattern, coordinating between
    different specialized classes without containing business logic itself.
    """

    def __init__(self):
        """Initialize all components of the application."""
        self.config = Config()
        self.file_manager = FileManager()
        self.text_processor = TextProcessor()
        self.word_counter = WordCounter()
        self.visualizer = WordCloudVisualizer()
        self.ui = UserInterface()

        # Initialize sample files
        self.file_manager.create_sample_files()

    def run(self):
        """
        Main application loop.

        This method orchestrates the entire user experience from start to finish.
        """
        self.ui.show_welcome_message()

        while True:
            try:
                # Get user's text source choice
                choice = self.ui.get_main_menu_choice()

                if choice == 3:  # Exit
                    self.ui.show_goodbye_message()
                    break

                # Get text based on user choice
                text = self._get_text_from_choice(choice)

                if not text:
                    self.ui.show_error("No text to process. Please try again.")
                    continue

                # Process the text and create word cloud
                self._process_and_visualize(text)

                # Ask if user wants to continue
                if not self.ui.ask_continue():
                    self.ui.show_goodbye_message()
                    break

            except KeyboardInterrupt:
                self.ui.show_message("\nProgram interrupted by user.")
                self.ui.show_goodbye_message()
                break
            except Exception as e:
                self.ui.show_error(f"An unexpected error occurred: {e}")
                if not self.ui.ask_continue():
                    break

    def _get_text_from_choice(self, choice):
        """
        Get text content based on user's menu choice.
        """
        if choice == 1:
            return self.ui.get_user_text_input()

        elif choice == 2:
            return self._handle_sample_file_selection()

        # elif choice == 3:
        #     return self._handle_custom_file_selection()

        return ""

    def _handle_sample_file_selection(self):
        """Handle the sample file selection process."""
        sample_files = self.file_manager.get_available_sample_files()

        if not sample_files:
            self.ui.show_message("No sample files found. Creating samples...")
            self.file_manager.create_sample_files()
            sample_files = self.file_manager.get_available_sample_files()

        selected_file = self.ui.get_file_selection(sample_files)

        if selected_file:
            filepath = self.file_manager.get_sample_file_path(selected_file)
            text = self.file_manager.read_text_file(filepath)
            if text:
                self.ui.show_message(f"Loaded: {selected_file}")
            return text

        return ""

    # def _handle_custom_file_selection(self):
    #     """Handle custom file selection process."""
    #     filepath = self.ui.get_custom_file_path()
    #
    #     if filepath and self.file_manager.file_exists(filepath):
    #         text = self.file_manager.read_text_file(filepath)
    #         if text:
    #             self.ui.show_message(
    #                 f"Loaded: {self.file_manager.get_filename(filepath)}"
    #             )
    #         return text
    #
    #     return ""

    def _process_and_visualize(self, text):
        """
        Process text and create word cloud visualization.
        """
        self.ui.show_message("Processing text...")

        # Get user preferences for customization
        preferences = self.ui.get_user_preferences() if self.ui.ask_customize() else {}
        max_words = preferences.get("max_words", self.config.DEFAULT_MAX_WORDS)
        color_scheme = preferences.get("color_scheme", self.config.DEFAULT_COLOR_SCHEME)

        try:
            # Step 1: Process the text
            processed_text = self.text_processor.process_text(text)
            self.ui.show_processing_step("Text cleaned", len(processed_text))

            # Step 2: Count word frequencies
            word_frequencies = self.word_counter.count_word_frequencies(
                processed_text, max_words
            )
            self.ui.show_word_count_info(word_frequencies)

            # Step 3: Create and display word cloud
            background_color = preferences.get("background_color", self.config.DEFAULT_BACKGROUND_COLOR)
            mask_image_path = preferences.get("mask_image_path")
            max_words = preferences.get("max_words", self.config.DEFAULT_MAX_WORDS)
            color_scheme = preferences.get("color_scheme", self.config.DEFAULT_COLOR_SCHEME)
            
            wordcloud = self.visualizer.create_word_cloud(
                word_frequencies, color_scheme=color_scheme,     background_color=background_color,
                mask_image_path=mask_image_path
            )

            if wordcloud:
                # Show top words to user
                self.ui.show_top_words(word_frequencies)
                # Handle saving if requested
                self._handle_save_request(wordcloud)

        except Exception as e:
            self.ui.show_error(f"Error processing text: {e}")

    def _handle_save_request(self, wordcloud):
        """Handle user request to save the word cloud."""
        if self.ui.ask_save():
            filename = self.ui.get_save_filename()
            success = self.visualizer.save_word_cloud(wordcloud, filename)
            if success:
                self.ui.show_message(f"Word cloud saved as '{filename}'")
            else:
                self.ui.show_error("Failed to save word cloud")


def main():
    """Entry point of the application."""
    try:
        app = WordCloudApp()
        app.run()
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
