# updated introdutory simple script at my years in college
#It uses a Naive Bayes classifier and reviews as positive or negative
#We use movie_reviews in order to build our classifier

from nltk.corpus import movie_reviews
import nltk
import random

def main():

    texts = [(list(movie_reviews.words(fileid)), category) \
    for category in movie_reviews.categories() \
    for fileid in movie_reviews.fileids(category)]
	#augments texts
    random.shuffle(texts)

    #converts to lowercase and calcultates fd
    words_ds = nltk.FreqDist(words.lower() for words in movie_reviews.words())

    #use words as features
    word_features = list(words_ds)[:3000]

    #each word from a doc in checked if it has our features
    def get_features(doc):
        doc_words = set(doc)
        features = {}
        for word in word_features:
            features['contains(%s)' % word] = (word in doc_words)
        return features

    #save features for each doc in each class
    featuresets = [(get_features(_doc), _class) for (_doc,_class) in texts]

    #splits docs between our sets
    train_set, test_set = featuresets[300:], featuresets[:300]
    print ("# training dataset: ", len(train_set))
    print ("# test dataset: ", len(test_set))

    #give train set to classifier
    classifier = nltk.NaiveBayesClassifier.train(train_set)

    #print accuracy
    print("Accuracy is: ")
    print(nltk.classify.accuracy(classifier, test_set))
	#prints some cool features
    print(classifier.show_most_informative_features(10))

if __name__ == '__main__':
    main()
