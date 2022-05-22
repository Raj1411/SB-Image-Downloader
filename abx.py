
import streamlit as st
import requests as rq
from bs4 import BeautifulSoup as bs
import re
import shutil,os
from zipfile import ZipFile


st.set_page_config(page_title="SB Image Downloader", page_icon="📚")
st.title("SB Image Downloader")
st.markdown("---")
final_urls=[]

url_1=st.text_input("Enter the URL of the product you want to download: ")

if url_1:

    r=rq.get(url_1)
    soup=bs(r.text,'html.parser')

    a_tags=soup.find_all('a',href=re.compile('//cdn.shopify.com/s/files/1'))

    for i in a_tags:
        aa=i.get('href')
        final_urls.append('https:'+aa)

    f_u=final_urls
    # print(f_u)

    for i in f_u:
        filename=i.split('/')[-1]
        f_1=filename.split('?')[0]
        # print(f_1)

        r1 = rq.get(i, stream = True)
        if r1.status_code == 200:
            r1.raw.decode_content = True
        with ZipFile('download','w') as f:
            f.writestr(f_1,r1.raw.read())

        with ZipFile('download', 'r') as zipObj:
            zipObj.extractall()
    st.success("All Images has been Downloaded Successfully")

else:
    pass






