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

- **Sel Mei 30 11:25:26 WIB 2017**
	- Trying to compile in Linux.
	- Use `Pillow` instead of `PIL`
	- Looks like `PIL` is installed for 64 bit instead of 32 bit
	```
	05-30 12:32:44.160 10290 10317 I python  :  ImportError: dlopen failed: "/data/data/ugm.dteti.pythoncompress.pythoncompress/files/app/lib/python2.7/site-packages/PIL/_imaging.so" is 64-bit instead of 32-bit
	```
- **Sen Jun  5 09:57:47 WIB 2017**
	- Try to compile using ubuntu 32 bit in virtual box: completed using Android API target 19; SDK 20.
	- Got this message when running the app:
	```
	06-05 09:55:01.870  7535  7559 I python  :  ImportError: dlopen failed: "/data/data/ugm.dteti.pythoncompress.pythoncompress/files/app/lib/python2.7/site-packages/PIL/_imaging.so" has unexpected e_machine: 3
	```
