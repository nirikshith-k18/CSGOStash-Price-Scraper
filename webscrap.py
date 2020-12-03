from selenium import webdriver
from bs4 import BeautifulSoup
import csv
scondition=['FN','MW','FT','WW','BS']

nskinp=[]
stskinp=[]
sskinp=[]
url = input("Enter CSGOSTASH skin url")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get(url)
htmlfile = driver.page_source
soup = BeautifulSoup(htmlfile ,'html.parser')

for a in soup.findAll('a', attrs={'class':['btn btn-default btn-sm market-button-skin','btn btn-default btn-sm market-button-skin disabled-clickable','btn btn-default btn-sm market-button-skin disabled']}):

	if a.find('span', attrs={'class':'pull-right'}):
		price=a.find('span', attrs={'class':'pull-right'})
		if a.find('span', attrs={'class':'pull-left price-details-st'}):
			stskinp.append(price.contents)
		elif a.find('span', attrs={'class':'pull-left price-details-souv'}):
			sskinp.append(price.contents)
		else:
			nskinp.append(price.contents)
#cleaning
nskinp=[''.join(x) for x in nskinp]
stskinp=[''.join(x) for x in stskinp]
sskinp=[''.join(x) for x in sskinp]
for c,itemprice in enumerate(nskinp):
	nskinp[c]=itemprice.replace(",", "").replace("₹","")
for c,itemprice in enumerate(stskinp):
	stskinp[c]=itemprice.replace(",", "").replace("₹","")
for c,itemprice in enumerate(sskinp):
	sskinp[c]=itemprice.replace(",", "").replace("₹","")

with open('skin.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	if stskinp:
		
		writer.writerow(["Wear", "Regular","StatTrack"])
		
		for count in range(len(nskinp)):
			temp=[]
			temp.append(scondition[count])
			temp.append(nskinp[count])
			temp.append(stskinp[count])
			writer.writerow(temp)
	elif sskinp:
		writer.writerow(["Wear", "Regular","Souvenir"])
		for count in range(len(nskinp)):
			temp=[]
			temp.append(scondition[count])
			temp.append(nskinp[count])
			temp.append(sskinp[count])
			writer.writerow(temp)
	else:
		writer.writerow(["Wear", "Regular"])
		for count in range(len(nskinp)):
			temp=[]
			temp.append(scondition[count])
			temp.append(nskinp[count])
			
			writer.writerow(temp)




driver.quit()
