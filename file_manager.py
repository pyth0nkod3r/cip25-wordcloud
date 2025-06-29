"""
File Manager Module
Handles all file operations including reading, writing, and managing sample files.
"""

import glob
import os
from typing import List

from config_module import Config


class FileManager:
    """
    Manages all file operations for the Word Cloud Generator.
    """

    def __init__(self):
        """Initialize the file manager."""
        self.config = Config()
        self.sample_directory = self.config.SAMPLE_DIRECTORY
        self._ensure_sample_directory_exists()

    def _ensure_sample_directory_exists(self):
        """Create the sample directory if it doesn't exist."""
        if not os.path.exists(self.sample_directory):
            try:
                os.makedirs(self.sample_directory)
                print(f"Created '{self.sample_directory}' directory.")
            except OSError as e:
                print(f"Warning: Could not create sample directory: {e}")

    def create_sample_files(self):
        """
        Create sample text files for users to experiment with
        """
        self._ensure_sample_directory_exists()

        created_files = []
        for filename, content in self.config.SAMPLE_FILES.items():
            filepath = os.path.join(self.sample_directory, filename)

            if not os.path.exists(filepath):
                try:
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(content.strip())
                    created_files.append(filename)
                except IOError as e:
                    print(f"Warning: Could not create {filename}: {e}")

        if created_files:
            print(f"Created sample files: {', '.join(created_files)}")

    def get_available_sample_files(self) -> List[str]:
        """
        Get a list of available sample text files.
        """
        if not os.path.exists(self.sample_directory):
            return []

        # Find all .txt files in the samples directory
        pattern = os.path.join(self.sample_directory, "*.txt")
        txt_files = glob.glob(pattern)

        # Extract just the filename without the path and sort
        filenames = [os.path.basename(file) for file in txt_files]
        return sorted(filenames)

    def get_sample_file_path(self, filename: str) -> str:
        """
        Get the full path for a sample file.
        """
        return os.path.join(self.sample_directory, filename)

    def read_text_file(self, filepath: str) -> str:
        """
        Read text from a file with robust error handling
        """
        if not os.path.exists(filepath):
            print(f"Error: File '{filepath}' not found!")
            return ""

        # use utf-8 encoding
        encodings = ["utf-8"]

        for encoding in encodings:
            try:
                with open(filepath, "r", encoding=encoding) as file:
                    content = file.read()

                    if not content.strip():
                        print(f"Warning: File '{filepath}' appears to be empty.")
                        return ""

                    # Success - return the content
                    return content

            except PermissionError:
                print(f"Error: Permission denied reading '{filepath}'")
                return ""
            except Exception as e:
                print(f"Error reading file '{filepath}': {e}")
                return ""
        print(f"Error: Could not decode '{filepath}' with any supported encoding.")
        return ""

    def write_text_file(self, filepath: str, content: str) -> bool:
        """
        Write text content to a file.
        """
        try:
            # Ensure directory exists
            directory = os.path.dirname(filepath)
            if directory and not os.path.exists(directory):
                os.makedirs(directory)

            with open(filepath, "w", encoding="utf-8") as file:
                file.write(content)
            return True

        except Exception as e:
            print(f"Error writing file '{filepath}': {e}")
            return False

    def file_exists(self, filepath: str) -> bool:
        """
        Check if a file exists.
        """
        return os.path.exists(filepath) and os.path.isfile(filepath)

    def get_filename(self, filepath: str) -> str:
        """
        Extract filename from a full path.
        """
        return os.path.basename(filepath)

    def clean_file_path(self, filepath: str) -> str:
        """
        Clean and normalize a file path.
        """
        if not filepath:
            return ""

        # Remove surrounding quotes and whitespace
        cleaned = filepath.strip().strip("\"'")

        # Normalize path separators
        cleaned = os.path.normpath(cleaned)

        # Expand the user home directory (~)
        cleaned = os.path.expanduser(cleaned)

        return cleaned
