import sys
import os
import getpass
import datetime
from shutil import copytree

parent_dir = 'C:\\Users\\' + getpass.getuser() + '\\Documents'

# prompt user for a source folder to be backed up
def get_source_file():
	print("What folder would you like to backup?\nC:\\Users\\" + getpass.getuser() + ">", end='')
	user_input = input()
	source = os.path.join("C:\\Users\\" + getpass.getuser(), user_input)
	if user_input.lower() == 'exit':
		print("Terminated\n\n") #this is if the use prints 'exit'
		exit(0)
	elif user_input.lower() == 'here':
		return os.getcwd()
	# check if source exists
	if os.path.exists(source):
		pass
	else:
		print("Folder does not exist.")
		return get_source_file()
	return source

# Check os before operating
if os.name == 'nt':
	# Create Backups folder for storing backups
	backups_dir = os.path.join(parent_dir,"Backups")
	if not os.path.exists(backups_dir):
		os.makedirs(backups_dir)

	parent_dir = backups_dir
	# Setup destination path aka backup folder name
	now = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
	new_folder = 'Backup ' + str(now) # Backup YYYY-MM-DD_HHMMSS
	destination = os.path.join(parent_dir,new_folder)
	print("===== Files will be backed up to " + destination + " =====")

	# promp user for what to backup
	if sys.argv[1] == '':
		source = get_source_file()
	else:
		source = os.path.join("C:\\Users\\" + getpass.getuser(), sys.argv[1])
	print("===== " + source + " will be backed up =====")
	print("[====== Wait for confirmation \"done\" ======]")

	#create destination folder and copy over the files
	try:
		copytree(source,destination)
	except:
		print("Could not create backup folder. Exiting\nDid NOT backup\n")
		exit(0)
	print("done")
# if OS is not windows, end prematurely
else:
	print("This program currently only works on Windows operating systems.")
print("Bye bye.")
