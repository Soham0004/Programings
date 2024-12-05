text = input("Enter some text: ")
text = text.lower()
article_counts = {
   "a": text.count(" a "),
   "an": text.count(" an "),
   "the": text.count(" the ")
}
total_articles = sum(article_counts.values())
print(f"Total number of articles: {total_articles}")
for article, count in article_counts.items():
   print(f"{article}: {count}")
