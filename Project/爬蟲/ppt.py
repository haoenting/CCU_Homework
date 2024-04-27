import requests
import os
import bs4
def saveImage(postUrl):  
    request = requests.get(postUrl) 
    data = bs4.BeautifulSoup(request.text, "html.parser")  
    imageData = data.find_all('img')                
    path = r"E:/"                    
    if (os.path.exists(path) == False):     
        os.makedirs(path)               
    imgList = []                  
    lenth = len(imageData)     
    for x in range(lenth):          
        imgList.insert(x,imageData[x].attrs["src"])   
    for i in range(lenth):                      
        getImage = requests.get(imgList[i])       
        image = getImage.content                 
        imageSave = open(path+"\img"+str(i)+".png","wb")      
        imageSave.write(image)                            
        imageSave.close()                    
postUrl = ""    
saveImage(postUrl)                       