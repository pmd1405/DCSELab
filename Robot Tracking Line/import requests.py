import requests

url = "https://tiktok-scraper7.p.rapidapi.com/"

querystring = {"url":"https://www.tiktok.com/@xinhgaitrenmang/video/7381461613380963600","hd":"1"}

headers = {
	"x-rapidapi-key": "8cf59bbcb3mshd0609f49cf33130p1ced35jsn07bfce2a4cf1",
	"x-rapidapi-host": "tiktok-scraper7.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())