# YellowPagesWebScraper
Python bot for scraping contact data from Canadian Yellow Pages into an Excel file.

Excel file contains the name, address, phone number, and website of every business from the extracted page.

&nbsp;

How to use:

* **Make sure to install the latest BeautifulSoup library before running script**

1. Enter occupation/industry of what you're looking for (E.g. "Doctor", "Dentist", "Plumber", "Mining", etc)

2. Enter the city for which you're looking for this occupation/industry (E.g. "Toronto", "Vancouver", "Montreal", etc)

3. Enter the **abbreviation** of the province/territory where the city is located.

   - Alberta = AB
   - British Columbia = BC
   - Manitoba = MB
   - New Brunswick = NB
   - Newfound Land = NL
   - Northwest Territories = NT
   - Nova Scotia = NS
   - Nunavut = NU
   - Ontario = ON
   - Prince Edward Island = PE
   - Quebec = QC
   - Saskatchewan = SL
   - Yukon Territory = YT

4. Enter the page number for which you want to extract data from (E.g. "1", "2", "5")

5. Done. The Excel file will be saved to the same location where the script is.

-----------------------------------------------------------------------------------
<p align="center">
Example Input: 
<br/>
<img src="https://github.com/ShakeebTahir/YellowPagesWebScraper/assets/32227140/93dbc1eb-942b-4f22-b357-a72e7723bd37" height="80%" width="80%"/>
<br/>
<br/>
Excel File Location: 
<br/>
<img src="https://github.com/ShakeebTahir/YellowPagesWebScraper/assets/32227140/cf07da0f-b453-40ca-8fb9-24ca8d14e0dd" height="80%" width="80%"/>
<br/>
<br/>
What Excel File Looks Like: 
<br/>
<img src="https://github.com/ShakeebTahir/YellowPagesWebScraper/assets/32227140/88e1c161-787c-47bb-b6df-fb035ff331de" height="80%" width="80%"/>
