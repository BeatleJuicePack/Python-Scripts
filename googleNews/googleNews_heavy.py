import bs4 as bs
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import re
import random
import time
import nltk
import urllib.request

# New link: https://news.google.com/rss/search?q={query}
# geolocation: https://news.google.com/news/rss/headlines/section/geo/{location}
# geolocation: .../geo/DenverCo
# custom topic: *ID = ;sladfkjsd;lkfjsalkfj..... https://news.google.com/rss/topics/{id}?hl={lang}
# major topic: https://news.google.com/news/rss/headlines/section/topic/{topic}
# major topics: WORLD NATION BUSINESS TECHNOLOGY ENTERTAINMENT SPORTS SCIENCE HEALTH

news_url="https://news.google.com/news/rss" # top news
#*unsupported* geo_url="https://news.google.com/news/rss/headlines/section/geo/"
# major_geo = [[DenverCo], [LA], [Korea], [Mexico], [etc...]]

# topics_list= world, us, business, technology, entertainment, sports, science, health
# local =  'CAAqEQgKIgtDQklTQWdnR0tBQVAB'

topics_url= "https://news.google.com/news/rss/topic/%s"
topics_list=['CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB', 'CAAqIggKIhxDQkFTRHdvSkwyMHZNRGxqTjNjd0VnSmxiaWdBUAE', 'CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pWVXlnQVAB', 'CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pWVXlnQVAB', 'CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtVnVHZ0pWVXlnQVAB', 'CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pWVXlnQVAB', 'CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp0Y1RjU0FtVnVHZ0pWVXlnQVAB', 'CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtVnVLQUFQAQ']
for x in topics_list:
#    print(topics_url + x)
  Client=urlopen(topics_url % (x))
  xml_page=Client.read()
  Client.close()

  soup_page=soup(xml_page,"xml")
  news_list=soup_page.findAll("item")
# Print news title, url and publish date
  for news in news_list:
    print(news.title.text)
  #print(news.link.text)
  # Read the text file line by line and search for term

  # Delay will prevent abuse
    delay = round(random.uniform(3.14, 10), 2)
    time.sleep(delay)

    newslink = (news.link.text)

    scraped_data = urllib.request.urlopen(newslink)
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
    article = news.title.text + ": " + summary + "\n" + news.pubDate.text + ": " + news.link.text + "\n" + "\n"
    print(summary)
    with open('googleNews.txt', 'a') as file: # 'wa' is write append mode
              file.write(article)

  #print(news.pubDate.text)
  #print("-"*60)
    print("\n")



# newslist =[[ news_url], [topics_url])
# for x in newslist:
#     print(x)
Client=urlopen(news_url)
xml_page=Client.read()
Client.close()

soup_page=soup(xml_page,"xml")
news_list=soup_page.findAll("item")
# Print news title, url and publish date
for news in news_list:
  print(news.title.text)
  #print(news.link.text)
  # Read the text file line by line and search for term

  # Delay will prevent abuse
  delay = round(random.uniform(3.14, 10), 2)
  time.sleep(delay)

  newslink = (news.link.text)

  scraped_data = urllib.request.urlopen(newslink)
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

  maximum_frequncy = max(word_frequencies.values())

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
  article = news.title.text + ": " + summary + "\n" + news.pubDate.text + ": " + news.link.text + "\n" + "\n"
  print(summary)
  with open('googleNews.txt', 'a') as file: # 'wa' is write append mode
            file.write(article)

  #print(news.pubDate.text)
  #print("-"*60)
  print("\n")
