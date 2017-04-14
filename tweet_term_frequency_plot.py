import sys
import json
import string
from collections import Counter


import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer


def process(text, tokenizer, stopwords):
    """Process the text of a tweet:
        - Lowercase
        - Tokenize
        - Stopword removal
        - Digits removal
    """
    text = text.lower()
    tokens = tokenizer.tokenize(text)
    return [tok for tok in tokens if tok not in stopwords and not tok.isdigit()]


if __name__ == '__main__':
    # Preparation to break down tweet words
    tweet_tokenizer = TweetTokenizer()
    stopword_list = (
        stopwords.words('english') +
        list(string.punctuation) +
        ['rt', 'via']
    )

    # Determine the 30 most common words
    counter = Counter()
    with open(sys.argv[1], 'r') as f:
        for line in f:
            tweet = json.loads(line)
            tokens = process(
                tweet.get('text', ''), tweet_tokenizer, stopword_list
            )
            counter.update(tokens)

    most_common = counter.most_common(30)

    # Plotting
    x = range(len(most_common))
    y = [count for tag, count in most_common]

    plt.bar(x, y)
    plt.title("Term Frequencies")
    plt.ylabel("Frequency")

    plt.savefig('term_distribution.png')
