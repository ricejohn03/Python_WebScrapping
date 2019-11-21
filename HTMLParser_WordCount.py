import bs4, requests

res = requests.get('https://www.tutorialspoint.com/')
try:
    res.raise_for_status()
except Exception as exc:
    print("there was a problem: %s '" %(exc))


soupobj = bs4.BeautifulSoup(res.text, features="html.parser")

news = soupobj.get_text()
print(news)
wordCount = {}
for word in str(news).split():
    if word in wordCount.keys():
        wordCount[word] += 1
    else:
        wordCount[word] = 1

print(wordCount)