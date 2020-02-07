import requests
from bs4 import BeautifulSoup
from datetime import datetime

class ypScraper:

    def __init__(self):
        self.searchOccupation = input("Enter an occupation: ")

        self.searchCity = input("Enter a city (Capatalize first letter!): ")

        self.searchProvince = input("Enter province/territory of city(AB, BC, MB, NB, NL, NT, NS, NU, ON, PE, QC, SK, YT): ")

        self.searchPageNum = input("Enter a page number: ")

        self.url = "https://www.yellowpages.ca/search/si/" + self.searchPageNum + "/" + self.searchOccupation + "/" + self.searchCity + "+" + self.searchProvince

        self.csvFile = None

    def getPageHTML(self, url):
        userAgent = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

        page = requests.get(self.url, headers = userAgent)

        parsedHTML = BeautifulSoup(page.text, "html.parser")

        return parsedHTML

    def getListings(self, parsedHTML):
        listings = parsedHTML.findAll("div", {"class": "listing__content__wrap--flexed"})

        return listings

    def createFile(self):
        filename = self.searchOccupation + "-" + self.searchCity + "-" + self.searchPageNum + ".csv"

        self.csvFile = open(filename, "w")

        self.csvFile.write("Number, Name, Address, Phone Number, Website," + "Data Extracted On: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "," + "URL: " + self.url + "\n")

    def closeFile(self):
        self.csvFile.close()

    def addInfo(self, listings):
        num = 0
        for business in listings:

            num += 1

            businessName = business.find("div", "listing__title--wrap").h3.a.text
            businessName = businessName.replace(",", "")

            businessPhone = business.find("ul", "mlr__submenu").li.h4.text

            try:
                businessWebsite = business.find("li", "mlr__item mlr__item--website").a["href"]
                websiteRedirect = businessWebsite.find("redirect=")
                businessWebsite = businessWebsite[websiteRedirect+9:]
                businessWebsite = businessWebsite.replace("%3A", ":")
                businessWebsite = businessWebsite.replace("%2F", "/")
            except:
                businessWebsite = "No Website"

            addressParsing = business.find("span", "listing__address--full").findAll("span", {"class": "jsMapBubbleAddress"})
            
            businessAddress = ""
            for info in addressParsing:
                businessAddress += str(info.text) + " "

            businessAddress = businessAddress.replace(",", "")

            self.csvFile.write(str(num) + "," + businessName + "," + businessAddress + "," + businessPhone + "," + businessWebsite + "\n")

            print(num)
            print(businessName)
            print(businessAddress)
            print(businessPhone)
            print(businessWebsite)
            print("")

if __name__ == "__main__":
    scraper = ypScraper()
    pageHTML = scraper.getPageHTML(scraper.url)
    listings = scraper.getListings(pageHTML)
    if(listings != []):
        scraper.createFile()
        scraper.addInfo(listings)
        scraper.closeFile()
    else:
        print("No Listings")