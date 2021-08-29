import requests as rq
import smtplib
from bs4 import BeautifulSoup
import time

url = "https://www.flipkart.com/denver-hamilton-prestige-caliber-combo-deodorant-spray-men/p/itm0c3aaee173a8b?pid=DEOEGYSHGZPPENTV&lid=LSTDEOEGYSHGZPPENTVGJSNPG&marketplace=FLIPKART&fm=personalisedRecommendation%2Fp2p-same&iid=R%3As%3Bp%3ADEOFCFXRQYF4JGFP%3Bpt%3Ahp%3Buid%3A5707e5d3-0894-11ec-bcdd-a79913930fc0%3B.DEOEGYSHGZPPENTV&ppt=hp&ppn=homepage&ssid=5fhie0e62o0000001630219358955&otracker=hp_reco_Recommended%2BItems_3_20.productCard.PMU_V2_DENVER%2BHamilton%252C%2BPrestige%2Band%2BCaliber%2BCombo%2BDeodorant%2BSpray%2B%2B-%2B%2BFor%2BMen_DEOEGYSHGZPPENTV_personalisedRecommendation%2Fp2p-same_2&otracker1=hp_reco_WHITELISTED_personalisedRecommendation%2Fp2p-same_Recommended%2BItems_DESKTOP_HORIZONTAL_productCard_cc_3_NA_view-all&cid=DEOEGYSHGZPPENTV"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36' }



def check_price():
    page = rq.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find("span", {'class':"B_NuCI"}).get_text()

    price= soup.find("div", {"class":"_30jeq3 _16Jk6d"}).get_text()[1:].replace(',','')
    price = float(price)

    print(price)

    if(price<1000.0):
        sendmail()


def sendmail():
        
    server= smtplib.SMTP('smtp.gmail.com', 587)

    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("choudharyaakash066@gmail.com","qkpclbtddtovndnw")

    subject = 'hello im alexa talk to me.'
    body ='wanna hang out???'
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('choudharyaakash066@gmail.com','siddhantsingh2201@gmail.com', msg)

    print("Email Send")
    server.quit()

while(True):
    check_price()
    time.sleep(60*60)    