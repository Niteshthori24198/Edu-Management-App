
members = [
  {"name":"Alice","preferred_genre":"Romance"},
  {"name":"Bob","preferred_genre":"Sci-Fi"}
  ]
books = [
  {"title":"Love in the Rain","genre":"Romance"},
  {"title":"Historical Times","genre":"History"},
  ]
result = []
for x in members:
    # print(x["name"])
    # print(x["preferred_genre"])
    member_name = x["name"]
    member_genre = x["preferred_genre"]
    for y in books:
      # print(y["title"])
      # print(y["genre"])
      book_title = y["title"]
      book_genre = y["genre"]
      if member_genre == book_genre:
          result.append({"member":member_name,"book":book_title})
          break
      else:
          result.append({"member":member_name,"book":None})
          break 
print(result)