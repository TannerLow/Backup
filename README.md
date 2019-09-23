# Backup
Creates a backup folder of a selected folder. It only supports Windows for the time being.

---

The program will ask for a source folder and will copy it to \\Documents\\Backups on the current user that is logged in.  
For example 

"Documents\\Projects" will copy the folder C:\\Users\\\<username\>\\Documents\\Projects 

to C:\\Users\\\<username\>\\Documents\\Backups\\

The files being copied over will be put in their own folder called "Backup YYYY-MM-DD_HHMMSS"  
to prevent the mixing of files as well as timestamp the backup.

---

When prompted for the source folder, type:  
* exit
  * to terminate the program
* here
  * to backup the directory the Backups.py file is currently in
* \<filepath\>
  * C:\\Users\\\<username\> is included for you. See example above.
  
---

## Update:
When being from command prompt the user can now specify a folder to copy immediately.  
<b>Ex. >Backups.py Documents\Important</b>  
This will not prompt the user for further input and will proceed to create a backup of the  
C:\\Users\\\<username\>\\Documents\\Important folder.
