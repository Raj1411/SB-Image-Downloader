
from opcode import opname
from time import time
from tkinter import E
from urllib import response
import streamlit as st
import requests as rq
from bs4 import BeautifulSoup as bs
import re
import shutil,os
import zipfile
from io import StringIO
from django.http import HttpResponse
from urllib.request import urlopen
from io import BytesIO
import base64
from PIL import Image
import time



# @st.cache
# def load_image(image_file):
#     img=Image.open(image_file)
#     return img




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
        # print(f_u)

        
        
        for i in f_u:
            filename=i.split('/')[-1]
            f_1=filename.split('?')[0]

        # with st.spinner('Downloading {}'.format(f_1)):
            response_1=urlopen(i)
            image=response_1.read()
            # img=load_image(BytesIO(image))
            handle.writestr(f_1,image)
            # time.sleep(1)

            # for i in range(0,len(final_urls)):
            #     handle.writestr(f_1,image)
        handle.close()


        st.info("All Images has been Extracted from Website, Click on the below Download button to Download the Images")

        
        dwnld=st.download_button(data=open('sample.zip','rb'),file_name='sample.zip',label='Download')




