# text-mining

## Project Overview:

I use IMDB as my data source. I hope to learn about the reviews on a movie that I want to watch recently called “Ticket to Paradise” to determine if I should go watch it or not. I use most frequent words, sentiment analysis, and similarity analysis on this source.

## Implementation:

1. The beginning part of the code is used to download the data from IMDB's website. I download the first 11 reviews on the IMDB into a list, and change the list to a string for easier process later.

2. The second part of the code is to get the most common words used in this data source.The first two functions are to process the file and the text.I get the stopwords data file to avoid stopwords being counted as most frequent appeared word.

3. The third part is to get the sentiment score for the data source.

4. The last part is to get the similarity between the random two reviews. I use token_set_ratio, rather than other function in fuzz library, to avoid counting extra and repeated word.I hope to see if the reviews are saying the same thing about the movie or not.

## Results:

1. I find in the most common words list, romantic and comedy are mentioned, meaning this is going to be a romantic comedy movie. Julia Roberts and George Clooney are mentioned, meaning they are the main characters and the actors probably matter a lot in the success of this movie. Good, like, better, great are in the list, meaning people generally have positive reviews on the movie.


The most common words are:
movie    21
roberts          10
clooney          9
romantic         8
julia    8
good     8
like     7
better   7
great    6
george   6
comedy   6


2. I also find in the sentiment analysis result, there are more positive words than negative words, and the compound score is very high (> 0.05), which means in general, the audience has a postive opinion towards the movie.

{'neg': 0.072, 'neu': 0.65, 'pos': 0.278, 'compound': 0.9999}

3. Lastly, I find that the similarities between first and second reviews, as well as between third and fourth reviews are not high. This indicates that people are talking about different things about this movie.

The similarity between first and second comment is:
54


## Reflection:

From what I learn from the result, I would definitely going to see this movie, cause it got good reviews and I am really into romantic and comedy movies.

From what I learn from text mining, I would use these in my future job. I am interested in marketing analysis, and these would be really useful in analyzing what people are saying on the social media, what people think of our brand, etc.
