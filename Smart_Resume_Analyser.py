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
from Courses import ds_course, web_course, android_course, ios_course, uiux_course, 
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


