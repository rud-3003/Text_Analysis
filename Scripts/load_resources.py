import os

# Define paths
base_folder = os.path.dirname(os.path.abspath(__file__))  # Base folder where this script is located
stopwords_folder = os.path.join(base_folder, '../StopWords')
dictionary_folder = os.path.join(base_folder, '../MasterDictionary')

# Load StopWords
def load_stopwords():
    stopwords_files = [
        "StopWords_Auditor.txt",
        "StopWords_Currencies.txt",
        "StopWords_DatesandNumbers.txt",
        "StopWords_Generic.txt",
        "StopWords_GenericLong.txt",
        "StopWords_Geographic.txt",
        "StopWords_Names.txt"
    ]
    stopwords = set()
    for file_name in stopwords_files:
        try:
            file_path = os.path.join(stopwords_folder, file_name)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                # Debugging: Print each loaded file and word count
                words = [word.strip().lower() for word in f if word.strip()]
                stopwords.update(words)
        except Exception as e:
            print(f"Error loading {file_name}: {e}")
    print(f"Total StopWords loaded: {len(stopwords)}")
    return stopwords


# Load Positive and Negative Words
def load_dictionaries():
    try:
        with open(os.path.join(dictionary_folder, "positive-words.txt"), 'r', encoding='utf-8', errors='ignore') as f:
            positive_dict = set(word.strip().lower() for word in f if word.strip() and not word.startswith(";"))

        with open(os.path.join(dictionary_folder, "negative-words.txt"), 'r', encoding='utf-8', errors='ignore') as f:
            negative_dict = set(word.strip().lower() for word in f if word.strip() and not word.startswith(";"))

    except Exception as e:
        print(f"Error loading dictionaries: {e}")
        positive_dict = set()
        negative_dict = set()

    return positive_dict, negative_dict

# Test the loading
if __name__ == "__main__":
    stopwords = load_stopwords()
    positive_dict, negative_dict = load_dictionaries()

    print(f"StopWords loaded: {len(stopwords)}")
    print(f"Positive words loaded: {len(positive_dict)}")
    print(f"Negative words loaded: {len(negative_dict)}")
