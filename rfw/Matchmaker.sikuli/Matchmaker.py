
import pdb
from sikuli.Sikuli import *
import shutil

addImagePath("Matchmaker.sikuli")
addImagePath("Demo_Personas.sikuli")
class Matchmaker():	
	def __init__(self):
		self.folder = "C:\\rfw\\results\\"
		self.imagePath = self.folder
		self.screenWidth = 1600
		self.screenHeight = 900
		self.imagePath = self.folder
		
	def UserA_Login(self):
		try:
			doubleClick("Chrome_DesktopShortcut.png")
			wait("Goto_Url.png")
			type("http://localhost:8081/user/MMQAUserA/login")
			type(Key.ENTER)	   
			r = find("Tasktray_Icon.png").right()
			click("Tasktray_Icon.png")
			assert exists("NVDA_Icon.png")
		except:
			self.captureMyScreen()
			assert False
	

	def UserA_Logout(self):
		try:
			reg = region.center()
			click("Ok_Button.png")
			type('d', KeyModifier.ALT)
			type("http://localhost:8081/user/MMQAUserA/logout")
			type(Key.ENTER)
			wait(5) 
			click("")
			r = find("Tasktray_Icon.png").right()
			click("Tasktray_Icon.png")
			assert not exists("NVDA_Icon.png")
		except:
			self.captureMyScreen()
			assert False


	
	def captureMyScreen(self):	
	        # create a new region to screenshot
		area = capture(Region(0,0,self.screenWidth,self.screenHeight))
	        # create the path to save the screenshot
		Path1 = os.path.join(self.imagePath)
	
	        # save the screenshot to the specified directory
		shutil.move(area, Path1)	
		
if __name__== "__main__":
    gpii = Matchmaker()
    gpii.runTest()		