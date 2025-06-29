"""
User Interface Module
Handles all user interactions, input, and output.
"""

from typing import List, Dict, Any

from config_module import Config


class UserInterface:
    """
    Manages all interactions with the user, including displaying menus,
    getting input, and showing messages.
    """

    def __init__(self):
        """Initialize the user interface with configuration."""
        self.config = Config()
        self.menu_width = self.config.UI_SETTINGS["menu_width"]
        self.separator_char = self.config.UI_SETTINGS["separator_char"]
        self.max_display_words = self.config.UI_SETTINGS["max_display_words"]

    def _print_separator(self, char: str = None):
        """
        Prints a separator line for better readability.
        """
        if char is None:
            char = self.separator_char
        print(char * self.menu_width)

    def show_welcome_message(self):
        """
        Displays the welcome message to the user.
        """
        self._print_separator()
        print("WELCOME TO MIRACLE'S WORD CLOUD GENERATOR")
        self._print_separator()
        print("\nThis tool helps you visualize text data as beautiful word clouds.")
        print("Let's get started!\n")

    def show_goodbye_message(self):
        """
        Displays the goodbye message to the user.
        """
        self._print_separator()
        print("THANK YOU FOR USING MIRACLE'S WORD CLOUD GENERATOR!")
        self._print_separator()
        print("Goodbye!\n")

    def show_message(self, message: str):
        """
        Displays a general message to the user.
        """
        print(f"[INFO] {message}")

    def show_error(self, error_message: str):
        """
        Displays an error message to the user.
        """
        print(f"[ERROR] {error_message}")

    def get_main_menu_choice(self) -> int:
        """
        Displays the main menu and gets the user's choice.
        """
        while True:
            self._print_separator()
            print(f"{'MAIN MENU':^{self.menu_width}}")
            self._print_separator()
            print("1. Enter text directly")
            print("2. Choose from sample files")
            # print("3. Provide a custom file path")
            print("3. Exit")
            self._print_separator()

            try:
                choice = int(input("Enter your choice (1-3): "))
                if 1 <= choice <= 3:
                    return choice
                else:
                    self.show_error(
                        "Invalid choice. Please enter a number between 1 and 3."
                    )
            except ValueError:
                self.show_error("Invalid input. Please enter a number.")

    def get_user_text_input(self) -> str:
        """
        Gets multi-line text input from the user.
        """
        print("\n[INPUT] Please paste or type your text. Press Enter twice to finish:")
        lines = []
        while True:
            line = input()
            if not line:
                break
            lines.append(line)
        return "\n".join(lines)

    def get_file_selection(self, files: List[str]) -> str:
        """
        Displays a list of files and gets the user's selection.
        """
        if not files:
            self.show_message("No files available for selection.")
            return ""

        while True:
            self._print_separator()
            print("SELECT A FILE")
            self._print_separator()
            for i, file in enumerate(files):
                print(f"{i+1}. {file}")
            self._print_separator()

            try:
                choice = input(
                    f"Enter your choice (1-{len(files)}) or 'b' to go back: "
                )
                if choice.lower() == "b":
                    return ""

                choice_idx = int(choice) - 1
                if 0 <= choice_idx < len(files):
                    return files[choice_idx]
                else:
                    self.show_error("Invalid choice. Please enter a valid number.")
            except ValueError:
                self.show_error("Invalid input. Please enter a number or 'b'.")

    # def get_custom_file_path(self) -> str:
    #     """
    #     Gets a custom file path from the user.
    #     """
    #     return input("\n[INPUT] Enter the full path to your text file: ").strip()

    def ask_continue(self) -> bool:
        """
        Asks the user if they want to continue or exit.
        """
        while True:
            response = (
                input("\nDo you want to generate another word cloud? (yes[y]/no[n]): ")
                .lower()
                .strip()
            )
            if response in ["yes", "y"]:
                return True
            elif response in ["no", "n"]:
                return False
            else:
                self.show_error(
                    "Invalid response. Please type 'yes', 'y' or 'no', 'n'."
                )

    def ask_customize(self) -> bool:
        """
        Asks the user if they want to customize word cloud settings.
        """
        while True:
            response = (
                input("\nDo you want to customize the word cloud settings? (yes/no): ")
                .lower()
                .strip()
            )
            if response in ["yes", "y"]:
                return True
            elif response in ["no", "n"]:
                return False
            else:
                self.show_error(
                    "Invalid response. Please type 'yes' ,' y ' or 'no', 'n'."
                )

    def get_user_preferences(self) -> Dict[str, Any]:
        """
        Gets word cloud customization preferences from the user.
        """
        preferences = {}

        # Max words
        while True:
            try:
                max_words_input = input(
                    f"Enter maximum number of words to display (default: {self.config.DEFAULT_MAX_WORDS}): "
                ).strip()
                if not max_words_input:
                    preferences["max_words"] = self.config.DEFAULT_MAX_WORDS
                    break
                max_words = int(max_words_input)
                if max_words > 0:
                    preferences["max_words"] = max_words
                    break
                else:
                    self.show_error("Please enter a positive number.")
            except ValueError:
                self.show_error("Invalid input. Please enter a number.")

        # Color scheme
        available_schemes = self.config.get_color_scheme_names()
        while True:
            print("\nAvailable color schemes:")
            for i, scheme in enumerate(available_schemes):
                print(f"{i+1}. {scheme.capitalize()}")
            color_choice = input(
                f"Enter choice (1-{len(available_schemes)}) or leave blank for default ({self.config.DEFAULT_COLOR_SCHEME.capitalize()}): "
            ).strip()

            if not color_choice:
                preferences["color_scheme"] = self.config.DEFAULT_COLOR_SCHEME
                break

            try:
                scheme_idx = int(color_choice) - 1
                if 0 <= scheme_idx < len(available_schemes):
                    preferences["color_scheme"] = available_schemes[scheme_idx]
                    break
                else:
                    self.show_error("Invalid choice. Please enter a valid number.")
            except ValueError:
                self.show_error("Invalid input. Please enter a number.")

        # Background color (optional)
        background_color = input(
            f"Enter background color (e.g., 'white', 'black', 'lightblue', default: {self.config.DEFAULT_BACKGROUND_COLOR}): "
        ).strip()
        if background_color:
            preferences["background_color"] = background_color

        return preferences

    def show_processing_step(self, step_name: str, count: int = None):
        """
        Shows a message indicating a processing step is complete.
        """
        message = f"{step_name} complete."
        if count is not None:
            message += f" Total items: {count}"
        self.show_message(message)

    def show_word_count_info(self, word_frequencies: Dict[str, int]):
        """
        Displays information about word frequencies.
        """
        self.show_message(
            f"Found {len(word_frequencies)} unique words after filtering."
        )

    def show_top_words(self, word_frequencies: Dict[str, int]):
        """
        Displays the top words and their counts.
        """
        self._print_separator()
        print(f"{'TOP {self.max_display_words} WORDS':}")
        self._print_separator()

        if not word_frequencies:
            print("No words to display.")
            return

        # Sort and display top words
        sorted_words = sorted(
            word_frequencies.items(), key=lambda item: item[1], reverse=True
        )
        for i, (word, count) in enumerate(sorted_words[: self.max_display_words]):
            print(f"{i+1}. {word}: {count}")
        self._print_separator()


    def ask_save(self) -> bool:
        """
        Asks the user if they want to save the generated word cloud.
        """
        while True:
            response = (
                input("\nDo you want to save the word cloud image? (yes/y/no/n): ")
                .lower()
                .strip()
            )
            if response in ["yes", "y"]:
                return True
            elif response in ["no", "n"]:
                return False
            else:
                self.show_error(
                    "Invalid response. Please type 'yes'/'y' or 'no'/'n'."
                )

    def get_save_filename(self) -> str:
        """
        Gets the desired filename for saving the word cloud.
        """
        filename = input(
            f"Enter filename to save (e.g., 'my_wordcloud.png', default: 'wordcloud.{self.config.DEFAULT_SAVE_FORMAT}'): "
        ).strip()
        if not filename:
            filename = f"wordcloud.{self.config.DEFAULT_SAVE_FORMAT}"

        # Ensure it has a valid image extension
        if not (
            filename.endswith(".png")
            or filename.endswith(".jpg")
            or filename.endswith(".jpeg")
        ):
            print("Warning: Recommended image format is .png or .jpg. Appending .png.")
            filename += ".png"

        return filename
