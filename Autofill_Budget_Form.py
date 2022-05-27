from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time

def sleep():
	time.sleep(0.5)


def YesApps():
	choice = random.randint(0,2)
	if choice == 0:
		inputChoice = '//*[@id="i5"]/div[3]/div'
	elif choice == 1:
		inputChoice = '//*[@id="i8"]/div[3]/div'
	else:
		inputChoice = '//*[@id="i11"]/div[3]/div'

	web.find_element_by_xpath(inputChoice).click()
	sleep()

	choice2 = random.randint(1,4)


	list = MainList.copy() #[19, 22, 25, 28, 31, 34, 37, 40, 43, 46]

	for x in range (choice2):
		chosen = random.randint(0,len(list))
		x = list[chosen]
		list.pop(chosen)
		inputChoice2 = '//*[@id="i'+str(x)+'"]'
		web.find_element_by_xpath(inputChoice2).click()
		sleep()

	next = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]'
	web.find_element_by_xpath(next).click()
	sleep()

def Submit():

	submit = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]'
	sleep()
	
	web.find_element_by_xpath(submit).click()
	sleep()
	#web.quit()


def NoApps():
	choice = random.randint(0,1)
	if choice == 0:
		inputChoice = '//*[@id="i5"]/div[3]/div'
	else:
		inputChoice = '//*[@id="i8"]/div[3]/div'

	web.find_element_by_xpath(inputChoice).click()

	next = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]'
	web.find_element_by_xpath(next).click()
	sleep()

	if choice == 0:
		Why();
	else:	
		NewBudgetingApp()

def Why():
	text = 'Not Applicable'
	inputText = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea'
	web.find_element_by_xpath(inputText).send_keys(text)

	next = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]'

	web.find_element_by_xpath(next).click()
	sleep()

	NewBudgetingApp()

def NewBudgetingApp():
	choice1 = random.randint(0,3)
	if choice1 == 0:
		inputChoice1 = '//*[@id="i5"]/div[3]/div' 
	elif choice1 == 1:
		inputChoice1 = '//*[@id="i8"]/div[3]/div'
	elif choice1 == 2:
		inputChoice1 = '//*[@id="i11"]/div[3]/div'
	else:
		inputChoice1 = '//*[@id="i14"]/div[3]/div'
	
	web.find_element_by_xpath(inputChoice1).click()
	sleep()

	choice2 = random.randint(0,1)
	if choice2 == 0:
		inputChoice2 = '//*[@id="i21"]/div[3]/div' 
	else:
		inputChoice2 = '//*[@id="i24"]/div[3]/div' 

	web.find_element_by_xpath(inputChoice2).click()
	sleep()
	
	choice3 = random.randint(0,2)
	if choice3 == 0:
		inputChoice3 = '//*[@id="i31"]/div[3]/div' 
	elif choice3 == 1:
		inputChoice3 = '//*[@id="i34"]/div[3]/div'
	else:
		inputChoice3 = '//*[@id="i37"]/div[3]/div'

	web.find_element_by_xpath(inputChoice3).click()
	sleep()
		
	choice4 = random.randint(0,1)

	if choice4 == 0:
		inputChoice4 = '//*[@id="i44"]/div[3]/div' 
	else:
		inputChoice4 = '//*[@id="i47"]/div[3]/div'

	web.find_element_by_xpath(inputChoice4).click()
	sleep()

	choice5 = random.randint(0,1)

	if choice5 == 0:
		inputChoice5 = '//*[@id="i54"]/div[3]/div' 
	else:
		inputChoice5 = '//*[@id="i57"]/div[3]/div'

	web.find_element_by_xpath(inputChoice5).click()
	sleep()

	Submit()

web = webdriver.Chrome()
MainList = [19, 22, 25, 28, 31, 34, 37, 40, 43, 46]

for x in range(3):
	web.get('https://forms.gle/gQN1UXixmmS7jqr77')

	age = random.randint(0,3)
	if age == 0:
	    inputAge = '//*[@id="i5"]/div[3]/div'
	elif age == 1:
	    inputAge = '//*[@id="i8"]/div[3]/div'
	elif age == 2:
	    inputAge = '//*[@id="i11"]/div[3]/div'
	else:
		inputAge = '//*[@id="i14"]/div[3]/div'

	difficulty = random.randint(0,1)
	if difficulty == 0:
		inputDifficulty = '//*[@id="i21"]/div[3]/div'
	else:
		inputDifficulty = '//*[@id="i24"]/div[3]/div'

	usage = 1 #random.randint(0,1)
	if usage == 0:
	    inputUsage = '//*[@id="i31"]/div[3]/div' #YES
	else:
	    inputUsage = '//*[@id="i34"]/div[3]/div' #NO

	next = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span'

	web.find_element_by_xpath(inputAge).click()
	sleep()

	web.find_element_by_xpath(inputDifficulty).click()
	sleep()

	web.find_element_by_xpath(inputUsage).click()
	sleep()

	web.find_element_by_xpath(next).click()
	sleep()

	if usage == 0:
		YesApps()	

	else:
		NoApps()
