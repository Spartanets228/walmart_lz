from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import csv
import time


options = Options() 
driver = webdriver.Chrome(options=options)
driver.get('https://www.imdb.com/chart/top/?ref_=hm_nv_menu')

time.sleep(6)

start = time.time()
movies = driver.find_elements(By.XPATH, '//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li//h3')
movies_names = []  
for movie in movies:
    movies_names.append(movie.text)
end = time.time()
movies_time = end - start


start = time.time()
movie_year_creating = driver.find_elements(By.XPATH, '//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li')
years = []
for i in movie_year_creating:
    year = i.find_element(By.XPATH, './/div[2]/div[2]/span[1]').text
    years.append(year)
end = time.time()
years_time = end - start


start = time.time()
movie_time_duration = driver.find_elements(By.XPATH, '//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li')
duration_list = []
for i in movie_time_duration:
    duration = i.find_element(By.XPATH, './/div[2]/div[2]/span[2]').text
    duration_list.append(duration)
end = time.time()
duration_time = end - start


start = time.time()
movie_items = driver.find_elements(By.XPATH, '//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li')
age_ratings = []
for i in movie_items:
    try:
        age = i.find_element(By.XPATH, './/div[2]/div[2]/span[3]').text
        age_ratings.append(age)
    except:
        age_ratings.append("Пока не сообщили")  
end = time.time()
raitings_time = end - start


with open('top_250_movies.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название фильма', 'Год выпуска', 'Продолжительность', 'Возрастное ограничение'])
    for row in zip(movies_names, years, duration_list, age_ratings):
        writer.writerow(row)

with open('time_of_work', 'w', newline='', encoding='utf-8') as file2:
    writer2 = csv.writer(file2)
    writer2.writerow(['Функция', 'Время выполнения (сек)'])
    writer2.writerow(['Сбор названий', movies_time])
    writer2.writerow(['Сбор годов выпуска', years_time])
    writer2.writerow(['Сбор продолжительности', duration_time])
    writer2.writerow(['Сбор возрастных ограничений', raitings_time])


driver.quit() 