from sikuli.Sikuli import *
from util import *
from regionDictionary import *

addImagePath("GPIITestImages.sikuli")

class Installer(util):		
		
	def GPII_Install(self):
		try:
			doubleClick("Installer_Msi.png")
			click("Next_Button.png")
			exists("Acceptlicense_Button.png")
			click("Acceptlicense_Button.png")
			click("Next_Button.png")
			click("Install_Button.png")
			wait("Finish_Button.png",FOREVER)
			click("Finish_Button.png")
			assert exists("Gpii_DesktopShortcut.png")
		except:
			self.captureMyScreen()
			assert False
			
	
			
	def Change_Installation(self):
		try:
			doubleClick("Installer_Msi.png")
			click("Next_Button.png")
			click("Change_Button.png")
			click("Feature_Select_Icon.png")
			click("Feature_Unselect_Icon.png")
			click("Next_Button.png")
			click("Change_Button.png")
			wait("Finish_Button.png",FOREVER)
			click("Finish_Button.png")
			assert not (exists("RFID_DesktopShortcut.png") and exists("USB_DesktopShortcut.png"))	
		except:
			self.captureMyScreen()
			
	def Remove_Installation(self):
		try:
			doubleClick("Installer_Msi.png")
			wait(3)
			click("Next_Button.png")
			click("Remove_Button.png")
			click("Remove1_Button.png")
			wait("Finish_Button.png",FOREVER)
			click("Finish_Button.png")
			assert not (exists("Gpii_DesktopShortcut.png") and exists("RFID_DesktopShortcut.png") and exists("USB_DesktopShortcut.png"))
		except:
			self.captureMyScreen()
			assert False
			
	def Change_InstallationPath(self):
		try:
			doubleClick("Installer_Msi.png")
			click("Next_Button.png")
			click("Acceptlicense_Button.png")
			click("Next_Button.png")
			click("Browse_Button.png")
			click("SelectPath_Icon.png")
			click("SelectPath_Icon.png")
			click("CreateFolder_Icon.png")
			type("gpii")
			click("Ok_Button.png")
			assert exists("Changed_Installation_Path.png")
			click("Next_Button.png")
			click("Install_Button.png")
			wait("Finish_Button.png",FOREVER)
			click("Finish_Button.png")
		except:
			self.captureMyScreen()
		
	def Cancel_Installation(self):
		try:
			click("Next_Button.png")
			click("Install_Button.png")
			click("Cancel_Button.png")
			click("Yes_Button.png")
			click("Finish_Button.png")
			assert not (exists("Gpii_DesktopShortcut.png") and exists("RFID_DesktopShortcut.png") and exists("USB_DesktopShortcut.png"))
		except:
			self.captureMyScreen()
			assert False
			
			
	def Cancel_UnInstallation(self):
		try:
			doubleClick("Installer_Msi.png")
			click("Next_Button.png")
			click("Remove_Button.png")
			click("Remove1_Button.png")
			click("Cancel_Button.png")
			click("Yes_Button.png")
			click("Finish_Button.png")
			assert (exists("Gpii_DesktopShortcut.png") and exists("RFID_DesktopShortcut.png") and exists("USB_DesktopShortcut.png"))
		except:
			self.captureMyScreen()
			assert False


	
	def Verify_ChangedInstalledPath(self):
		try:	
			click("Cortana_Icon.png")
			type("This")
			click("PC_Icon.png")
			wait(5)
			type(Key.UP, KEY_WIN)
			doubleClick("C_Drive.png")		
			doubleClick("gpii_Folder.png")
			assert (exists("Listeners_Folder.png") and exists("Node_Icon.png") and exists("Gpii_Icons.png"))
		except:
			self.captureMyScreen()
				
	
	   
if __name__== "__main__":
    gpii = Installer()
    gpii.runTest()
