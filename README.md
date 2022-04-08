# Remote Play

Remote Play is a console application written in python that allows you to transfer your keyboard inputs to another pc.
It allows for all sorts of fun ways to play with your friends online and still share controlls as if you were sitting right next to them.

##Install
First download the code from this repository.

Then install python (and pip) if you do not have already and add it to the path variable.

now open cmd and execute:

pip install pynput

pip install pywin32

...

If you are the one who is hosting the server you will also have to port forward port 5000 for TCP.
Then you will have to give your friends your public ip (which you can find here: myip.com) and they will have to enter it in their programs. 
(Currently you will have to change the python remote_client.py script)




##Read before Trying

As once the client program is executed all of your key and mouse inputs are deactivated,
it is convenient to know that you can regain control over your system by pressing "AltGr" + "T". 

In case any problems occur please contact us. Thank you for trying Remote Play!

