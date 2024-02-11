import requests
from bs4 import BeautifulSoup

def icerik_bulucu(url, aranan_kelime):
  
    try:
        response = requests.get(url)
        response.raise_for_status()  
    except requests.RequestException as e:
        print(f'Hata: {e}')
        return
    
 
    soup = BeautifulSoup(response.text, 'html.parser')
    

    icerikler = soup.find_all('a', class_='makale-basligi')
    

    for icerik in icerikler:
        baslik = icerik.text.strip()
        link = icerik['href']
        if aranan_kelime.lower() in baslik.lower():
            print(f'Başlık: {baslik}, Link: {link}')

url = 'https://ornekwebsite.com/makaleler'
aranan_kelime = 'Python'
icerik_bulucu(url, aranan_kelime)
