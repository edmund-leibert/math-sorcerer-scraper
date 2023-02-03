import sys
import os
import requests
import urllib.request
from bs4 import BeautifulSoup
import bs4

# Header information for the request
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q-0.9",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36",
    "Cache-Control": "max-age=0, no-cache, no-store",
    "Upgrade-Insecure-Requests": "1"
}

# Math sorcerer amazon lists
math_sorcerers_lair_amazon_idea_lists: list = [
    # Pre-Algebra, Algebra, and Geometry Books
    "https://www.amazon.com/shop/themathsorcerer/list/3J1W6SI6G3LD3?ref_=aip_sf_list_spv_ofs_mixed_d",
    # Epic Math Book List
    "https://www.amazon.com/shop/themathsorcerer/list/38XPHUJA75VTM?ref_=aip_sf_list_spv_ofs_mixed_d",
    # Calculus Books
    "https://www.amazon.com/shop/themathsorcerer/list/SKD9TCJQOZAI?ref_=aip_sf_list_spv_ofs_mixed_d",
    # Physics Books
    "https://www.amazon.com/shop/themathsorcerer/list/19UC24KBC1TIS?ref_=aip_sf_list_spv_ofs_mixed_d",
    # Real Analysis/Advanced Calculus Books
    "https://www.amazon.com/shop/themathsorcerer/list/PXA22AINMW0O?ref_=aip_sf_list_spv_ofs_mixed_d",
    # Graduate Level Math Books
    "https://www.amazon.com/shop/themathsorcerer/list/1KWMINJU0O3ND?ref_=aip_sf_list_spv_ofs_mixed_d",
    # Topology Books
    "https://www.amazon.com/shop/themathsorcerer/list/7JM1O2RO2BU4?ref_=aip_sf_list_spv_ofs_mixed_d",
    # Linear Algebra Books
    "https://www.amazon.com/shop/themathsorcerer/list/245Z6WZLBSCZE?ref_=aip_sf_list_spv_ofs_mixed_d",
    # Graph Theory Books
    "https://www.amazon.com/shop/themathsorcerer/list/DKUO44JFCA6F?ref_=aip_sf_list_spv_ofs_mixed_d",
    # Number Theory Books
    "https://www.amazon.com/shop/themathsorcerer/list/3TLBQZIZQ15YR?ref_=aip_sf_list_spv_ofs_mixed_d",
    # Computer Science Books
    "https://www.amazon.com/shop/themathsorcerer/list/1MUGOJJWDXHAD?ref_=aip_sf_list_spv_ofs_mixed_d",
    # Discrete Mathematics Books
    "https://www.amazon.com/shop/themathsorcerer/list/1ODR382WAHS7I?ref_=aip_sf_list_spv_ofs_mixed_d",
    # Complex Analysis Books
    "https://www.amazon.com/shop/themathsorcerer/list/ARWZFD5K2ZYN?ref_=aip_sf_list_spv_ofs_mixed_d",
    # Probability and Statistics Books
    "https://www.amazon.com/shop/themathsorcerer/list/3TOTRDJOTO9YD?ref_=aip_sf_list_spv_ofs_mixed_d",
    # Proof Writing Books
    "https://www.amazon.com/shop/themathsorcerer/list/3AGGO8TP6VT8G?ref_=aip_sf_list_spv_ofs_mixed_d",
    # Partial Diffential Equations
    "https://www.amazon.com/shop/themathsorcerer/list/1GWYD6EWNH777?ref_=aip_sf_list_spv_ofs_mixed_d",
    # Abstract Algebra Books
    "https://www.amazon.com/shop/themathsorcerer/list/2MN58TKSOXAAM?ref_=aip_sf_list_spv_ofs_mixed_d",
    # Differential Equations Books
    "https://www.amazon.com/shop/themathsorcerer/list/U3H6063C88IX?ref_=aip_sf_list_spv_ofs_mixed_d",
    # College Algebra, Precalculus, and Trigonometry Books
    "https://www.amazon.com/shop/themathsorcerer/list/M0MLY2DIS25K?ref_=aip_sf_list_spv_ofs_mixed_d",
]

# Iterate through the Math Sorcerer’s Lair curated academic lists...
if False:
    print("Requesting the following...")
    for idx, amazon_idea_list in enumerate(math_sorcerers_lair_amazon_idea_lists):
        r = requests.get(amazon_idea_list, HEADERS)
        soup = BeautifulSoup(r.text, 'html.parser')
        print(amazon_idea_list)
        filename_to_write: str = str(soup.find_all(class_="list-spv-listTitle")[0].contents[0])
        filename_to_write: str = str(filename_to_write).lower()
        filename_to_write: str = filename_to_write.replace(" ", "-")
        filename_to_write: str = filename_to_write.replace("/", "-")
        filename_to_write: str = filename_to_write.replace(",", "")
        filename_to_write: str = filename_to_write + ".html"
        print(filename_to_write)
        with open("scraped/" + str(filename_to_write), 'w', encoding="utf-8") as fileOpen:
            fileOpen.write(r.text)

# assign directory
directory = 'scraped'
 
print("iterating over files in the scraped directory...")
# iterate over files in scraped and build all_textbooks
all_textbooks = zip([],[])
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)
        with open(f, "r") as fOpen:
            soup = BeautifulSoup(fOpen, "html.parser")
            textbooks = soup.find_all(class_ = "product-title-text")
            authors = soup.find_all(class_ = "product-brand-text")
            list_items = zip(textbooks,authors)
            all_textbooks = all_textbooks.join(list_items)

# for textbook in all_textbooks:
#     print(textbook + " | " + textbook)

print("finish")
