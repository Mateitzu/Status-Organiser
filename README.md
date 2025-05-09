# Status-Organiser
A software to organise users and their status. It is not pretty but sometimes useful.

User-Instruction-Manual:

Super-Basic:

When you start the program, after the logo,author showed, you should be asked to enter a password, default password is "12345", you can also change the password in the settings. 

After the password is entered correctly you should be prompted with:
"Enter Command, adduser, adduserlist, removeuser, removeuserlist, banuser, unbanuser, showusers, wipeserver, exit, settings, info, help, entervisualmode, exitvisualmode| : "
You have to enter one of these 14 commands to interact with the program

Basic:

Here's what every command does:

adduser: adds an user with a name entered by you later
adduserlist: adds a list of users from a ".json" list. To generate one of these files, not type it manually, you can download a software from(link 1)
removeuser: removes an user with a name entered by you later
removeuserlist: removes a list of user from a ".json" list.
banuser: bans an user with a name entered by you later
unbanuser: unbans an user with a name entered by you later
showusers: shows all users saved
wipeserver: wipes all data(users, not settings)
exit: closes the software
settings: opens a tab for settings
info: shows program info
help: shows the "User-Instruction-Manual"
entervisualmode: enters the visual-mode. This mode shows everyuser before you type in a command
exitvisualmode: exits the visual-mode

Settings Instructions:

To change a setting/settings you have a to enter the settings tab. After you've done that you will be shown all the settings available to be changed. To actually change one of them, you have to enter a number from 1 to 9 and change the value of the setting. ex: 1,2,3,on,off,white,blue,magenta.

Here's all values that can be entered at each number:

1. 1,2,3,4,5,etc.(any int. number)
2. 1,2,3,4,5,etc.(any int. number)
3. white, red, green, blue, yellow, cyan, magenta
4. (anything, but be carefoul because it's your password)
5. on,off
6. on,off
7. on,off
8. (cannot enter anything, because it's a command)
9. (cannot enter anything, because it's a command)

Here's what every setting means:

1. Logo-Time = how much time does the logo stay on screen when you boot/close the program
2. Message-Time = after how much time the screen refreshes when a message is shown.(attention! do not confuse a message with an error)
3. Text Colour = what colour should the text have.(only the normal text, not the settings, info, help, author, and others)
4. Password = software password
5. Fast Exit = after you close the program it closes instantly or shows the logo, and then closes.
6. Show User IDs = when the users list is showed, should it show the users id too at the same time?
7. Auto Visual Mode = it activates the visual-mode when you start the software
8. Back = goes back
9. Save Settings = saves settings and then goes back

Challanging:

Here is how to make a json file yourself:
1. Create a txt file.
2. Rename it and give it the extension ".json"
3. Open the file with a text editor(if you don't know much just open it with notepad)
4. Type "{}"
5. Set cursor here: "{|}"(between the curly braces)
6. Press ENTER
7. Type :
"name" : {"banned": false},
8. Instead of "name" type the user's name
9. Repeat the process with different names(not optional)
10. When you type the last user type it without the ","
That is all :D

Links:

link1: https://github.com/Mateitzu/JSON-Generator
