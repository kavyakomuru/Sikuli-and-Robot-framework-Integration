from sikuli.Sikuli import *
import os
import sys
myPath = os.path.dirname(getBundlePath())
if not myPath in sys.path: sys.path.append(myPath)
from util import *
from regionDictionary import *
addImagePath("GPIITestImages.sikuli")

class Resources(util):	
	
	
	def Show_Desktop(self):
		type('d', KEY_WIN)		
		
	def Start_GPII(self):
		doubleClick("Gpii_DesktopShortcut.png")
		click("Tasktray_Icon.png")
		wait(5)
		click("GPII_Tasktray_Icon.png")
		assert exists("GPII_Tasktray_Menu.png")		
		
	def Close_GPII(self):
		click("Exit_GPII_Tasktray.png")
		click("Tasktray_Icon.png")
		assert not exists("GPII_Tasktray_Icon.png")

	def Open_Browser(self):	
		type('d', KEY_WIN)
		doubleClick("Chrome_DesktopShortcut.png")
		click("Maximize_Browser.png")
		
	def Close_Browser(self):
		type('d', KEY_WIN)
		click("Chrome_Browser.png")
		click("Close_Button.png")
		
if __name__== "__main__":
    gpii = Resources()
    gpii.runTest()		