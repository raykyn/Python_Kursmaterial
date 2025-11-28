min_year = None
min_book = None
max_year = None
max_book = None
for title, author, year, lang, topics in books:
    if " v.u.Z." in year:
        year = year.replace(" v.u.Z.", "")
        year = -int(year)
    else:
        year = int(year)

    if min_year is None or year < min_year:
        min_year = year
        min_book = [title, author, year, lang, topics]
    if max_year is None or year > max_year:
        max_year = year
        max_book = [title, author, year, lang, topics]

print("Ältestes", min_book)
print("Neuestes", max_book)