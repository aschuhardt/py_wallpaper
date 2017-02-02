# py_wallpaper
A simple python script that generates colorful gradient-pattern wallpapers. I have it called in my .xinitrc to run and pass its output into Feh.

Example output:
![This is an example of what the script's output looks like using the default parameters](https://raw.githubusercontent.com/aschuhardt/py_wallpaper/master/output.png)

Requirements: Python 3.5 (3 will likely work), PIL (Pillow), Numpy, Argparse

Instructions:
  - Run the following commands with Python 3.5 and Pip installed (substitute correct version of Pip for your Python installation):
  
  ```
      pip3.5 install pillow
      
      pip3.5 install numpy
      
      pip3.5 install argparse
  ```
  
Arguments:

-f --filename file_path (default ./output.png): The path of the desired output file.

-w --width some_integer (default 1366): The width of the final image.

-t --height some_integer (default 768): The height of the final image.

-r --radius some_integer (default 128): The radius of the Gaussian blur pass.

-o --offset some_integer (default 50): The maximum amount each channel of the base color will be offset (RGB). Higher = more color variation.

-c --basecolor (hexidecimal RGB string (i.e. "#FFFFFF")) (default randomly chosen): The base color that will be used to generate the image.
