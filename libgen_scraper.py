import sys
import time
import webbrowser

from libgen_api import LibgenSearch

col_names = [
        "ID",
        "Author",
        "Title",
        "Publisher",
        "Year",
        "Pages",
        "Language",
        "Size",
        "Extension",
        "Mirror_1",
        "Mirror_2",
        "Mirror_3",
        "Mirror_4",
        "Mirror_5",
        "Edit",
    ]



# Make a search object.
search = LibgenSearch()

filters = {"Extension": "pdf", "Language": "English"}

# To search for a specific author.
# author = ' '.join(sys.argv[1:])
# books = search.search_author_filtered(f"{author}", filters, exact_match=False)

# To search for an exact book.
title = ' '.join(sys.argv[1:])
books = search.search_title_filtered(f"{title}", filters, exact_match=False)

length = len(books)
print(f"Downloading {length} books.")

links = []
for book in books:
    download_link = search.resolve_download_links(book)
    links.append(download_link["GET"])

for i in range(len(links)):
    if i % 2 == 0:
        time.sleep(10)
    webbrowser.open(links[i])


print("Done")
