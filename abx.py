
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
        
        with st.spinner('Downloading Images...'):
            handle=zipfile.ZipFile('sample.zip','w')
            response=urlopen(i)
            image=response.read()
            img=load_image(BytesIO(image))
            for i in range(0,len(final_urls)):
                handle.writestr(f_1,image)
            handle.close()
            time.sleep(0.1)

    st.info("All Images has been Extracted from Website, Click on the below Download button to Download the Images")
    st.download_button(data=open('sample.zip','rb'),file_name='sample.zip',label='Download')


else:
    pass






