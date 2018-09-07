#!/usr/bin/env python3

from tkinter import *
import os
from datetime import datetime

root = Tk()
root.wm_title("Raspistill GUI ")

PATH = str(os.path.abspath(__file__))
PATH = PATH[:PATH.rfind('/')]		# remove file.py ending
USB = PATH +'/USBstick'


#  Cam Version :   Version 2.x (IMX219)
#      std img :  3280 x 2464	
#		  max  :  15 fps / A.K.A. 66 ms

# std mode must be 2 / 3
# 	-md 6 	1280 x 720
#	-md 7 	640  x 480
#    reduced resolution seems to cut out....
cam_mode = " -md 2"

# Wide angle cam : 
# 2592 × 1944 
# 1/3 =  864 x 648

# my 7"" LCD
# 1024 x 600

#flip = " -hf -vf"
flip = ""
#preview = " -p '5,5, 960,540' "
preview = " -p '5,5, 800,600' "
noPre = " -n "

# * Functions

def full_datetime():
	dtt = datetime.now()
	stamp = "%02d" % (dtt.year) 
	stamp += "/%02d" % (dtt.month) 
	stamp += "/%02d" % (dtt.day)
	stamp += "_%02d" % (dtt.hour)
	stamp += ":%02d" % (dtt.minute)
	stamp += ":%02d" % (dtt.second)
	return stamp

def TL_stamp():
	dtt = datetime.now()
	stamp = "TL"
	stamp += "_%01d" % (dtt.hour)
	stamp += "_%02d" % (dtt.minute)
	stamp += "_%02d" % (dtt.second)
	return stamp

def ID_stamp():
	dtt = datetime.now()
	stamp = "TL"
	#stamp += "_%04d" % (dtt.hour*dtt.minute+dtt.second)
	stamp += "_%02d" % (dtt.hour)
	stamp += "%02d" % (dtt.minute)
	return stamp

def cam_preview():
	os.system( "raspistill" +flip +preview)

def cam_snap():
	global cnsl_txt, USB
	FLNM = USB +"/" +TL_stamp() +".jpg"
	cnsl_txt.set( "raspistill " +cam_mode +flip + noPre  +" -o " +FLNM )	
	os.system( "raspistill " +cam_mode +flip +noPre  +" -o " +FLNM )	

def cam_selfie():
	global cnsl_txt, USB
	FLNM = USB +"/" +TL_stamp() +".jpg"
	cnsl_txt.set( "raspistill " +cam_mode +flip + preview  +" -o " +FLNM )	
	os.system( "raspistill " +cam_mode +flip + preview  +" -o " +FLNM )	
	
def tl_minute():
	global cnsl_txt, USB
	# raspistill -t 30000 -tl 2000 -o image%04d.jpg
	# %04 = framecount		-t total time : 30s		-tl img interval : 2 s
	period = 60		# seconds
	intvl  = 400	# milli seconds
	FLPTH = USB +"/" +ID_stamp() 
	os.mkdir(FLPTH)
	cnsl_txt.set( "raspistill " +cam_mode +flip + preview +" -t " +str(period*1000) +" -tl " +str(intvl) + " -o " +FLPTH +"/%03d.jpg" )	
	os.system(    "raspistill " +cam_mode +flip + preview +" -t " +str(period*1000) +" -tl " +str(intvl) + " -o " +FLPTH +"/%03d.jpg" )	

def tl_city():
	global cnsl_txt, USB
	period = 120		# seconds
	intvl  = 200	# milli seconds
	FLPTH = USB +"/" +ID_stamp() 
	os.mkdir(FLPTH)
	cnsl_txt.set( "raspistill " +cam_mode +flip + preview +" -t " +str(period*1000) +" -tl " +str(intvl) + " -o " +FLPTH +"/%03d.jpg" )	
	os.system(    "raspistill " +cam_mode +flip + preview +" -t " +str(period*1000) +" -tl " +str(intvl) + " -o " +FLPTH +"/%03d.jpg" )	



#		**		GUI
rw = 0

sticker = Label(root, text="Path:\t" +PATH )
sticker.grid(row=rw, column=0, columnspan=3)

rw+=1
sticker = Label(root, text="pics to :\t" +USB )
sticker.grid(row=rw, column=0, columnspan=3 )

rw+=1
sticker = Label(root, text="timestamp :\t" +full_datetime() )
sticker.grid(row=rw, column=0, columnspan=3 )

rw+=1
preview_b = Button(root, text="Preview", command=cam_preview )
preview_b.grid(row=rw, column=2)  #preview_b.pack()
preview_l = Label(root, text=" to setup shot use : ")
preview_l.grid(row=rw, column=0)  # preview_l.pack()

rw+=1
snap_b = Button(root,text="Snap", command=cam_snap )
snap_b.grid(row=rw, column=0)
snap_l = Label(root, text="  to take a picture.")
snap_l.grid(row=rw, column=1)

rw+=1
selfie_b = Button(root,text="Selfie", command=cam_selfie )
selfie_b.grid(row=rw, column=0)
selfie_l = Label(root, text="   just because.")
selfie_l.grid(row=rw, column=1)

rw+=1
TL1_b = Button(root,text="TL_1", command=tl_minute )
TL1_b.grid(row=rw, column=2)
TL1_l = Label(root, text=" test Timelapse ")
TL1_l.grid(row=rw, column=0)

rw+=1
TL2_b = Button(root,text="TL_2", command=tl_city )
TL2_b.grid(row=rw, column=2)
TL2_l = Label(root, text=" City Timelapse 1 min ")
TL2_l.grid(row=rw, column=0)


# **  Console
rw+=1
cnsl_txt = StringVar()
console = Label(root, textvariable=cnsl_txt)
console.grid(row=rw, column=0, columnspan=3)

rw+=1
rw+=1
exit_b = Button(root, text="Exit", command=root.destroy )
exit_b.grid(row=rw, column=0, columnspan=2)

root.mainloop()

