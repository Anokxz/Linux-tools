import os
import subprocess
import time




def tool_check():
	tools={"Zphisher":"https://github.com/htr-tech/zphisher.git","TBomb":"https://github.com/TheSpeedX/TBomb.git","sherlock":"https://github.com/sherlock-project/sherlock.git"}
	for i in tools:
		if os.path.isdir(i):
			pass
		else:
			print(f"{i} downloading from github ... \n\n please wait \n") 
			subprocess.run(['sudo', 'git', 'clone',tools[i]],shell=False)
			subprocess.run(['clear'])

def tool_name():
	print("""
	
███████████████████████████████████████████████████████████▀████████████████████████████████████
█─▄─▄─█─▄▄─█─▄▄─█▄─▄█████▄─▄█▄─▀█▄─▄█─▄─▄─█▄─▄▄─█▄─▄▄▀█─▄▄▄▄█▄─▄▄▀██▀▄─██─▄─▄─█▄─▄█─▄▄─█▄─▀█▄─▄█
███─███─██─█─██─██─██▀████─███─█▄▀─████─████─▄█▀██─▄─▄█─██▄─██─▄─▄██─▀─████─████─██─██─██─█▄▀─██
▀▀▄▄▄▀▀▄▄▄▄▀▄▄▄▄▀▄▄▄▄▄▀▀▀▄▄▄▀▄▄▄▀▀▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▀▄▄▄▄▀▄▄▄▀▀▄▄▀




""")
def clear():
	#To Clear the terminal
	subprocess.run(['clear'])


def main():
	tool_name()
	print('''AVAIABLE TOOLS:

	1.SHERLOCK 
	2.ZPHISHER
	3.TBOMB\n\n''')
	
	choice = int(input("Enter your choice (1,2,3,4) : "))
	
	
	if choice == 1 :
		#Running sherlock
		clear()
		print('''
		
▒█▀▀▀█ ▒█░▒█ ▒█▀▀▀ ▒█▀▀█ ▒█░░░ ▒█▀▀▀█ ▒█▀▀█ ▒█░▄▀ 
░▀▀▀▄▄ ▒█▀▀█ ▒█▀▀▀ ▒█▄▄▀ ▒█░░░ ▒█░░▒█ ▒█░░░ ▒█▀▄░ 
▒█▄▄▄█ ▒█░▒█ ▒█▄▄▄ ▒█░▒█ ▒█▄▄█ ▒█▄▄▄█ ▒█▄▄█ ▒█░▒█

''')
		username = input("Enter the username you want to search : ")
		os.chdir('sherlock')
		print(f"Started scaning for the user {username} : ")
		subprocess.run(['sudo','python3','sherlock',username])
		os.chdir('..')
	elif choice == 2:
		#running Zphisher
		os.chdir('zphisher')
		subprocess.run(['sudo','bash','zphisher.sh',])
		os.chdir('..')
	elif choice == 3 :
		#running Tbomb
		os.chdir('TBomb')
		subprocess.run(['python3','bomber.py'])
		os.chdir('..')
	else :
		print("Wrong Input Tryagain ")
		clear()
		main()
	#clear()
	#tool_name()
	choice = input("Do you want to continue (Yes --> Y or something else for a NO ): ")
	if choice == 'y' or choice == 'Y' :
		clear()
		main()
	else:
		print("Exiting The Program in 3seconds")
def thankyou():
	print('''

█████████████████████████████████████████████████████████████████████████████████████████████████████▀█
█─▄─▄─█─█─██▀▄─██▄─▀█▄─▄█▄─█─▄███▄─█─▄█─▄▄─█▄─██─▄███▄─▄▄─█─▄▄─█▄─▄▄▀███▄─██─▄█─▄▄▄▄█▄─▄█▄─▀█▄─▄█─▄▄▄▄█
███─███─▄─██─▀─███─█▄▀─███─▄▀█████▄─▄██─██─██─██─█████─▄███─██─██─▄─▄████─██─██▄▄▄▄─██─███─█▄▀─██─██▄─█
▀▀▄▄▄▀▀▄▀▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▀▀▀▄▄▄▀▀▄▄▄▄▀▀▄▄▄▄▀▀▀▀▄▄▄▀▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀
''')
	exit()
def device_driver():
	tool_check()
	main()
	thankyou()
device_driver()
