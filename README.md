# ahye

ahye is a server for saving and serving files submitted by gyazo screenshooters. 
It also features a web interface that supports uploading and mirroring images.

## Desktop Clients

### Windows

The Windows gyazo client is open source and [available on github.](https://github.com/gyazo/Gyazo-for-Linux/blob/master/gyazo)
Simply change [the server address](https://github.com/gyazo/Gyazowin/blob/11152a5c3a5fe85f702c87cdd1a3f814f90f8218/gyazowin/gyazowin.cpp#L794) and recompile.

### Linux

A gyazo client for Linux is [available here](https://github.com/masui/gyazo-ruby). Written in ruby, 
you'll need to [change the server address here](https://github.com/gyazo/Gyazo-for-Linux/blob/master/gyazo#L37) any then you're good to go.

### OS X

A mac client, also written in ruby, is [available here](https://github.com/masui/gyazo-ruby). Just [change the server address here](https://github.com/masui/gyazo-ruby/blob/c62a06a70b8a1de602e245a46b0d5d70b9615f22/lib/gyazo.rb#L32).

## Web interface

### Drag-and-drop uploads

To upload an image file you've already saved on your computer, just visit your ahye website and drag the image into the browser window. 
The file will automatically upload.

### Mirroring

It can be useful to mirror images already hosted elsewhere, especially in cases where the image might be removed from the server, or the remote server might go down due to a rush of traffic.

All you have to do is place the image's URL after the url of your ahye server. So, let's say your ahye server is located at `http://ahye.myweb.com`, and you want to mirror the file `http://i.imgur.com/EHWlL.jpg`, you just have to go to `http://ahye.myweb.com/http://i.imgur.com/EHWlL.jpg` and your ahye server will automatically rehost the image and redirect you to its own copy.