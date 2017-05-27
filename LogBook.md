Image Compression in Python
===========================
The log book.

- **Sat May 27 12:31:43 WIB 2017**
	- Trying `buildozer`.
		- https://kivyspacegame.wordpress.com/2014/06/30/tutorial-how-to-build-python-for-android-with-ubuntu-and-buildozer/
		- http://blog.rhesoft.com/2014/07/17/python-for-android-tutorial-1-using-the-accelerometer/
	- Image compression in Python
		- https://www.softwariness.com/articles/reduce-image-file-sizes-using-python/
	- Other options: SL4A
		- https://github.com/kuri65536/sl4a
		- Run SL4A from native app: intent builder.
	- `buildozer` always failed when compiling `pyjnius`, possibly because of space character in the directory name. Solved by removing space character in the folder name.
	- If other libraries are needed, eg., `numpy` or `PIL`, these shuould be compiled specifically for the device architecture, which is mostly frustating.