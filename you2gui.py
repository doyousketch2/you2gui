#!/usr/bin/env python
# -*- coding: utf-8 -*-
##=========================================================
##  you2be.py                                   22 Mar 2017
##
##  simple youtube-dl gui
##
##  Eli Leigh Innis
##  Twitter :  @ Doyousketch2
##  Email :  Doyousketch2 @ yahoo.com
##
##  GNU GPLv3                 gnu.org/licenses/gpl-3.0.html
##=========================================================
##  required  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##  first, you'll need youtube-dl:
##        sudo apt-get install youtube-dl
##
##  (or) use synaptic package manager
##  (or) download from rg3.github.io/youtube-dl


##  then you'll need easygui and pyperclip:
##  (linux)
##        sudo pip install easygui pyperclip
##  (mac)
##        sudo python -m pip install easygui pyperclip
##  (win)
##        py -m pip install easygui pyperclip
##=========================================================
##  libs  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import sys                             ##  for exit command
import easygui as eg           ##  Graphical User Interface
import subprocess as sp           ##  commandline processes
import pyperclip as clip             ##  clipboard contents

##=========================================================
##  vars  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

title  = 'you2gui.py'
y2  = 'youtube-dl'

##=========================================================
##  script  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

clipboard  = clip .paste()
if not clipboard .startswith('http'):  ##  only autofill URL box if clipboard has a URL
  clipboard  = ''

##  enterbox(msg='Enter something.', title=' ', default='', strip=True, image=None, root=None)
URL  = eg .enterbox('URL?',  title,  clipboard)
if URL is None:   sys .exit()   ##  exit if Cancel pressed
if len(URL) < 1:   sys .exit()   ##  exit if no URL typed in, yet pressed OK

getvidname  = [y2,  '-e',  URL]

info  = sp .Popen(gathering,  stdout = sp .PIPE,  stderr = sp .PIPE)
vidname, viderr  = info .communicate()

if len(viderr) > 0:   print(viderr);   sys .exit()   ##  exit if there's an error

gathering  = [y2,  '-F',  URL]

info  = sp .Popen(gathering,  stdout = sp .PIPE,  stderr = sp .PIPE)
out, err  = info .communicate()

if len(err) > 0:   print(err);   sys .exit()   ##  exit if there's an error

choices  = out .split('\n')[6:-1]   ##  skip misc text and blank entries

##  choicebox(msg='Pick something.', title=' ', choices=())
choice  = eg .choicebox(vidname + '\n\nFormat?',  title,  choices)
if choice is None:   sys .exit()   ##  exit if dialog box closed

code  = choice .split(' ')[0]   ##  keep number code, discard text

download  = [y2,  '-f',  code,  URL]

##=========================================================
##  main  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

sp .call(download)

##=========================================================
##  eof  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
