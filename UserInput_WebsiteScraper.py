import requests, bs4


print("Finish the www. domain to scrape the page for text")
website = input('www.')
res = requests.get('http://' + website)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")
soup.prettify()

scrapeChoice = ''
while scrapeChoice != 'exit':
    print("what Html Tag would you like to scrape? \n examples of valid tags would be (div, a, h1, ul, p")
    scrapeChoice = input()
    div = soup.find_all(scrapeChoice)
    if not div:
        print('we scrapped the website and could not find any %s' % scrapeChoice)
    elif scrapeChoice != 'exit':
        print(div)
        print("\n\n you have scraped the %s tags fot website %s \n if you would like continue enter another tag or type exit"% (scrapeChoice, website))

