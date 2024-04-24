import nltk
from nltk.corpus import stopwords
from collections import Counter

# Download NLTK resources
nltk.download('stopwords')
nltk.download('punkt')

def read_text_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def remove_stopwords_from_text(text):
    stop_words = set(stopwords.words('english'))
    words = nltk.word_tokenize(text)
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

def calculate_letter_frequency(text):
    text = text.replace(" ", "")  # Remove spaces before counting letters
    letter_frequency = Counter(text)
    return letter_frequency

def display_letter_frequency(letter_frequency):
    for letter, frequency in letter_frequency.items():
        print(f"The letter '{letter}' appears {frequency} times.")

file_path = "/assignment2/random_paragraphs.txt"
# Read the contents of the text file
text_content = read_text_file(file_path)

# Remove stopwords from the text
filtered_text_content = remove_stopwords_from_text(text_content)

# Count letter frequency
letter_frequency_result = calculate_letter_frequency(filtered_text_content)

# Print letter frequency
display_letter_frequency(letter_frequency_result)

# Count of letters in original and filtered content
original_letter_count = sum(1 for char in text_content if char.isalpha())
filtered_letter_count = sum(1 for char in filtered_text_content if char.isalpha())

# Count total number of words before removing stopwords
total_words_before_filter = len(nltk.word_tokenize(text_content))

# Count total number of words after removing stopwords
total_words_after_filter = len(nltk.word_tokenize(filtered_text_content))

# Print additional information
print(f"Number of Characters before filtering: {original_letter_count:,}")
print(f"Number of Characters after filtering: {filtered_letter_count:,}")
print(f"Number of Words before filtering: {total_words_before_filter}")
print(f"Number of Words after filtering: {total_words_after_filter}")