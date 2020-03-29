#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 22:27:23 2020

@author: rashi
"""

# Program To Read video 
# and Extract Frames 
import cv2 

# Function to extract frames 
def FrameCapture(path): 
	
	# Path to video file 
	vidObj = cv2.VideoCapture(path) 

	# Used as counter variable 
	count = 0

	# checks whether frames were extracted 
	success = 1

	while success: 

		# vidObj object calls read 
		# function extract frames 
		success, image = vidObj.read() 

		# Saves the frames with frame-count 
		cv2.imwrite("/home/rashi/Downloads/video-audio/v-frames/frame%d.jpg" % count, image) 

		count += 1

# Driver Code 
if __name__ == '__main__': 

	# Calling the function 
	FrameCapture("/home/rashi/Downloads/video-audio/Bhaiya_Book.mp4") 
