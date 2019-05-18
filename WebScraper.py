#Web Page Image Scraping
import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from PIL import Image
weblink=input("Enter Web Page link:")
web_req=requests.get(weblink)
BS=BeautifulSoup(web_req.text,'lxml')
imgs=BS.find_all('img')
i=1
print(imgs)
for j in imgs:
    url=j['src']
    print("Image :{} & URL:{}".format(i,url))
    #print(url)
    res=requests.get(url,stream=True)
    img=Image.open(res.raw)
    plt.imshow(img)
    plt.close()
    img.save("C:/Users/DELL/Untitled Folder/Scraper_images/"+str(i)+".png")
    i+=1

