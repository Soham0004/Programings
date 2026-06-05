import requests
import string
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from wordcloud import WordCloud
import nltk

# Download stopwords
nltk.download('stopwords')
from nltk.corpus import stopwords

# Step 1: Read text from URL
url = "https://www.sthda.com/sthda/RDoc/example-files/martin-luther-king-i-have-a-dream-speech.txt"
text = requests.get(url).text

# Step 2: Preprocessing
stop_words = set(stopwords.words('english'))
translator = str.maketrans('', '', string.punctuation + string.digits)

cleaned_lines = []
for line in text.splitlines():
    line = line.lower().translate(translator)
    words = [word for word in line.split() if word not in stop_words]
    cleaned_lines.append(" ".join(words))

# Step 3: Create Document-Term Matrix
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(cleaned_lines)
word_list = vectorizer.get_feature_names_out()
frequencies = X.toarray().sum(axis=0)

# Step 4: Create frequency DataFrame
freq_df = pd.DataFrame({'word': word_list, 'freq': frequencies})

# Step 5: Save term-document matrix to CSV
df_matrix = pd.DataFrame(X.toarray(), columns=word_list)
df_matrix.to_csv("TextMining.csv", index=False)

# Step 6: Word Cloud
word_freq_dict = dict(zip(word_list, frequencies))

wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='white',
    max_words=20,
    min_font_size=10,
    prefer_horizontal=0.5,
    colormap='Dark2'
).generate_from_frequencies(word_freq_dict)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Word Cloud of MLK's Speech")
plt.tight_layout()
plt.show()

# Step 7: Top 10 most frequent words bar chart
top_words = freq_df.sort_values(by='freq', ascending=False).head(10)

plt.figure(figsize=(10, 6))
plt.barh(top_words['word'], top_words['freq'], color='steelblue')
plt.xlabel('Frequency')
plt.ylabel('Words')
plt.title('Top 10 Most Frequent Words')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
