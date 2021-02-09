import requests
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

#카운트 횟수를 위한 전역변수
global tum
tum = 1 
#팔로우 카운트를 위한 전역변수
global followcount
followcount = 0

def searh():
    #searh
    search = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
    search.send_keys('#먹팔')
    time.sleep(8)
    search = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a')
    search.send_keys(Keys.ENTER)

    time.sleep(7)
    feed = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[3]/div[3]/a') 
    feed.send_keys(Keys.ENTER) 
    time.sleep(7)

def logout():
    xboutton = driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.qJPeX.fm1AK.TxciK.yiMZG > button')  
    time.sleep(8) #여기 왜 8초???
    ac = ActionChains(driver) 
    ac.move_to_element(xboutton) 
    ac.click()  
    ac.perform()
    time.sleep(5)
    profile = driver.find_element_by_css_selector('#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg > div > div:nth-child(5) > span')   
    ac = ActionChains(driver) 
    ac.move_to_element(profile)  
    ac.click() 
    ac.perform() 
    time.sleep(5)
    logout = driver.find_element_by_css_selector('#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg > div > div:nth-child(5) > div.poA5q > div.uo5MA._2ciX.tWgj8.XWrBI > div._01UL2 > div:nth-child(6) > div')
    ac = ActionChains(driver)
    ac.move_to_element(logout)
    ac.click() 
    ac.perform()

    driver.close() #드라이버 종료
    driver.quit()

def like():
    try:
        like = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button')
        likeBtnTxt = driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > div > span > svg')
        likeBtnTxt = likeBtnTxt.get_attribute('aria-label')
        if likeBtnTxt != '좋아요':
            print("이미 좋아요를 누른게시물입니다.")
            time.sleep(7)
        else:   
            like.send_keys(Keys.ENTER)  
            time.sleep(6)
    except:
        nextFeed()            

def nextFeed():
    try:
        nextFeed = driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.EfHg9 > div > div > a._65Bje.coreSpriteRightPaginationArrow')
        ac = ActionChains(driver)  #마우스이동
        ac.move_to_element(nextFeed)  #element로 이동
        ac.click()  #눌러준다.
        ac.perform() #실행해준다.
        time.sleep(7)
    except:
        print("다음 버튼을 찾을 수가 없습니다.")    

def follow():
    global tum
    global followcount
    commitlist = [
    '사진이 이뻐요!! 먹팔해요~',
    '피드가 정말 이뻐요~(୨୧ ❛ᴗ❛)✧ 먹팔해요~~',
    '구경 잘하고 갑니당~ 저도 먹스타 하는데 먹팔 어때요? ( ´●ᗜ●`*)',
    '안녕하세요~ 피드구경하다가 소통하고싶네요~ 먹팔해요~ (ง ˙ω˙)ว',
    '비주얼 최고,, Ҩ(°0˚)Ҩ 먹팔해요 !',
    '저희 먹팔해요! 피드가 정말 이쁘네요~ 자주 소통하고싶어요~',
    '피드 잘보고가요!! 우리 먹팔해요 :)',
    '와~ 사진엄청 잘찍으시네요! 완전 금손이세요! 대박! 소통하고싶어요! 먹팔해요~',
    '헉 완전 대박!! 사진을 엄청 잘찍으시네요! 피드가 이뻐요! 먹팔해요~ 선팔하구갈게요~ :)',
    '피드가 정말 이뻐요 어떤 어플쓰시는지 궁금해요! 저희 자주소통해요! 먹팔해요~ 선팔하고 갈게요~ (ง ˙ω˙)ว',
    ]
    #팔로우하기
    follow =  driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.bY2yH > button')
    print(follow.text) #팔로우 테그안에 문자 확인
    음식 사진인지 판별하는 곳
    time.sleep(3)
    img = driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > div._97aPb > div > div > div.KL4Bh > img')
    imgtext = img.get_attribute('alt')
    if '음식' in imgtext : 
    print('음식사진입니다.')
        if follow.text == '팔로우':
            followcount = followcount+1
            tum = tum+1
            print(str(followcount)+"번 째 팔로우 입니다.")
            #댓글달기
            try:
                commit = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea')
                random_list = random.choice(commitlist)
                ac = ActionChains(driver)
                ac.move_to_element(commit)
                ac.click()
                ac.pause(3)
                ac.send_keys(random_list)
                ac.pause(1)  
                ac.send_keys(Keys.ENTER)
                ac.perform()
            except:
                print('댓글권한이 없습니다.')

            time.sleep(8)
            ac = ActionChains(driver)  #마우스이동
            ac.move_to_element(follow)  #element로 이동
            ac.click()  #눌러준다.
            ac.perform() #실행해준다.
            time.sleep(7)
            nextFeed()
        else:
            tum = tum+1
            print('팔로잉 되어있습니다. ('+str(tum)+"번 째 작업입니다.)")
            nextFeed()
    else:
        print(img.get_attribute('alt'))
        nextFeed()

print(time.ctime()) #시작시간
id = ''
password = ''
url = 'https://www.instagram.com/'

driver = webdriver.Chrome('/Users/sungmin/Desktop/chromedriver')
driver.get(url)
soup = bs(driver.page_source, 'html.parser')
time.sleep(5) 

login_id = driver.find_element_by_name('username') 
login_id.send_keys(id) 
login_pw = driver.find_element_by_name('password') 
login_pw.send_keys(password) 
login_pw.send_keys(Keys.RETURN)

time.sleep(8)

#테그검색
searh()

# 1분에 3개 1시간에 180개 
while True:
    like() #좋아요함수
    follow() #팔로우함수
    if tum >= 100:
        logout() #로그아웃함수
        print(time.ctime()) #끝난시간
        break
# 이로직이면 20분에 60번 가능!!