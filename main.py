'Newspaper Module to scrap news'
from newspaper import Article
url = 'https://www.latimes.com/world-nation/story/2020-09-20/coronavirus-aerosol-airborne-spread'

my_article = Article(url, language="en")
my_article.download()
# print(my_article.html)
my_article.parse()
# Extract the title
print('Title:', my_article.title)
# Extract the authors
print('Author: ', my_article.authors)
# Publishing date
print('Publishing date: ', my_article.publish_date)
# NLP on the article
my_article.nlp()
# Extract summary
print('Summary: ', my_article.summary)
# Extract keywords
print('Keywords: ', my_article.keywords)
