# Text Analysis Project

This project performs text analysis on extracted articles, calculates various metrics, and saves the results in an Excel file. The analysis includes metrics like positive and negative scores, polarity, subjectivity, readability, and more.

## Features

- Tokenizes text into sentences and words.
- Computes positive and negative scores using predefined dictionaries.
- Calculates readability metrics such as FOG Index and average sentence length.
- Identifies complex words and personal pronouns.
- Outputs results in a structured Excel file.

## Project Structure

```
project_root/
├── Scripts/
│   ├── main.py  # Main analysis code
│   ├── extract_text.py  # To read from the list of urls
│   ├── load_resources.py # Helper functions to load resources
├── StopWords/        # StopWords files
├── Dictionaries/     # Positive and Negative word dictionaries 
├── ExtractedTexts/       # Folder containing input text files
├── Input.xlsx # Excel file containing list of urls
├── Output_Data_Structure.xlsx # Generated Excel output
```

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd project_root
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Setup

1. Place the input text files in the `ExtractedTexts/` directory.
2. Ensure the StopWords and Dictionaries are correctly set up in the `resources/` folder.

## Usage

1. Run the script to analyze text files:
   ```bash
   python code/text_analysis.py
   ```
2. The results will be saved in the `Output_Data_Structure.xlsx` file.

## Output

The output Excel file contains the following columns:

- `URL_ID`: Identifier for the article.
- `URL`: Placeholder for the article's URL.
- `POSITIVE SCORE`: Count of positive words in the text.
- `NEGATIVE SCORE`: Count of negative words in the text.
- `POLARITY SCORE`: Difference between positive and negative scores, normalized.
- `SUBJECTIVITY SCORE`: Ratio of subjective words to total words.
- `AVG SENTENCE LENGTH`: Average number of words per sentence.
- `PERCENTAGE OF COMPLEX WORDS`: Proportion of complex words in the text.
- `FOG INDEX`: Readability metric.
- `AVG NUMBER OF WORDS PER SENTENCE`: Average words per sentence.
- `COMPLEX WORD COUNT`: Number of complex words in the text.
- `WORD COUNT`: Total number of words.
- `SYLLABLE PER WORD`: Average syllables per word.
- `PERSONAL PRONOUNS`: Count of personal pronouns.
- `AVG WORD LENGTH`: Average length of words in the text.

## Example Output

### Output:
The corresponding row in the Excel file:

| URL_ID | URL       | POSITIVE SCORE | NEGATIVE SCORE | POLARITY SCORE | SUBJECTIVITY SCORE | ... |
|--------|-----------|----------------|----------------|----------------|--------------------|-----|
| 1      | URL_1     | 2              | 0              | 1.0            | 1.0                | ... |

## Requirements

- Python 3.7+
- Required libraries:
  - `pandas`
  - `nltk`

## Notes

1. Ensure that NLTK resources like `punkt` and `stopwords` are downloaded before running the script:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```
2. The script uses custom stopwords and dictionaries loaded from the `resources/` folder.

## License

This project is licensed under the MIT License.

---

**Happy Analyzing!**
