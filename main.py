#! python3
#   Go news scraping service
#
#   Created for use by Stew Towle in CS 361 F2021
#   Code by Katie Strauss
#   Last updated 11/05/2021
#
#   This program requests data from usgo.org/news using the requests module
#   then parses the html using the beautifulSoup module and converts it to
#   output as json objects in a .json file

import requests
import bs4
import json


def main():
    rawNewsHtml = requests.get('https://www.usgo.org/news/')
    rawNewsHtml.raise_for_status()

    if rawNewsHtml.status_code is not requests.codes.ok:
        print(requests.HTTPError)

    else:
        goSiteParsed = bs4.BeautifulSoup(rawNewsHtml.text, 'html.parser')
        htmlTitles = goSiteParsed.select('.storytitle')
        htmlDates = goSiteParsed.select('.date')

        objDict = []
        for date, storyTitle in zip(htmlDates, htmlTitles):
            href = str(storyTitle).find("href")
            linkStart = str(storyTitle).find('"', href) + 1
            linkEnd = str(storyTitle).find('"', linkStart) - 1
            
            objDict.append({"Title": storyTitle.text, "Date": date.text, "Link": str(storyTitle)[linkStart:linkEnd]})

        with open("usgoNews.json", "w") as goNews:
            goNews.write(json.dumps(objDict))
        
        goNews.close()

if __name__ == "__main__":
    main()
