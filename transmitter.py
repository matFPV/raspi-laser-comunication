#TRANSMISSION
#by mtroll21
#use this o the transmitter side (the one with the laser)
	
#imports
inport RPi.GPIO as io
import time
import letBin.py #import letter map

io.setmode(io.BCM)

#define
laser = 27
io.setup(laser, io.OUT)


input = raw_input("") #usr input
letters[] = input.split("") #split text to letters
loopIf = letter.lenght
while(loopIf >= 1): #loop
	letters
	io.output(laser, True) #convert letters to binaray and send data
	time.sleep(<time delay>)
