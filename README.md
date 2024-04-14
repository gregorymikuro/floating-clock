# floating-clock
#### I made this for my parrot os but can work in most oss.

The floating clock Python script I provided should be able to run on most desktop operating systems that have Python and Tkinter installed, including:

*  Linux: It will work on Linux distributions like Parrot OS, Ubuntu, Debian, Fedora, etc. Tkinter is included in the Python standard library on Linux.

*  macOS: Python and Tkinter are both available on macOS by default or via Homebrew/pip. It will run without any issues.

*  Windows: On Windows, Python comes bundled with Tkinter. So as long as Python is installed, the script can run without problems.

Some operating systems it may not work on:

   Android/iOS: Since these are mobile operating systems, a floating GUI window app doesn't really make sense. Tkinter isn't available.

   Embedded/IoT systems: If the OS doesn't support X11 or have GUI capabilities, Tkinter won't be available to use.

   Proprietary/closed source OS: Unlikely to have Python/Tkinter pre-installed by default. May require additional installation steps.

So in summary:

*    Linux - Yes, will work out of the box
*    macOS - Yes
*    Windows - Yes
*    Android/iOS - No
*    Embedded systems - Possibly no
*    Proprietary OS - Maybe, depends on software availability

As long as the OS supports Python and Tkinter, the script should run fine. The main requirements are having X11/GUI capabilities and Python installed. Most mainstream desktop OS will meet those requirements. Let me know if you have any other specific OS in mind.
