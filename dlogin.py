import os
import subprocess
import shlex
import time

from head import header
from selenium import webdriver
from pathlib import Path


def user_pass():

	directory = str(Path(__file__).parents[0])
	print(os.listdir(directory))
	if 'credentials' in os.listdir(directory):
		print('Credentials exist\n')
		password='';repeat=''
	else:
		while True:
			header()
			username = input('Credentials - email:')
			command = shlex.split('stty -echo')
			subprocess.run(command)
			password = input ('\n(echo off) Credentials - password: ')
			repeat = input ('\nRepeat - password: ')
			subprocess.run(shlex.split('stty echo'),shell=False)		
			if password == repeat:
				with open('credentials','a') as credentials:
					credentials.write(username+"\n")
					credentials.write(password)
					repeat='';password=''
				credentials.close()
				break		
			else:
				print('Does not match')
		
def login_automation(username, password):		

	browser = webdriver.Chrome()
	page = 'https://www.deezer.com/en/login'		
	browser.set_window_size(400,400); browser.get(page)
	gdpr_button = browser.find_element_by_xpath('//*[@id="gdpr-btn-accept-all"]')
	mail = browser.find_element_by_xpath('//*[@id="login_mail"]')
	passw = browser.find_element_by_xpath('//*[@id="login_password"]')
	login = browser.find_element_by_xpath('//*[@id="login_form_submit"]')	
	gdpr_button.click();time.sleep(0.4)
	mail.send_keys(username); passw.send_keys(password)
	login.click()


