import streamlit as st
import pandas as pd
import base64, random
import time, datetime
from pyresparser import ResumeParser
from pdfminer3.layout import LAParams, LTTextbox
from pdfminer3.pdgpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import TextConverter
import io, random
from streamlit_tags import st_tags
from PIL import images
import pymysql
#from Courses import ds_course, web_course, android_course, ios_course, uiux_course, 
import pafy
import plotly.express as px

def fetch_yt_video(link):
  video = pafy.new(link)
  return video_title

def get_table_download_link(df, filename, text):
  csv = df.to_csv(index=False)
  b64 = base64.b64encode(csv.encode()).decode()
  href = 
  return href

def pdf_reader(file):
  resourse_manager = PDFResourseManager()
  fake_file_handle = io.StringIO()
  #converter = TextConverter(resourse_manager, fake_file_handle, LAParams=LAP)
  page_interpreter =  PDFPageInterpreter(resourse_manager, converter)
  with open(file, 'rb') as fh:
    for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
      page_interpreter.process_page(page)
      print(page)
    text = fake_file_handle.get_value()

  converter.close()
  fake_file_handle.close()
  return text

def show_pdf(file_path):
  with open(file_path, 'rb') as f:
    base64_pdf = bas64.bf64encode(f.read()).decode('utf-8')
    #pdf_display= 
    st.markdown(pdf_display, unsafe_allow_html=True)

def course_recommender(course_list):
  st.subheader("**Courses & Certificates Recommendations**")
  c = 0
  rec_course = []
  no_of_reco =  st.slider('Choose number of Course Recommendations:', 1, 10, 14)
  random_shuffle(cousrse_list)
  for c_name, c_link in courselist:
    c += 1
    st.markdown(f"({c}) [{c_name}]({c_link})")
    rec_course.append(c_name)
    if c == no_of_reco:
      break

return rec_course

connection = pymysql.connect(host='localhost', user='root', password='', db='sra')
cursor = connection.cursor()

def insert_date(name, email, rec_score, timestamp
                          




                    
                          




      
                        
