# Technocalypse
If you are from the VWCC computer science club, you're in the right place!
## File Locations
The main executable file is located under `Technocalypse/usr/bin/game.py`.
All assets such as pictures, fonts, and sounds are in `Technocalypse/usr/lib/technocalypse/assets/`
## Debian Packaging
As of right now the plan is to package this game into a .deb file so it can be installed onto a raspberry pi. The `DEBIAN` folder and `share` folder are only for packaging purposes, and have no impact on the actual program. Keep in mind that this is being developed for a linux system, the file paths in the program need to be formatted correctly.
### Example of correct format:
```
usr/lib/technocalypse/assets/Techno.ttf
usr/bin/game.py
```
### Example of incorrect format:
```
usr\lib\technocalypse\assets\Techno.ttf
usr\bin\game.py
```
This also means certain files can only go in certain places. **All assets** need to go in `usr/lib/technocalypse/assets/`. The program file in `usr/bin/` needs to be the only file in that directory. Putting anything else in there will mess up the packaging process.
## License
This software is under the GNU GPL3.0+ license, which means it is free for anyone to copy, distribute, and modify. All of the assets used to make this game are from free sources, and it needs to remain that way.