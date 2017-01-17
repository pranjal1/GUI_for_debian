#!/usr/bin/env python
import sys
import os
try:  
	import gi
	gi.require_version('Gtk', '3.0')
	from gi.repository import Gtk
except:  
	sys.exit(1)  	


class leeroyjenkins:

	wTree = None

	def __init__( self ):
		self.gladefile = "./data/final_design.glade" 
        	self.glade = Gtk.Builder()
        	self.glade.add_from_file(self.gladefile)
        	self.glade.connect_signals(self)
        	self.glade.get_object("window1").show_all()
		filename = "/etc/hostapd/hostapd.conf"
		exit1 = bool(False)	
		exit2 = bool(False)
		with open(filename) as openfile:    # Open file for reading of text data
			for num, line in enumerate(openfile,1):
				if "ssid=" in line and exit1 == False:
					ssid = line
                			exit1=True
				if "wpa_passphrase=" in line and exit2 == False:
					password = line
                			exit2=True
		ssid = ssid[5:]          #remove unncessary part of the string
		password = password[15:]
		ssid = ssid[:-1]          #remove unncessary part of the string
		password = password[:-1]


		self.glade.get_object("entry1").set_text(ssid)
		self.glade.get_object("entry2").set_text(password)
		self.glade.get_object("entry3").set_text("B8:27:EB:27:72:8F")

        def load_clicked(self, widget):
		filename = "/etc/hostapd/hostapd.conf"
		exit1 = bool(False)	
		exit2 = bool(False)
		with open(filename) as openfile:    # Open file for reading of text data
			for num, line in enumerate(openfile,1):
				if "ssid=" in line and exit1 == False:
					ssid = line
                			exit1=True
				if "wpa_passphrase=" in line and exit2 == False:
					password = line
                			exit2=True
		ssid = ssid[5:]          #remove unncessary part of the string
		password = password[15:]
		ssid = ssid[:-1]          #remove unncessary part of the string
		password = password[:-1]


		self.glade.get_object("entry1").set_text(ssid)
		self.glade.get_object("entry2").set_text(password)
		self.glade.get_object("entry3").set_text("B8:27:EB:27:72:8F") 
	

	def confirm_clicked(self, widget):
		os.system("sudo service hostapd stop")		
		os.system("sudo service dnsmasq stop")

		filename = "/etc/hostapd/hostapd.conf"
		exit1 = bool(False)	
		exit2 = bool(False)
		with open(filename) as openfile:    # Open file for reading of text data
			for num, line in enumerate(openfile,1):
				if "ssid=" in line and exit1 == False:
					ssid = line
                			exit1=True
				if "wpa_passphrase=" in line and exit2 == False:
					password = line
                			exit2=True
		ssid = ssid[5:]          #remove unncessary part of the string
		password = password[15:]
		

		new_ssid = self.glade.get_object("entry4").get_text()
		new_ssid = new_ssid + "\n" 
		new_password = self.glade.get_object("entry5").get_text()
		new_password = new_password + "\n"
		with open(filename, 'r') as openfile:
    			s = openfile.read()
		s = s.replace(ssid, new_ssid)
		s = s.replace(password, new_password)
		with open(filename, "w") as f:
    			f.write(s)

                new_ssid = new_ssid[:-1]          #remove unncessary part of the string
		new_password = new_password[:-1]	
		
		self.glade.get_object("entry1").set_text(new_ssid)
		self.glade.get_object("entry2").set_text(new_password)
		
		os.system("sudo service hostapd start")		
		os.system("sudo service dnsmasq start")

        def help_clicked(self, widget):
		self.gladefile = "./data/help_page.glade" 
        	self.glade = Gtk.Builder()
        	self.glade.add_from_file(self.gladefile)
        	self.glade.connect_signals(self)
        	self.abc=self.glade.get_object("window1")
		self.abc.show_all()
		self.entryForText = self.glade.get_object("textview1")
		with open('./data/help', 'r') as myfile:
    			data=myfile.read()
		self.entryForText.get_buffer().set_text(data)

		
	def quit_clicked(self, widget):
		sys.exit(0)

letsdothis = leeroyjenkins()
Gtk.main()
