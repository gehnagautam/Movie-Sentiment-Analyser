# Movie Sentiment Analyser

A machine learning-based sentiment analysis project that classifies movie reviews as either positive or negative using natural language processing (NLP) techniques. The model utilizes a Naive Bayes classifier to make predictions based on text input.

## Features
- Classifies movie reviews as either **Positive** or **Negative**.
- Built using **Naive Bayes** classifier with **scikit-learn**.
- The model is trained using a dataset of movie reviews.
- Provides an interactive command-line interface to input sentences for sentiment prediction.

## Prerequisites
Make sure you have the following installed:
- Python 3.x
- pip (Python package installer)

### Python Libraries:
- `pandas`
- `scikit-learn`
- `numpy`


## How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/sentiment-classifier.git
    ```

2. Navigate to the project folder:
    ```bash
    cd sentiment-classifier
    ```

3. Create a virtual environment:
    - On Windows:
      ```bash
      python -m venv venv
      ```
    - On macOS/Linux:
      ```bash
      python3 -m venv venv
      ```

4. Activate the virtual environment:
    - On Windows:
      ```bash
      .\venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

5. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

6. Run the application:
    ```bash
    python app.py
    ```

## How to Use
After running the script, you will be prompted to enter a movie review sentence. The model will predict whether the sentiment is **Positive** or **Negative**.

- To exit the program, type `'q'` and press Enter.

## Dataset
The model is trained using a dataset of labeled movie reviews (`sentiment.csv`). Ensure the CSV file is present in the project directory.

## Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Please ensure that your code follows the existing coding style and includes appropriate tests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

