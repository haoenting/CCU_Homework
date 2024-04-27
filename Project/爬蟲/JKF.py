from bs4 import BeautifulSoup
import requests
import os

response = requests.get(f"https://www.jkforum.net/thread-15583993-1-1.html")
soup = BeautifulSoup(response.text, "lxml")

results = soup.find_all("img", {"inpost": "1"}, limit=120)

image_links = [result.get("file") for result in results]  # 取得圖片來源連結

for index, link in enumerate(image_links):

    img = requests.get(link)  # 下載圖片

    with open("images\\" + str(index+1) + ".jpg", "wb") as file:  # 開啟資料夾及命名圖片檔
        file.write(img.content)
