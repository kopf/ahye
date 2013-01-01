# ahye

ahye is a server for saving and serving files submitted by gyazo screenshooters. 
It also features a web interface that supports uploading and mirroring images.

## Desktop Clients

### Windows

The Windows gyazo client is open source and [available on github.](https://github.com/gyazo/Gyazowin)
Simply change [the server address](https://github.com/gyazo/Gyazowin/blob/11152a5c3a5fe85f702c87cdd1a3f814f90f8218/gyazowin/gyazowin.cpp#L794) and recompile.

### Linux

A gyazo client for Linux is [available here](https://github.com/gyazo/Gyazo-for-Linux). Written in ruby, 
you'll need to [change the server address here](https://github.com/gyazo/Gyazo-for-Linux/blob/master/gyazo#L37) any then you're good to go.

### OS X

To use your ahye server with an OS X client, simply download the OS X client from [the official gyazo
website](http://www.gyazo.com). Then, edit `/Applications/Gyazo.app/Contents/Resources/script` with your favourite
editor, changing the `HOST` and `CGI` variables to point to your ahye server's upload endpoint.

You can also change the program's icon by following [these instructions](http://superuser.com/a/37813/90167) and using the icon [provided in the ahye
repository here](https://github.com/kopf/ahye/blob/master/ahye/static/progicon32.ico)

## Web interface

### Drag-and-drop uploads

To upload an image file you've already saved on your computer, just visit your ahye website and drag the image into the browser window. 
The file will automatically upload.

### Mirroring

It can be useful to mirror images already hosted elsewhere, especially in cases where the image might be removed from the server, or the remote server might go down due to a rush of traffic.

All you have to do is place the image's URL after the url of your ahye server. So, let's say your ahye server is located at `http://ahye.myweb.com`, and you want to mirror the file `http://i.imgur.com/EHWlL.jpg`, you just have to go to `http://ahye.myweb.com/http://i.imgur.com/EHWlL.jpg` and your ahye server will automatically rehost the image and redirect you to its own copy.
