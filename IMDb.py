from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import numpy as np
import time


options = Options() 
driver = webdriver.Chrome(options=options)
driver.get('https://www.imdb.com/chart/top/?ref_=hm_nv_menu')


