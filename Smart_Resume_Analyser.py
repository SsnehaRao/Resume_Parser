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
from Courses import ds_course, web_course, android_course, ios_course, uiux_course, resume_videos, interview_videos
import pafy
import plotly.express as px

def fetch_yt_video(link):
  video = pafy.new(link)
  return video_title

def get_table_download_link(df, filename, text):
  csv = df.to_csv(index=False)
  b64 = base64.b64encode(csv.encode()).decode()
  href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">{text}</a>'
  return href

def pdf_reader(file):
  resourse_manager = PDFResourseManager()
  fake_file_handle = io.StringIO()
  converter = TextConverter(resourse_manager, fake_file_handle, LAParams=LAParams())
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
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
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

#Create Table
  DB_table_name = 'user_data'
  table_sql = "CREATE TABLE IF NOT EXISTS" + DB_table_name + """(ID INT NOT NULL AUTO INCREMENT, Name varchar(100) NOT NULL, email_ID varchar(50) NOT NULL, resume_score varchar(8) NOT NULL, Timestamp varchar(50) NOT NULL, Page_no VARCHAR(5) NOT NULL, Predicted_Field VARCHAR(25) NOT NULL, User_level VARCHAR(30) NOT NULL, Actual_skills VARCHAR(300) NOT NULL, Recommended_skills VARCHAR(300) NOT NULL, Recommended_courses VARCHAR(600) NOT NULL, PRIMARY KEY (ID)); )"""
                         
  cursor.execute(table_sql)
  if choice == 'Normal User':
    pdf_file = st.file_uploader("Choose your Resume", type=["pdf"])
    if pdf_file is not None:
      save_image_path = './Uploaded_Resumes/' + pdf_file.name
      with open(save_image_path, "wb") as f:
        f.write(pdf_file.getbuffer())
        show_pdf(save_image_path)
        resume_data = ResumeParser(save_image_path).get_extracted_data()
        if resume_data:
          ## Get the whole resume data
          resume_text = pdf_reader(save_image_path)
          st.header("**Resume Analysis**")
          st.success("Hello " + resume_data['name'])
          st.subheader("**Your Basic info**")
          try:
             st.text('Name: ' + resume_data['name'])
             st.text('Email: ' + resume_data['email'])
             st.text('Contact: ' + resume_data['mobile_number'])
             st.text('Resume pages: ' + str(resume_data['no_of_pages']))
          except:
              pass
          cand_level = ''
          if resume_data['no_of_pages'] == 1:
            cand_level = "Fresher"
            st.markdown('''<h4 style='text-align: left; color: #d73b5c;'>You are looking Fresher.</h4>''', unsafe_allow_html=True)
          elif resume_data['no_of_pages'] == 2:
            and_level = "Intermediate"
            st.markdown('''<h4 style='text-align: left; color: #1ed760;'>You are at intermediate level!</h4>''', unsafe_allow_html=True)
          elif resume_data['no_of_pages'] >= 3:
            cand_level = "Experienced"
            st.markdown('''<h4 style='text-align: left; color: #fba171;'>You are at experience level!''', unsafe_allow_html=True)
            st.subheader("**Skills Recommendation💡**")
            keywords = st_tags(label='### Skills that you have', text='See our skills recommendation', value=resume_data['skills'], key='1')




                    
                          




      
                        

                          




                    
                          




      
                        
