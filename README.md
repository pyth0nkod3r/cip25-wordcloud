# Miracle's Word Cloud Generator

## Overview

This project provides a robust and modular Python application for generating word clouds from text data. It is designed with a clear separation of concerns, making it easy to understand, maintain, and extend. Whether you want to visualize the most frequent words in a document, analyze text from sample files, or explore custom text inputs, this tool offers a user-friendly interface and customizable options.

## Features

- **Flexible Text Input**: Generate word clouds from direct text input or pre-defined sample files.
- **Advanced Text Processing**: Includes comprehensive text cleaning (lowercase conversion, punctuation removal, number removal, whitespace normalization) and intelligent stop word filtering.
- **Customizable Word Clouds**: Control the maximum number of words displayed, choose from a variety of color schemes, and set custom background colors.
- **Shaped Word Clouds**: Utilize mask images to generate word clouds in custom shapes.
- **Modular Design**: Built with an object-oriented approach, separating functionalities into distinct modules for better organization and reusability.
- **Informative Output**: Provides detailed information about the generated word cloud, including total words displayed and number of occurences.
- **Easy Saving**: Save generated word clouds as image files (PNG, JPG) for later use.

## Modular Structure

The application is structured into several interconnected modules, each responsible for a specific aspect of the word cloud generation process:

- `config_module.py`: Centralizes all application-wide configuration settings, including default values for word cloud parameters, stop words, color schemes, and UI settings. This module acts as a single source of truth for all configurable aspects of the application.

- `file_manager.py`: Manages all file-related operations. This includes reading text from files, creating and managing sample text files, and handling file paths. It ensures robust error handling for file access and encoding issues.

- `text_processor.py`: Responsible for cleaning and preparing raw text data. It performs tasks such as converting text to lowercase, removing punctuation, numbers, URLs, and email addresses, tokenizing text into individual words, and filtering out common stop words and short words.

- `word_counter.py`: Focuses on analyzing processed text to determine word frequencies. It takes a list of words and returns a dictionary of word counts, optionally limiting the results to the most frequent words.

- `wordcloud_visualizer.py`: Handles the core logic for generating and displaying word clouds. It leverages the `wordcloud` and `matplotlib` libraries to create visually appealing word clouds, offering options for color schemes, background colors, and custom shapes using mask images.

- `user_interface.py`: Manages all interactions with the user. This module is responsible for displaying menus, prompting for user input, validating choices, and presenting messages, errors, and word cloud information in a clear and user-friendly manner.

- `wordcloud_main.py`: The main entry point of the application. It acts as the orchestrator, initializing all other modules and coordinating the overall workflow from user input to word cloud generation and display. It ties all the modular components together to provide a seamless user experience.

This modular design enhances maintainability, readability, and allows for easy updates or extensions to specific functionalities without affecting the entire system. Each module is designed to be self-contained and perform a single, well-defined task.




## Installation

To get started with the Word Cloud Generator, follow these simple steps:

1.  **Clone the Repository (Optional)**:
    If you are getting the code from a repository, you can clone it using Git:
    ```bash
    git clone git@github.com:pyth0nkod3r/cip25-wordcloud.git
    cd cip25-wordcloud
    ```

2.  **Download the Files**:
    Ensure all the Python files (`config_module.py`, `file_manager.py`, `text_processor.py`, `word_counter.py`, `wordcloud_visualizer.py`, `user_interface.py`, `wordcloud_main.py`) are in the same directory on your local machine.

3.  **Install Required Libraries**:
    The application relies on several Python libraries. You can install them using `pip`:
    ```bash
    pip install matplotlib wordcloud numpy Pillow
    ```
    -   `matplotlib`: For creating and displaying plots.
    -   `wordcloud`: The core library for generating word clouds.
    -   `numpy`: Used internally by `wordcloud` for efficient numerical operations.
    -   `Pillow`: A friendly fork of PIL (Python Imaging Library), required by `wordcloud` for image processing, especially for shaped word clouds.

## Usage

Once you have installed the necessary libraries and placed all the Python files in the same directory, you can run the application from your terminal:

```bash
python3 wordcloud_main.py
```

Upon running, the application will present you with a main menu:

```
============================================================
                   WELCOME TO THE WORD CLOUD GENERATOR
============================================================

This tool helps you visualize text data as beautiful word clouds.
Let's get started!

============================================================
                         MAIN MENU
============================================================
1. Enter text directly
2. Choose from sample files
3. Exit
============================================================
```

Follow the on-screen prompts to generate your word cloud:

1.  **Enter text directly**: Choose this option to type or paste text directly into the console. Press Enter twice to signal the end of your input.

2.  **Choose from sample files**: The application comes with pre-defined sample text files (e.g., Shakespeare, Random, Test, Technology, Nature, Literature). You can select one from the list to generate a word cloud.

3.  **Exit**: Terminate the program.

After selecting your text source, you will be asked if you want to customize the word cloud settings. If you choose 'yes', you can specify:

-   **Maximum number of words**: Limit the number of words displayed in the word cloud.
-   **Color scheme**: Select from various pre-defined color palettes (e.g., random, blue, warm, nature, purple, ocean, sunset, forest, monochrome).
-   **Background color**: Set the background color of the word cloud image (e.g., 'white', 'black', 'lightblue').

Once the word cloud is generated, it will be displayed in a new window. You will also be given the option to save the word cloud as an image file (defaulting to `.png`).

### Example Workflow:

1.  Run `python3 wordcloud_main.py`.
2.  Select option `2` to choose from sample files.
3.  Select `shakespeare.txt`.
4.  Choose whether to customize settings (e.g., select 'blue' color scheme).
5.  View the generated word cloud.
6.  Opt to save the word cloud image.

Enjoy creating your word clouds!


