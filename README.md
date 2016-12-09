# Quadtree

A Quadtree Implementation in Python, for Algorithms Design and Analysis class, Macalester Fall 2016.

Instructions:

Requires Pillow, which can be install via pip with
```
 pip install pillow
```

1. Prepare two data files: a PNG file for the base map and a TXT file for the points.

 The first line in the TXT file should give the dimension of the PNG, in the format "x y"
 
 The second line onwards are points, each in the form "x y"
 
 Name both of them the same except for the extension, for example "example.txt" and "example.png"
 
2. Run main.py in the terminal. The script runs on Python 3, so if you have Python 2 installed also, specify the Python version to run.
 ```
  python main.py
 ```
3. Type the name of the data file, without the extension, and hit Enter to run.

It should automatically create two new files:

1. A PNG file that ends in "Boxed". It is the PNG file with black grids for quadrants division.
2. A TXT file that ends in "Tree". It is a record of the tree that was created.
