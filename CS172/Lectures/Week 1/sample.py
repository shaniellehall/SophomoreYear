import string
import re

class Spellchecker:
    """
    A spell checker class that loads a dictionary of valid words
    and provides functionality to check if words are spelled correctly.
    """
    
    def __init__(self, dictionary_filename):
        """
        Constructor that loads valid words from a dictionary file.
        
        Args:
            dictionary_filename (str): Name of the file containing valid words
        """
        self.valid_words = set()  # Use set for O(1) lookup time
        
        try:
            with open(dictionary_filename, 'r', encoding='utf-8') as file:
                for line in file:
                    # Strip whitespace and convert to lowercase
                    word = line.strip().lower()
                    if word:  # Only add non-empty words
                        self.valid_words.add(word)
            print(f"Dictionary loaded successfully with {len(self.valid_words)} words.")
            
        except FileNotFoundError:
            print(f"Error: Dictionary file '{dictionary_filename}' not found.")
            raise
        except Exception as e:
            print(f"Error reading dictionary file: {e}")
            raise
    
    def check(self, word):
        """
        Check if a word is in the dictionary.
        
        Args:
            word (str): The word to check
            
        Returns:
            bool: True if word is in dictionary, False otherwise
        """
        # Convert to lowercase for case-insensitive comparison
        return word.lower() in self.valid_words


def extract_words(text_line):
    """
    Extract words from a line of text by removing punctuation and splitting.
    
    Args:
        text_line (str): A line of text
        
    Returns:
        list: List of clean words (lowercase, no punctuation)
    """
    # Remove punctuation and convert to lowercase
    # Use regex to keep only letters and spaces
    cleaned_line = re.sub(r'[^a-zA-Z\s]', ' ', text_line)
    cleaned_line = cleaned_line.lower()
    
    # Split into words and filter out empty strings
    words = [word for word in cleaned_line.split() if word]
    
    return words


def main():
    """
    Main function that runs the spell checker program.
    """
    print("=== Spell Checker Lab ===\n")
    
    # Step 1: Get dictionary file name
    dictionary_file = input("Enter dictionary file name: ").strip()
    if not dictionary_file:
        print("Error: Dictionary file name cannot be empty.")
        return
    
    # Step 2: Create Spellchecker instance
    try:
        spell_checker = Spellchecker(dictionary_file)
    except:
        print("Failed to create spell checker. Exiting.")
        return
    
    # Step 3: Get text file to check
    text_file = input("Enter text file name to check: ").strip()
    if not text_file:
        print("Error: Text file name cannot be empty.")
        return
    
    # Step 4: Read and process the text file
    try:
        misspelled_words = []
        
        with open(text_file, 'r', encoding='utf-8') as file:
            line_number = 0
            
            for line in file:
                line_number += 1
                words = extract_words(line)
                
                for word in words:
                    if not spell_checker.check(word):
                        if word not in misspelled_words:  # Avoid duplicates
                            misspelled_words.append(word)
        
        # Step 5: Display results
        print(f"\n=== Spell Check Results ===")
        print(f"File processed: {text_file}")
        
        if not misspelled_words:
            print("✅ No misspelled words found!")
        else:
            print(f"❌ Found {len(misspelled_words)} misspelled word(s):")
            print("-" * 30)
            for i, word in enumerate(misspelled_words, 1):
                print(f"{i:2d}. {word}")
                
    except FileNotFoundError:
        print(f"Error: Text file '{text_file}' not found.")
    except Exception as e:
        print(f"Error reading text file: {e}")


if __name__ == "__main__":
    main()
