from sikuli.Sikuli import *
from util import *
from regionDictionary import *

addImagePath("GPIITestImages.sikuli")


class Demo_Personas(util):	
		
	def Sammy_Login(self):
		try:
			type('d', KeyModifier.ALT)
			wait(2)
			type("http://localhost:8081/user/sammy/login")
			type(Key.ENTER)
			wait(5)
			assert (exists("Magnifier_Icon.png") and exists("Test.png"))
		except:
			self.captureMyScreen()
			assert False
					
	def Sammy_Logout(self):	
		try:
			type('d', KeyModifier.ALT)
			type("http://localhost:8081/user/sammy/logout")
			type(Key.ENTER)
			assert not exists("Zoom_200%.png")
		except:
			self.captureMyScreen()
			assert False
		
	   
	def Elod_Login(self):
		try:
			type('d', KeyModifier.ALT)
			type("http://localhost:8081/user/elod/login")
			type(Key.ENTER)	   
			assert (exists("Magnifier_Icon.png") and exists("Zoom_200%.png"))
		except:
			self.captureMyScreen()

			
			
	def Elod_Logout(self):	
		try:
			type('d', KeyModifier.ALT)
			type("http://localhost:8081/user/elod/logout")
			type(Key.ENTER)
			assert not (exists("Magnifier_Icon") and exists("Zoom_200%"))
		except:
			self.captureMyScreen()
			assert False
		
			
	
	def Alice_Login(self):
		try:
			wait(4)
			type('d', KeyModifier.ALT)
			type("http://localhost:8081/user/alice/login")
			type(Key.ENTER)	   
			assert exists("OnScreenKeyboard_Icon.png")
		except:
			self.captureMyScreen()
			assert False
					
	def Alice_Logout(self):	
		try:
			type('d', KeyModifier.ALT)
			type("http://localhost:8081/user/alice/logout")
			type(Key.ENTER)
			assert not (exists("OnScreenKeyboard_Icon.png") and exists("Keyboard_Img.png"))
		except:
			self.captureMyScreen()
			assert False		
			
	def Elmer_Login(self):
		try:
			type('d', KeyModifier.ALT)
			wait(2)
			type("http://localhost:8081/user/elmer/login")
			type(Key.ENTER)
			wait(5)
			assert exists("screen.png")
		except:
			self.captureMyScreen()
			assert False
		
					
	def Elmer_Logout(self):	
		try:
			click("Chrome_Browser.png")
			type('d', KeyModifier.ALT)
			type("http://localhost:8081/user/elmer/logout")
			type(Key.ENTER)
			wait(5)
			assert not exists("screen.png")
		except:
			self.captureMyScreen()
			assert False
		  	
if __name__== "__main__":
    gpii = Demo_Personas()
    gpii.runTest()
