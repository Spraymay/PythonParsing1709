import json
from ast import literal_eval as le
import nltk
from collections import Counter

nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('russian')
my_words = ['(', ')', ',', ':', ';', '?', '!', '-',
            '—', '=', '#', '«', 'НЛО', '»', '"', '@', '.', '2021', '+', 'как', 'Как']

with open('example.json', encoding='utf-8') as f:
    Mass = le(json.load(f))  # list of dict's

text = ''
for item in Mass:
    text += item['title'] + item['author']

splited_text = nltk.word_tokenize(text)
filtred1_text = [word for word in splited_text if word not in stopwords]
filtred2_text = [word for word in filtred1_text if word not in my_words]
parts = Counter(word for word in filtred2_text)

data = {}

i = 0
max = 10
for part in parts:
    data[part] = parts[part]
    i += 1
    if (max <= i):
        break

print(nltk.FreqDist(data).most_common(5))
