# 2.
titles = []
searchword = "geschichte"

for title, author, year, lang, topics in books:
    if searchword in title.lower():
        titles.append(title)
    for topic in topics:
        if searchword in topic.lower():
            titles.append(title)

print(titles)