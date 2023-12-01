# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.sentiment import SentimentIntensityAnalyzer

# nltk.download("punkt")
# nltk.download("vader_lexicon")

# text = "This is an example sentence. It showcases natural language processing."

# # Tokenization
# tokens = word_tokenize(text)
# print("Tokens:", tokens)

# # Sentiment Analysis
# sid = SentimentIntensityAnalyzer()
# sentiment_score = sid.polarity_scores(text)
# print("Sentiment Score:", sentiment_score)

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html", title="Home", content="Welcome to my Flask app!")

# if __name__ == "__main__":
#     app.run(debug=True)
