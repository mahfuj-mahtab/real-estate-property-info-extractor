from bs4 import *
import requests
import pandas as pd


price=[]
address1=[]
address2=[]
bed_info=[]
bath_info=[]
area_info=[]
base_url='http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s='
for i in range(0,30,10):
    url=base_url+str(i)+'.html'
    r = requests.get(url,headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    content=r.content
    soup=BeautifulSoup(content, "html.parser")
    all_div=soup.find_all("div",{"class":"propertyRow"})

    for item in all_div:
        p=item.find("h4",{"class":"propPrice"}).text.strip()
        price.append(p)
        a=item.find_all("span",{"class":"propAddressCollapse"})
        address1.append(a[0].text.strip())
        address2.append(a[1].text.strip())
        try:
            bed=item.find("span",{"class":"infoBed"}).find("b")
            bed_info.append(bed.text)
        except:
            bed_info.append("None")
        try:
            bath=item.find("span",{"class":"infoValueFullBath"}).find("b")
            bath_info.append(bath.text)
        except:
            bath_info.append("None")
        try:
            area=item.find("span",{"class":"infoSqFt"}).find("b")
            area_info.append(area.text)
        except:
            area_info.append("None")


    df=pd.DataFrame({"address":address1, "Locality": address2,"Bed rooms":bed_info, "Bath rooms": bath_info, "Area Info": area_info,"Price": price})
    df.to_csv("output.csv")


            

