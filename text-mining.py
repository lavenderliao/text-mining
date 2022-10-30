from imdb import Cinemagoer
import sys
from unicodedata import category

# create an instance of the Cinemagoer class
ia = Cinemagoer()

# search movie
movie = ia.search_movie("Ticket to Paradise")[0]
# print(movie.movieID)
# '14109724'

movie_reviews = ia.get_movie_reviews('14109724')
comments = []
for i in range(0,10):
    x = movie_reviews['data']['reviews'][i]['content']
    comments.append(x)
comment_text = ''.join(comments)

# word frequencies

def process_file(filename):
    """Makes a histogram that contains the words from a file.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, encoding='utf8')

    # strippables = string.punctuation + string.whitespace
    # via: https://stackoverflow.com/questions/60983836/complete-set-of-punctuation-marks-for-python-not-just-ascii

    strippables = ''.join(
        [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")]
    )

    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break

        line = line.replace('-', ' ')
        line = line.replace(
            chr(8212), ' '
        )  # Unicode 8212 is the HTML decimal entity for em dash

        for word in line.split():
            # remove punctuation and convert to lowercase
            word = word.strip(strippables)
            word = word.lower()

            # update the histogram
            hist[word] = hist.get(word, 0) + 1

    return hist


def process_text(text):
    """Makes a histogram that contains the words from a text.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    hist = {}

    # strippables = string.punctuation + string.whitespace
    # via: https://stackoverflow.com/questions/60983836/complete-set-of-punctuation-marks-for-python-not-just-ascii

    strippables = ''.join(
        [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")]
    )

    for word in text.split():
            # remove punctuation and convert to lowercase
        word = word.strip(strippables)
        word = word.lower()

            # update the histogram
        hist[word] = hist.get(word, 0) + 1

    return hist

def most_common(hist, excluding_stopwords=True):
    """Makes a list of word-freq pairs(tuples) in descending order of frequency.
    hist: map from word to frequency
    excluding_stopwords: a boolean value. If it is True, do not include any stopwords in the list.
    returns: list of (frequency, word) pairs
    """
    t = []

    stopwords = process_file('data/stopwords.txt')

    stopwords = list(stopwords.keys())
    # print(stopwords)

    for word, freq in hist.items():
        if excluding_stopwords:
            if word in stopwords:
                continue

        t.append((freq, word))

    t.sort(reverse=True)
    return t


def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.
    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[:num]:
        print(word, '\t', freq)

def main():
    hist = process_text(comment_text)
    t = most_common(hist, False)

    print('The most common words are:')
    for freq, word in t[0:20]:
        print(word, '\t', freq)
    print_most_common(hist, 20)

if __name__ == "__main__":
    main()

# sentiment analysis
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sentence = comment_text
score = SentimentIntensityAnalyzer().polarity_scores(sentence)
print('The sentiment analysis result is')
print(score)

# similarity of two comments
from thefuzz import fuzz
import random
first_comment = random.choice(comments)
second_comment = random.choice(comments)
result1 = fuzz.token_set_ratio(first_comment,second_comment)
print('The similarity between first and second comment is:')
print(result1)
