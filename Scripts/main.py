import os
import pandas as pd
import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from load_resources import load_dictionaries, load_stopwords

# Load StopWords, Positive and Negative Dictionaries
stopwords = load_stopwords()
positive_dict, negative_dict = load_dictionaries()  

# Define paths
base_folder = os.path.dirname(os.path.abspath(__file__))
input_folder = os.path.join(base_folder, '../ExtractedTexts')
output_file = '../Output_Data_Structure.xlsx'

# Helper functions
def count_syllables(word):
    word = word.lower()
    vowels = "aeiouy"
    count = sum(1 for char in word if char in vowels)
    if word.endswith(('es', 'ed')) and count > 1:
        count -= 1
    return max(1, count)

def calculate_analysis_metrics(text):
    # Tokenize text
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    cleaned_words = [word.lower() for word in words if word.isalpha() and word.lower() not in stopwords]

    # Positive and Negative Scores
    positive_score = sum(1 for word in cleaned_words if word in positive_dict)
    negative_score = sum(1 for word in cleaned_words if word in negative_dict)
    polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
    subjectivity_score = (positive_score + negative_score) / (len(cleaned_words) + 0.000001)

    # Readability Metrics
    total_words = len(cleaned_words)
    total_sentences = len(sentences)
    avg_sentence_length = total_words / total_sentences if total_sentences > 0 else 0

    complex_words = [word for word in cleaned_words if count_syllables(word) > 2]
    percentage_complex_words = len(complex_words) / total_words if total_words > 0 else 0
    fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)

    # Additional Metrics
    avg_words_per_sentence = total_words / total_sentences if total_sentences > 0 else 0
    word_count = total_words
    syllables_per_word = sum(count_syllables(word) for word in cleaned_words) / total_words if total_words > 0 else 0
    avg_word_length = sum(len(word) for word in cleaned_words) / total_words if total_words > 0 else 0

    # Personal Pronouns Count
    personal_pronouns = len(re.findall(r'\b(I|we|my|ours|us)\b', text, re.IGNORECASE))

    return {
        "URL_ID": "",  # Placeholder to be filled later
        "URL": "",  # Placeholder to be filled later
        "POSITIVE SCORE": positive_score,
        "NEGATIVE SCORE": negative_score,
        "POLARITY SCORE": polarity_score,
        "SUBJECTIVITY SCORE": subjectivity_score,
        "AVG SENTENCE LENGTH": avg_sentence_length,
        "PERCENTAGE OF COMPLEX WORDS": percentage_complex_words,
        "FOG INDEX": fog_index,
        "AVG NUMBER OF WORDS PER SENTENCE": avg_words_per_sentence,
        "COMPLEX WORD COUNT": len(complex_words),
        "WORD COUNT": word_count,
        "SYLLABLE PER WORD": syllables_per_word,
        "PERSONAL PRONOUNS": personal_pronouns,
        "AVG WORD LENGTH": avg_word_length
    }

# Analyze articles and save results
results = []
for file_name in os.listdir(input_folder):
    if file_name.endswith('.txt'):
        url_id = file_name.split('.')[0]
        with open(os.path.join(input_folder, file_name), 'r', encoding='utf-8') as file:
            text = file.read()
            metrics = calculate_analysis_metrics(text)
            metrics["URL_ID"] = url_id
            metrics["URL"] = f"URL_{url_id}" 
            results.append(metrics)

df = pd.DataFrame(results)
df = df[[
    "URL_ID", "URL", "POSITIVE SCORE", "NEGATIVE SCORE", "POLARITY SCORE", "SUBJECTIVITY SCORE", 
    "AVG SENTENCE LENGTH", "PERCENTAGE OF COMPLEX WORDS", "FOG INDEX", "AVG NUMBER OF WORDS PER SENTENCE", 
    "COMPLEX WORD COUNT", "WORD COUNT", "SYLLABLE PER WORD", "PERSONAL PRONOUNS", "AVG WORD LENGTH"
]]

# Save to Excel
df.to_excel(output_file, index=False)
print(f"Results saved to {output_file}")