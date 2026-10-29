import csv
from pathlib import Path
import requests
from bs4 import BeautifulSoup

URL = "https://quotes.toscrape.com/tag/life/"
HEADERS = {"User-Agent": "hillel-homework/1.0 (educational practice)"}


def parse_quotes(html):
    soup = BeautifulSoup(html, "html.parser")
    return [
        {"author": quote.select_one("small.author").get_text(strip=True),
         "text": quote.select_one("span.text").get_text(strip=True).strip("“”")}
        for quote in soup.select("div.quote")
    ]


def main():
    response = requests.get(URL, headers=HEADERS, timeout=10)
    response.raise_for_status()
    rows = parse_quotes(response.text)
    if not rows:
        raise ValueError("Цитат не знайдено: перевірте відповідь сайту")
    path = Path(__file__).with_name("life.csv")
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["author", "text"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Збережено {len(rows)} цитат у {path.name}")


if __name__ == "__main__":
    main()
