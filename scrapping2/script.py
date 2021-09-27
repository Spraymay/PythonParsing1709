import requests
import nltk
import re
from collections import Counter
from nltk import pos_tag

url = 'https://gist.githubusercontent.com/nzhukov/b66c831ea88b4e5c4a044c952fb3e1ae/raw/7935e52297e2e85933e41d1fd16ed529f1e689f5/A%2520Brief%2520History%2520of%2520the%2520Web.txt'
text_all = requests.get(url).text
text = re.findall(r"[\w']+|[.,!?;]", text_all)
tokens_tag = pos_tag(text)

counts = Counter(y for _,y in tokens_tag)
tags_dict = {
"Существительные": counts['NN']+counts['NNP']+counts['NNS']+counts['NNPS'],
"Глаголы": counts['VB']+counts['VBG']+counts['VBD']+counts['VBN']+counts['VBP']+counts['VBZ'],
"Наречия": counts['RB']+counts['RBR']+counts['RBS'],
"Прилагательные": counts['JJ']+counts['JJR']+counts['JJS'],
"Предлоги": counts['IN'],
"Частиц": counts['RP'],
"Определителей": counts['DT'],
"Междометий": counts['UH'],
}
most = Counter(tags_dict).most_common(5)
print(dict(most))