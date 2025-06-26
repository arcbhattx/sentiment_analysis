import nltk.sentiment
import pandas
import nltk

#nltk.download('punkt')

data_frame = pandas.read_csv('sample_data.csv')

#print(data_frame.head())


review_sentences = data_frame['review_text'].dropna()

tokenized_review_sentences = []

sentences_polarity_scores = []

negative_sentences = []

positive_sentences = []

neutral_sentences = []


#loop through all the reviews
for sentence in review_sentences:
    #tokenized_review_sentences.append(nltk.word_tokenize(sentence))

    #get polarity scores of all sentences and stores them in a list
    sid = nltk.sentiment.SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(sentence)
    sentences_polarity_scores.append(ss)

    #classify each sentence as pos, neg or neutral
    
    if ss['compound'] < -0.2:
        negative_sentences.append(sentence)
    elif ss['compound'] > 0.2:
        positive_sentences.append(sentence)
    else:
        neutral_sentences.append(sentence)



# prints the first 5 tokenized sentences
print(review_sentences[:5]) 
print(sentences_polarity_scores[:5])

#print the amount of pos, neg and neu sentences

print('Pos: ', len(positive_sentences))
print('Neg: ', len(negative_sentences))
print('Neu: ', len(neutral_sentences))






