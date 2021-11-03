#! python3
# Prints the current weather for a location from the command line.
import webbrowser, sys
import requests, bs4
import re

import json
import subprocess


def main():
    res = requests.get('https://www.usgo.org/news/')

    res.raise_for_status()

    if res.status_code is not requests.codes.ok:
        print("error")

    else:
        goSiteParsed = bs4.BeautifulSoup(res.text, 'html.parser')
        htmlTitles = goSiteParsed.select('.storytitle')
        htmlDates = goSiteParsed.select('.date')

        dates = []
        for date in htmlDates:
            dates.append(date.text)

        titles = []
        links =[]
        for tag in htmlTitles:
            titles.append(tag.text)
            href = str(tag).find("href")
            linkStart = str(tag).find('"', href) + 1
            linkEnd = str(tag).find('"', linkStart) - 1

            links.append(str(tag)[linkStart:linkEnd])

        pairs = []

        for title, date, link in zip(titles, dates, links):
            pairs.append([title, date, link])

        for row in pairs:
            print(f"title: {row[0]}")
            print(f"date: {row[1]}")
            print(f"link: {row[2]}")
            print()

if __name__ == "__main__":
    main()