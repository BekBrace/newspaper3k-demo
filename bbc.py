import newspaper
# create a newspaper object
bbc = newspaper.build('http://bbc.co.uk')

# Article URLs
# for article in bbc.articles:
#     print(article.url)

# Categories
for category in bbc.category_urls():
    print(category)
