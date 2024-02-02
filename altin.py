import requests
from bs4 import BeautifulSoup

def main(url):
	page = requests.get(url)
	soup = BeautifulSoup(page.content, "html.parser")
	res = soup.find_all("td", attrs={"class":"tdparitedeger tdpg"})
	alis = res[4]
	satis = res[5]
	print("--GRAM ALTIN--")
	print(f"alis: {alis.string}")
	print(f"satis: {satis.string}")
	print("--GRAM GUMUS--")
	print(f"alis: {res[10].string}")
	print(f"satis: {res[11].string}")
	
if __name__ == "__main__":
	main("https://www.nadirdoviz.com/fiyatekrani")
