# Pixel Console Image Renderer, Editor & Module

A simple renderer for images in the terminal using the .pci file format

## Installation & Usage

### Installing Via PyPI

Run this command to install PCI

`$ pip install pci`

Then to run PCI, run the following in your terminal

`$ pci`

### Installing Via GitHub

```
$ git clone https://github.com/El1teWatermelonGames/pci.git
$ cd pci
$ python setup.py install
```
*In linux you may need to type `python3` instead of `python`*

Then to run PCI, run the following in your terminal

`$ pci`

## Usage in code

### Rendering an image file

To render an existing image file you have to use the renderImage() function

***image.pci***
```
FFF000FFF00FFF
F0F00F000000F0
FFF00F000000F0
F0000F000000F0
F00000FFF00FFF
```

***example.py***
```
from pci.rem import renderImage

renderImage("image.pci")
```

### Rendering image data

This time you reformat the image yourself as a list in python & put it through a seperate function, renderData()

***example.py***
```
from pci.rem import renderData

image = [
    "FFF000FFF00FFF",
    "F0F00F000000F0",
    "FFF00F000000F0",
    "F0000F000000F0",
    "F00000FFF00FFF"
]

renderData(image)
```
