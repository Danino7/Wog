from selenium import webdriver
from selenium.webdriver.common.by import By
from MainScores import url

def test_scores_service():
    my_driver = webdriver.Chrome()
    my_driver.get(url)
    score = my_driver.find_element(By.ID, "score")
    score = int(score.text)
    if 1 < score < 1000:
        return True
    else:
        return False

def main_function():
   test_score = test_scores_service()
   if test_score:
       return 0
   else:
       return -1

main_function()
