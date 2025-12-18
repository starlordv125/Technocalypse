# Technocalypse
If you are from the VWCC computer science club, you're in the right place!
## Pygame
You will need to install the `pygame` and possibly `pillow` python package. You can use `pip` or if you have linux you can use your package manager.
## File Locations
All assets such as pictures, fonts, and sounds are in `./assets/`.

We may change this later to better organize all of the files, if so this readme file will update to reflect that.
## Packaging
We are going to use pyinstaller to package the program, there is a function in `technocalypse.py` dedicated to finding the correct path for files depending on the OS. Make sure to use the correct slash when opening files. Both the program and the final packages should work on both Linux and Windows.
### Example of correct format:
```
assets/Techno.ttf
```
### Example of incorrect format:
```
assets\Techno.ttf
```
## License
This software is under the GNU GPL3.0+ license, which means it is free for anyone to copy, distribute, and modify. All of the assets used to make this game are from free sources, and it needs to remain that way. Any modification or fork of this game is legally required to use the GNU GPL3.0 or above license.
