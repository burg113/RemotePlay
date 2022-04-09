# Remote Play

Remote Play is a console application written in python that allows you to transfer your keyboard inputs to another pc.
It allows for all sorts of fun ways to play with your friends online and still share controlls as if you were sitting right next to them.


##Install

First download the code from this repository [green "Code" button -> "Download ZIP"] and unzip it.

Then install python (and pip) if you do not have already and add it to the path variable.
If everything is working correctly you should be able to execute the pythoncheck.bat file without any errors (you should be given the version of both your python and pip version).

Now execute the pipinstalls.bat file in order to get all the required python library's.

If you are the one who is hosting the server you will also have to port forward port 5000 for TCP.
Then you will have to give your friends your public ip (which you can find here: myip.com) and they will have to enter it in their programs. 
(Currently you will have to change the python remote_client.py script)


##Read before Trying

As once the client program is executed all of your key and mouse inputs are deactivated,
it is convenient to know that you can regain control over your system by pressing "AltGr" + "T". 

In case any problems occur please contact us. Thank you for trying Remote Play!

## Known issues 

When the server is closed all connected clients will crash upon any input.

Scrolling on a trackpad (scrolling gesture) will not work.

Similarly, when scrolling to fast (can only be achieved on trackpad or with infinite scroll wheel) a lot of latency will be introduced. You will have to wait untill all of the scroll inputs are executed.
