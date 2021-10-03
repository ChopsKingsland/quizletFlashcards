import requests
from bs4 import BeautifulSoup


def getquiz(URL):
    # URL = "https://quizlet.com/158478531/python-flash-cards/"
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(class_="SetPageTerms-termsList")

    all_terms = results.find_all("div", class_="SetPageTerms-term")

    extracted = []

    for pair in all_terms:
        # print(pair, end="\n"*2)
        words = pair.find_all("span", class_="TermText")

        meList = []

        meList.append(words[0].text)
        meList.append(words[1].text)

        extracted.append(meList)

        

        # for word in words:
        #     print(word.text)

        # print("\n\n")

    return extracted

# print(getquiz("https://quizlet.com/158478531/python-flash-cards/"))