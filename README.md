# ahye

ahye is a server for saving and serving files submitted by gyazo screenshooters. 
It also features a web interface that supports uploading and mirroring images.

## Clients

### Windows

The Windows gyazo client is open source and [available on github.](https://github.com/gyazo/Gyazowin)
Simply change [the server address](https://github.com/gyazo/Gyazowin/blob/11152a5c3a5fe85f702c87cdd1a3f814f90f8218/gyazowin/gyazowin.cpp#L794) and recompile.

### Linux

A gyazo client for Linux is [available here](https://github.com/masui/gyazo-ruby). Written in ruby, 
you'll simply need to [change the server address here](https://github.com/masui/gyazo-ruby/blob/c62a06a70b8a1de602e245a46b0d5d70b9615f22/lib/gyazo.rb#L32).

### OS X

The ruby client above should also work for OS X. If there are actually any OS X-specific clients out there, add the info here and submit a pull request!