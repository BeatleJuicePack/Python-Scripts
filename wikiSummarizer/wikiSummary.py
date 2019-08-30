
# ** Based on the article: "https://stackabuse.com/text-summarization-with-nltk-in-python/" **

# pip install beautifulsoup4 
# pip install lxml

# The following will scrape data from the given URL

import bs4 as bs
import urllib.request
import re
import random
import time
import nltk
# nltk.download('punkt')
# nltk.download('stopwords')

# Read the text file line by line and search for term

wikiSearch = "./wikiSearch.txt"
with open(wikiSearch) as ws:
    line = ws.readline()
    while line:
        URL = ("https://en.wikipedia.org/wiki/%s" % (line))
        try:
            scraped_data = urllib.request.urlopen(URL)

            article = scraped_data.read()

            parsed_article = bs.BeautifulSoup(article,'lxml')

            paragraphs = parsed_article.find_all('p')

            article_text = ""

            for p in paragraphs:
                article_text += p.text

# Preprocessing will remove any unwanted text and characters from the article

# Removing Square Brackets and Extra Spaces
            article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
            article_text = re.sub(r'\s+', ' ', article_text)

# Removing special characters and digits
            formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
            formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

# Converts text to sentences
            sentence_list = nltk.sent_tokenize(article_text)

# Finds the frequency of occurence of each word and applies a weight
            stopwords = nltk.corpus.stopwords.words('english')

            word_frequencies = {}
            for word in nltk.word_tokenize(formatted_article_text):
                if word not in stopwords:
                    if word not in word_frequencies.keys():
                        word_frequencies[word] = 1
                    else:
                        word_frequencies[word] += 1

# Finds the weighted frequency and divides by the number of occurances

            maximum_frequncy = max(word_frequencies.values(), default=0)

            for word in word_frequencies.keys():
                word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

# Sentences are scored

            sentence_scores = {}
            for sent in sentence_list:
                for word in nltk.word_tokenize(sent.lower()):
                    if word in word_frequencies.keys():
# Only sentences less than 30 words are used
            #word_count = 30
                        if len(sent.split(' ')) < 30:
                            if sent not in sentence_scores.keys():
                                sentence_scores[sent] = word_frequencies[word]
                            else:
                                sentence_scores[sent] += word_frequencies[word]

# Finds the top 7 sentences and prints them based on their scores
            import heapq
            summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

            summary = ' '.join(summary_sentences)
            txtSum = line.strip() + ": " + summary + "\n"
            print(txtSum) # line.strip() deletes hidden characters
        
    #    with open('wikiSummary.txt', 'a') as file: # 'r' is read mode
    #        contents = file.readline(line)
    #        search_word = line.strip() + ": "
    #        if search_word in contents:
    #            print("Word has been previously documented and will be skipped.")
    #            continue
    #        else:
            with open('wikiSummary.txt', 'a') as file: # 'wa' is write append mode
                file.write(txtSum)

# Delay will prevent abuse
            delay = round(random.uniform(20, 35), 2)
            time.sleep(delay)
        
            line = ws.readline()
            continue

        except:
            continue

print("List concluded; program terminating...")
