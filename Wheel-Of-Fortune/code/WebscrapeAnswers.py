# %%
#==================#
#I DID NOT WRITE THIS CODE. I AM USING SCOTTS CODE JUST TO OBTAIN A BETTER ANSWER BANK#
#==================#
from bs4 import BeautifulSoup
import requests
import json
import numpy as np

def load_answers():

    dict = {}

    hints = ["around-the-house","before-and-after","book-title","classic-movie","classic-tv","college-life","event","family","fictional-character","fictional-place","food-and-drink","fun-and-games","headline","husband-and-wife","in-the-kitchen","landmark","living-thing","megaword","movie-quotes"]

    for y in hints:
        counter = 0
        html = requests.get("https://wheeloffortuneanswer.com/" + y + "/").text

        soup = BeautifulSoup(html, 'lxml')
        for s in soup.select('a'):
            s.extract()
        phrases = soup.find_all("td",class_ = "column-1")

        for x in range(0,50):
            phrases.pop(len(phrases) - 1)


        for x in phrases:
            if counter < 10 and True:
                key = x.get_text().strip()
                dict[key] = y
                counter += 1

    return dict

def select_answer(answerdict):
    # given the full dictionary of answers, selects an answer randomly
    keys = list(answerdict)
    numanswers = len(answerdict)
    select = np.random.randint(0,numanswers)
    answer = keys[select]
    categories = list(answerdict.values())
    category = categories[select]
    category = category.replace('-',' ')
    category = category.upper()
    print(f'Category: {category}')
    return answer



if __name__ == '__main__':
    dict = load_answers()
    answer = select_answer(dict)
    print(answer)
 
