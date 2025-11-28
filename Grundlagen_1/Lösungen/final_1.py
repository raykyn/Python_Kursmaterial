# 1.

# ohne Listenkomprehension
counter = 0
for title, author, year, lang, topics in books:
    if " v.u.Z." in year:
        year = year.replace(" v.u.Z.", "")
        year = -int(year)
    else:
        year = int(year)
    if year < 2000:
        counter += 1

# ohne Listenkomprehension, mit regex
counter = len(books)
for title, author, year, lang, topics in books:
    if re.search("20\d\d", year) and not "v.u.Z." in year:
        counter -= 1

# mit Listenkomprehension
counter = len(books) - sum([1 for title, author, year, lang, topics in books if re.search("20\d\d", year) and not "v.u.Z." in year])

print(counter)