
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

print("Script started.")
# Load dataset (sentiment.csv should be in the same folder)
try:
    df = pd.read_csv("C:/Users/gauta/sentiment-classifier/sentiment.csv")
    print("Dataset loaded successfully.")
    print(df.head())  # Check the first few rows of the dataset
except FileNotFoundError:
    print("Error: sentiment.csv not found.")
    exit()

# Check if the dataset contains the necessary columns
if 'sentiment' not in df.columns or 'review' not in df.columns:
    print("Error: Dataset must have 'sentiment' and 'review' columns.")
    exit()

# Rename columns for easier access
df = df.rename(columns={"sentiment": "sentiment", "review": "text"})
df = df[["text", "sentiment"]].dropna()

# Optional: Use a subset for faster training (use all data for better results)
df = df.sample(5000, random_state=42)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(df["text"], df["sentiment"], test_size=0.2, random_state=42)

# Build the machine learning pipeline
model = Pipeline([
    ('vectorizer', CountVectorizer()),  # Converts text into numerical features
    ('classifier', MultinomialNB())     # Naive Bayes classifier for text classification
])

# Train the model
print("Training the model...")
model.fit(X_train, y_train)

# Test it in a loop, take input from user
print("\nSentiment Analysis Ready. Type 'q' to quit.\n")
while True:
    sentence = input("Enter a sentence to analyze: ")
    
    # Handle empty input
    if not sentence.strip():
        print("Please enter a valid sentence.")
        continue
    
    if sentence.lower() == 'q':
        print("Exiting...")
        break
    
    try:
        # Make prediction
        prediction = model.predict([sentence])
        print("Sentiment:", prediction[0])  # Display prediction (Positive/Negative)
    except Exception as e:
        print(f"Error while predicting: {e}")

