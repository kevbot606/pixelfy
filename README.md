# Welcome to Pixelfy!

## Installation
Simply download the repository as a zip file, and open in your IDE of choice.

## How it works
Pixelfy uses Turtle graphics and Python Image Library to "pixelfy" your pictures. It iterates through the pixels in a given image, pulls an RGB tuple, and appends it to list.

After the user specifies a desired resolution, Pixelfy uses Turtle graphics to print a dotted grid, dot-by-dot, using the color data from the list of RGB tuples. In the end, the user is left with an abstracted version of the original image that they can screenshot and share.

## Using Pixelfy
After installing, run the main.py file. Enter the filepath to the image you want to abstract.

Next, you will be prompted for a level of detail on a scale of 1-10. **Important:** 1 is the highest level of detail, which will generate more dots at a smaller scale, resulting in a more detailed, less-abstracted final image. The higher the level of detail, the longer the image will take to process.

Note: Pixelfy has not been calibrated for numbers outside of this range, however, numbers greater than 10 can be provided for a more extreme level of abstraction. Results may vary.

## Example
![alt text](https://github.com/kevbot606/pixelfy/blob/main/pic.jpg?raw=true) =250x250
![alt text](https://github.com/kevbot606/pixelfy/blob/main/alt_pic.png?raw=true)




