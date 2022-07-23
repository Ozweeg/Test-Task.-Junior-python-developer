import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def create_list_of_animals(start_url):
    animals_number = dict()
    current_url = start_url
    user_agent = UserAgent().random

    headers = {
        "user-agent": f"{user_agent}",
        "Accept": "*/*"
    }
    while True:
        req = requests.get(current_url, headers=headers)
        src = req.text
        soup = BeautifulSoup(src, "lxml")

        if 'A' in animals_number.keys():
            animals_number.pop('A')
            animals_number.pop('H')
            animals_number = dict(sorted(animals_number.items(), key=lambda x: x[0])) # sorting by alphabet
            return animals_number

        all_li = soup.find("div", class_="mw-category mw-category-columns").find_all("li")
        for item in all_li:
            try:
                animals_number[item.text[0]] = animals_number.get(item.text[0]) + 1 #
            except TypeError:
                animals_number[item.text[0]] = 1
        last_animal = all_li[-1].text.replace(' ', '+')
        current_url = f"https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту&pagefrom={last_animal}#mw-pages"

url = u"https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"

if __name__ == '__main__':
    animals_number = create_list_of_animals(url)
    for key, value in animals_number.items():
        print(f"{key}: {value}")