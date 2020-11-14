#import statements
from selenium import webdriver
import random
from time import sleep

driver = webdriver.Chrome()
#referral link
links = ['https://www.pointsprizes.com/ref/21883147', 'https://www.pointsprizes.com/blg/21883147/28/top-free-mmorpg-games-of-2017', 'https://www.pointsprizes.com/blg/21883147/101/best-minecraft-resource-packs-for-2018'
,'https://www.pointsprizes.com/blg/21883147/60/10-best-minecraft-survival-mods', 'https://www.pointsprizes.com/blg/21883147/72/12-best-arma-3-mods-you-can-try-right-now']

with open('emails.txt', 'r') as f:
    emails = f.readlines()

for _ in range(len(links)):
    linksRandom = random.choice(links)
    driver.get(linksRandom)
    driver.find_element_by_xpath('//*[@id="wrapper"]/div[4]/div/div/div[1]/form/div[1]/input[1]').send_keys(random.choice(emails))
    input("Press Enter to continue...")



quit()
