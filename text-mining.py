from imdb import Cinemagoer

# create an instance of the Cinemagoer class
ia = Cinemagoer()

# search movie
movie = ia.search_movie("Ticket to Paradise")[0]
print(movie.movieID)
# '14109724'

movie_reviews = ia.get_movie_reviews('14109724')
first_comment = movie_reviews['data']['reviews'][0]['content']

# sentiment analysis
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sentence = first_comment
score = SentimentIntensityAnalyzer().polarity_scores(sentence)
print(score)

# if __name__ == "__main__":
#     main()