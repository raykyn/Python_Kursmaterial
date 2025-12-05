import requests

isbn = "9783864881138"

isbn_list = [
    "9783864881138", # nestor Handbuch (Digital Preservation)
    "9783110551822", # Bibliotheken der Schweiz: Innovation durch Kooperation
    "9783039190829", # Actualité archivistique suisse (Archivwissenschaft Schweiz)
    "9783110768954", # Grundlagen der Informationswissenschaft (The Standard Work)
    "9783476054463", # Digital Humanities: Eine Einführung
    "9783110653656", # Praxishandbuch Forschungsdatenmanagement
    "9783110519594", # Informationsethik und Bibliotheksethik
    "9783825257118", # Forschen in der Linguistik (Data & Metadata context)
    "9783110525878", # Praxishandbuch IT-Grundlagen für Bibliothekare
    "9783486581720", # Information Retrieval (Stock)
    "9783110255539", # Handbuch Methoden der Bibliotheks- und Informationswissenschaft
    "9783796545986", # Handbuch der Schweizer Klosterbibliotheken
    "9783476026224", # Digital Humanities (Metzler Handbuch)
    "9783898642453", # Langzeitarchivierung (Veraltet aber oft zitiert)
    "9783598117589", # Bibliotheksmanagement (Standard)
    "9783110321456", # Bibliothekarisches Grundwissen (The "Red Book" for education)
    "9783825245566", # Grundlagen der Archivwissenschaft
    "9783110303193", # Handbuch Bibliotheksspezifische IT
    "9781610696319", # Digital Curation for Libraries (International context)
    "9783111029917"  # Praxishandbuch Bibliotheksmanagement (New Edition)
]

for isbn in isbn_list:
    url = f"https://lobid.org/resources/search?q=isbn:{isbn}&format=json"
    
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if len(data["member"]) > 0:
            book_entry = data["member"][0]

            title = book_entry.get("title", "No Title Found")

            first_author = book_entry.get("contribution", [{}])[0].get("agent", {})
            author_name = first_author.get("label", "Unknown Author")

            topics = book_entry.get("subjectslabels", "topics not found")

            print(title, author_name, topics)

        else:
            print("No entry found for this ISBN.")
    else:
        print("No entry found for this ISBN.")
