import json
import re
from tqdm import tqdm
from langdetect import detect
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk


f = open('result.json')

data = json.load(f)
messages = data['messages']
parsedMessages = []
count = 0

for i in tqdm(range(len(messages))):
    string = messages[i]['text']
    if(type(string) is list):
        string = ' '.join([x for x in string if type(x) is str])
    if(('SHIB' in string.upper() or 'DOGE' in string.upper())):
        parsedMessages.append(string)

englishMessages = [x for x in tqdm(parsedMessages) if detect(x)=='en']
print(len(englishMessages))
nltk.download('vader_lexicon')
analyzer = SentimentIntensityAnalyzer()
# print(analyzer.polarity_scores('Stardoge on pancake swap is going crazy .   0xc6c025ab017aa364cc6bd0c0fdb7b916bc286a6a'))
# print(parsedMessages)