from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

class covid19:
	def __init__(self):
		exePath = "chromedriver.exe"
		self.driver = webdriver.Chrome(executable_path = exePath)
	
	def openSite(self):
		self.driver.get('https://www.mohfw.gov.in/')
		time.sleep(2)
	
	def getData(self):
		dataButton = self.driver.find_element_by_xpath('/html/body/div/div/div/section[3]/div/div/div/h2/a')
		dataButton.click()
		time.sleep(2)
		id = []
		state = []
		total_cases = []
		cured = []
		deaths = []

		for i in range(1, 34):
			data = self.driver.find_element_by_xpath('/html/body/div/div/div/section[3]/div/div/div/div/table/tbody/tr[' + str(i) + ']').text
#			print(data.split())
			lst = data.split()
			
			id.append(int(lst[0]))
			diff = len(lst)-5
			if diff > 0:
				s = ""
				for j in range(1, diff+2):
					s += lst[j]
					if j != (diff+1):
						s += " "
				state.append(s)
			else:
				state.append(lst[1])
			
			total_cases.append(int(lst[-3]))
			cured.append(int(lst[-2]))
			deaths.append(int(lst[-1]))
			
#		print(id)
#		print(state)
#		print(total_cases)
#		print(cured)
#		print(deaths)
		
		file = "./corona-stats/src/abc.json"
		f = open(file, 'w')
		f.write('{"lstModel": [')
		f.close()
		
		for i in range(0, 33):
			f = open(file, 'a')
			f.write('{"id": ')
			f.write(str(id[i]))
			f.write(',"state": ')
			f.write('"')
			f.write(state[i])
			f.write('"')
			f.write(',"Total_Cases": ')
			f.write(str(total_cases[i]))
			f.write(',"Cured": ')
			f.write(str(cured[i]))
			f.write(',"Deaths": ')
			f.write(str(deaths[i]))
			f.write('}')
			if i < 32:
				f.write(',')
				f.close()
			else:
				f.close()
		f = open(file, 'a')
		f.write(']}')
		f.close()

bot = covid19()
bot.openSite()
print('Opened Site')
bot.getData()
#while True:
#	time.sleep(3600)
#	bot.getData()
input('ALL DONE')