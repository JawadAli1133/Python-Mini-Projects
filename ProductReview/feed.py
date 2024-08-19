import nltk
import os

# Set NLTK data directory explicitly (optional)
nltk_data_dir = os.path.join(os.getcwd(), 'nltk_data')
nltk.data.path.append(nltk_data_dir)

# Download necessary resources
nltk.download('wordnet', download_dir=nltk_data_dir)
nltk.download('averaged_perceptron_tagger', download_dir=nltk_data_dir)
nltk.download('punkt', download_dir=nltk_data_dir)

from textblob import TextBlob

# Read feedbacks from file
with open('feedbacks', 'r', encoding='utf-8') as file:
    content = file.readlines()

# Analyze each feedback using TextBlob
for feedback in content:
    blob = TextBlob(feedback)
    feedback_score = blob.sentiment.polarity
    print(f'Feedback: {feedback}\nScore: {feedback_score}')
