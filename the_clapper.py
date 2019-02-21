print('\n')
print(''' To run this python file,
       you must download the selenium
      chromedriver, then drag and drop
        it into your  “/usr/local/bin”    ''')
print()
print()

import os
import pdb
import time
from os import system
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('/usr/local/bin/chromedriver')

driver.get('https://medium.com/m/signin?redirect=https%3A%2F%2Fmedium.com%2F&operation=login')


####### UNCOMMENT BELOW TO HAVE YOUR COMPUTER TALK ########
# print('...loading...')
# print('...')
# system('say -v Oliver Hello gang!')
# system('say -v Oliver I am Oliver')
# time.sleep(.25)
# system('say I am Kate')
# time.sleep(.25)
# system('say -v Zarvox I am Zee bot')
# time.sleep(.25)
# system('say -v Oliver and we want to Welcome you to THE Clapper!')
# time.sleep(.75)
# system('say -v Oliver What "login method" would you like to use?')
# time.sleep(.5)
# system('say -v Zarvox Facebook,')
# system('say -v Zarvox  Google,')
# system('say -v Zarvox or Twitter?')
# time.sleep(.5)
# system('say Once you have made your selection,')
# system('say Please click the appropriate link in your browser')
# system('say or, fill in your command line with one of the following terminal options:')
# time.sleep(1.5)
# system('say -v Oliver DONT TEST me TONY... MAKE YOUR SELECTION ALREADY!!!')

print('Please sign-in by using one of the following automated input functions:')
print()
print('sign_in_via_facebook(<FACEBOOK SIGN-ON HERE>, <FACEBOOK-PASSWORD HERE>, <@MEDIUM_TAG_NAME HERE>)')
print()
print('sign_in_via_google(<GOOGLE SIGN-ON HERE>, <GOOGLE-PASSWORD HERE>, <@MEDIUM_TAG_NAME HERE>)')
print()
print('sign_in_via_twitter(<TWITTER SIGN-ON HERE>, <TWITTER-PASSWORD HERE>, <@MEDIUM_TAG_NAME HERE>)')
print()
print('--- < Please input your username, password, and medium tag as strings > ---')
print()

##################################################################################################

# LOGIN FUNCTIONS HERE


medium_self_tag = []

def sign_in_via_facebook(username, password, medium_tag):
    medium_self_tag.append(medium_tag)
    facebook_button = driver.find_element_by_xpath('//button[2]')
    webdriver.ActionChains(driver).move_to_element(facebook_button).click(facebook_button).perform()
    time.sleep(2)
    user_input = driver.find_element_by_id('email')
    password_input = driver.find_element_by_id('pass')
    user_input.send_keys(username)
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)
    print("You should be logged in now")


def sign_in_via_google(username, password, medium_tag):
    medium_self_tag.append(medium_tag)
    google_button = driver.find_element_by_xpath('//button[1]')
    webdriver.ActionChains(driver).move_to_element(google_button).click(google_button).perform()
    time.sleep(1.5)
    user_input = driver.find_element_by_id('identifierId')
    user_input.send_keys(username)
    user_input.send_keys(Keys.ENTER)
    time.sleep(1.5)
    password_input = driver.find_element_by_name('password')
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)
    print("You should be logged in now")


def sign_in_via_twitter(username, password, medium_tag):
    medium_self_tag.append(medium_tag)
    twitter_button = driver.find_element_by_xpath('//button[3]')
    webdriver.ActionChains(driver).move_to_element(twitter_button).click(twitter_button).perform()
    time.sleep(2)
    user_input = driver.find_element_by_id('username_or_email')
    password_input = driver.find_element_by_id('password')
    user_input.send_keys(username)
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)
    print("You should be logged in now")


##################################################################################################

# BLOG CLAPPING FUNCTIONS HERE


link_root = 'https://medium.com/'

cohort_blog_profiles = ['@adamliscia', '@andrewsproul', '@anthonytapias', '@AudreyLorberfeld', '@augustinechang',
 '@briansrebrenik', '@cruble', '@chrispfchung', '@chrismanna', '@darshanp1295', '@pruchka',
 '@emmabernstein2018', '@erika.russi', '@evan13', '@imamun', '@jaimejcheng', '@j.jacisin', '@kahartman95',
 '@kyle.powers103', '@marcellou19', '@mubarakb', '@p.t.bailey04', '@boscacci', '@robert.hillery', '@samiramunir',
 '@scbronder12', '@thomasggrigg', '@vaeb80', '@vishalpatel2890', '@yishuen']

# test1 = '@boscacci'
# test2 = ['@boscacci', '@adamliscia']


def remove_self():
    if "@" in medium_self_tag[0]:
        pass
    else:
        medium_self_tag[0] = "@" + medium_self_tag[0]
    for tag_id in cohort_blog_profiles:
        if tag_id == medium_self_tag[0] :
            cohort_blog_profiles.remove(tag_id)



def make_it_clap():
    clap_button = driver.find_element_by_xpath('//footer/div[1]/div[3]/div/div[1]/div/div/button')
    for i in range(50):
        webdriver.ActionChains(driver).move_to_element(clap_button).click(clap_button).perform()
        print('clap, clap!')
        print(i+1)
        time.sleep(.15)
    print('Are your hands tired yet?... lolzzz')


article_xpaths = ['//*[@id="root"]/div/section/div[2]/div[1]/div[2]/div/a/div/section/h1',
                  '//*[@id="root"]/div/section/div[2]/div[1]/div[3]/div/a/div/section/h1',
                  '//*[@id="root"]/div/section/div[2]/div[1]/div[4]/div/a/div/section/h1',
                  '//*[@id="root"]/div/section/div[2]/div[1]/div[5]/div/a/div/section/h1',
                  '//*[@id="root"]/div/section/div[2]/div[1]/div[6]/div/a/div/section/h1']



def like_recent_post(medium_tag):
    for ind, value in enumerate(article_xpaths):
        xpath = value
        profile_link = link_root + medium_tag

    #>>> move browser to profile
        print('Scroll down, clicking post')
        driver.get(profile_link)
        time.sleep(1.9)
    #>>> move to the profile's posts
        driver.execute_script("window.scrollTo(0, 460)")
        time.sleep(.85)

        try:
            blog_post = driver.find_element_by_xpath(xpath)
    #>>> move to blog post
            webdriver.ActionChains(driver).move_to_element(blog_post).click(blog_post).perform()
            print('Down to the clap button!')
            time.sleep(2)
    #>>> move to bottom of blog post
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1.8)
            print('50 claps this time')
    #>>> start clapping
            make_it_clap()
            time.sleep(1.2)
            driver.back()

        except Exception as e:
            print(medium_tag,'article post #', ind + 1, "  xpath link didn't work  --->", e)
            pass



def like_recent_post_whole_class(listy):
    remove_self()
    for medium_tag in listy:
        like_recent_post(medium_tag)





################################### THE END ###################################
