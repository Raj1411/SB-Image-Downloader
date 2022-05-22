
import streamlit as st
import requests as rq
from bs4 import BeautifulSoup as bs
import re
import shutil,os
import zipfile
from urllib.request import urlopen
from PIL import Image
from io import BytesIO
import time

@st.cache
def load_image(image_file):
    img=Image.open(image_file)
    return img



st.set_page_config(page_title="SB Image Downloader", page_icon="📚")
st.title("SB Image Downloader")
st.markdown("---")
final_urls=[]

url_1=st.text_input("Enter the URL of the product you want to download: ")

handle=zipfile.ZipFile('sample.zip','w')

if url_1=="":
    pass
else:
    ac=st.button("Generate Images")
    if ac:


        r=rq.get(url_1)
        soup=bs(r.text,'html.parser')

        a_tags=soup.find_all('a',href=re.compile('//cdn.shopify.com/s/files/1'))

        for i in a_tags:
            aa=i.get('href')
            final_urls.append('https:'+aa)

        f_u=final_urls
        
        for i in f_u:
            filename=i.split('/')[-1]
            f_1=filename.split('?')[0]

        with st.spinner('Downloading {}'.format(f_1)):
            response_1=urlopen(i)
            image=response_1.read()
            # img=load_image(BytesIO(image))
            handle.writestr(f_1,image)
            time.sleep(1)
        handle.close()


        st.info("All Images has been Extracted from Website, Click on the below Download button to Download the Images")

        
        dwnld=st.download_button(data=open('sample.zip','rb'),file_name='sample.zip',label='Download')
