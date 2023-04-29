from selenium import webdriver
from selenium.webdriver.common.by import By


def test_scores_service(url):
    my_driver = webdriver.Chrome()
    my_driver.get(url)
    score = my_driver.find_element(By.ID, "score")
    score = int(score.text)
    if 1 < score < 1000:
        return True
    else:
        return False

def main_function():
   url = 'http://127.0.0.1:8777'
   if test_scores_service(url):
       return 0
   else:
       return -1

main_function()
