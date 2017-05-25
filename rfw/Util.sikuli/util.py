from sikuli.Sikuli import *
import shutil
from regionDictionary import *

class util:
	
	def __init__(self):
		self.folder = "C:\\rfw\\results\\Screenshots"
		self.imagePath = self.folder
		self.screenWidth = 1600
		self.screenHeight = 900
		screenWidth = 1600
		screenHeight = 900
		self.reg = regionDictionary(self.screenWidth,self.screenHeight)
		
		
		
	def captureMyScreen(self):
	        # create a new region to screenshot
		area = capture(Region(0,0,self.screenWidth,self.screenHeight))
	        # create the path to save the screenshot
		Path1 = os.path.join(self.imagePath)
	
	        # save the screenshot to the specified directory
		shutil.move(area, Path1)	
