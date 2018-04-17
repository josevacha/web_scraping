
#import urllib.request
import urllib.response
import json
from bs4 import BeautifulSoup


# Create a variable with the url
#url = 'https://www.lebatex.com/products/amore-allison-eden-customizable-fabric'
url = 'https://www.lebatex.com/products/complex-cubes-allison-eden-m-o-d-sample'

# Use urllib to get the contents
page = urllib.request.urlopen(url).read()


# create a soup object
soup = BeautifulSoup(page, 'html.parser')

# Product Name
product_name=(soup.h2.get_text().split('-')[0])

# SKU
sku=soup.find(class_="skus").get_text().replace("-","").strip()

# Sample Id
sample_id=soup.find(class_="skus").get_text().strip()

# Description
desc=soup.find("div",class_="short-description")
description=desc.p.get_text()

# Construction | For more innformation
construction= desc.p.next_sibling.get_text()

# Base Cloth
base=desc.p.next_sibling.next_sibling
base_cloth=base.strong.get_text().split("/")[0]

#Repeat
repeat=desc.p.next_sibling.next_sibling.next_sibling.get_text().split(":")[1]

# Image Path
img_tag=soup.find("div",class_="product-photo-container")
img_path="http:"+ img_tag.a.get('href').split("?")[0]


data={}
data.update({"URL":url,"product_name":product_name,"sku":sku,"sample_id":sample_id,"description":description,"construction":construction,"base_cloth":base_cloth,
             "repeat":repeat,"img_path":img_path
             })

print (json.dumps(data, ensure_ascii=False))
