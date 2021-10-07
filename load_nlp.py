import nltk
import os

if __name__ == "__main__":
    if os.getenv("NLTK_DATA") is None:
        nltk.download("averaged_perceptron_tagger")
        nltk.download("punkt")
        nltk.download("wordnet")
        nltk.download("stopwords")
    else:
        nltk.download("averaged_perceptron_tagger", download_dir='nltk_data/')
        nltk.download("punkt", download_dir='nltk_data/')
        nltk.download("wordnet", download_dir='nltk_data/')
        nltk.download("stopwords", download_dir='nltk_data/')
