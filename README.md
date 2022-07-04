# Draw your own presentations!

MyPaint is a great tool for digital drawing.
To my knowledge, there exists no tool so far, which automatically 
creates nice presentations out of MyPaint layers.

All this small project does is to take a file of raster layers (.ora format) and a html template
to convert this into a reveal.js html presentation.

Demo:
[Talk on Symplectic Numerical Integration, Universtiy of Auckland, 2018](https://steffenpl.github.io/MyPaintEdSlidesExamples/talks/2018/symplectic_methods/index.html#/)



# Usage

## In very, very short:
 1. use MyPaint (or Krita) to create the slides, save as `.ora` into one folder. The slides will appear in alphabetical order.
 3. run ```python ora_interface.py <template_file> <input(s)> <output_folder>```

## Detailed instructions:
1. Install python. A popular choice is https://www.anaconda.com/
2. Download a current release of this repository: https://github.com/SteffenPL/MyPaintEdSlides/releases/tag/v0.1
3. Unpack the repository to a folder of your choice.
4. Create a subfolder called `talk` (or any name you want).
5. Create your slides as `.ora` files with MyPaint or Krita and store the slides in the folder `talk`.
6. Open a python terminal and navigate to the root of the repository folder (which containts the file `ora_interface.py`.
7. Run ```python ora_interface.py html_templates/reveal_with_chalkboard/ ./talk ./slides/talk```
8. Open the file `./slides/talk/index.html`. This should be your presentation.

More advanced usage includes to modify the html_template. Options are to change the background by editing the line
```javascript
// Parallax background image
parallaxBackgroundImage: 'parallax-2.jpg', // e.g. "https://s3.amazonaws.com/hakim-static/reveal-js/reveal-parallax-1.jpg"
```

You can draw on the slides during the talk by pressing the key `c` thanks to https://github.com/rajgoel/reveal.js-plugins/tree/master/chalkboard

# Tutorial/Example

We will use the slides from the folder `examples/mypaint` to generate the presentation `examples/mypaint/index.html`.

## How to generate slides

1. Clone the repository 
```git clone https://github.com/SteffenPL/MyPaintEdSlides.git```

2. Open the new folder MyPaintedSlides
```cd MyPaintEdSlides```

3. Call the program `ora_interface` in a python shell:
```python ./ora_interface.py ./html_templates/reveal_with_chalkboard/default.html_template ./examples/mypaint/*.ora ./examples/mypaint/build```

You might have to install missing python libraries. (PIL, numpy)
Now, the folder `./examples/mypaint/build` should contain the example presentation in the file `index.html`, see
[demo](https://steffenpl.github.io/MyPaintEdSlides/examples/mypaint/build/index.html#/).

The parameters are expected to be such that:
- `<template_file>` is a HTML file which contains a line `<!--slides-->` which will be the place were the slides are inserted.
Moreover, the parent folder of this file will be copied into the output directory, i.e. all javascript dependencies and backgrounds should be in the parent folder of the file.
- `<input(s)>` can be either a single `.ora` file or you can use `*.ora` to determine a collection of `.ora` files.
- `<output_folder>` the folder were the presentation will be generated.


## How to create the slides (with MyPaint)

Reveal.js supports slides (left-right) and subslides (up-down).

We use seperate `.ora` files to differentiate between slides and
within one `.ora` file we use groups to generate the subslides.

This is best explained with an example:

```
000_title.ora:
- layer 0: name="background"
- layer 1
- layer 2

001_groups.ora:
- layer 0: name="background"
- layer 1
- group 1:
  - layer 2
  - group 2:
    - layer 2.1
  - group 3
- layer 4 (skip)
- layer 5
```

This would generate a HTML presentation with
two slides, containting the following content:

```
slide 0:
- subslide with layer 1
- subslide with layer 1,2

slide 1:
- subslide with layer 1
- subslide with layer 1,2 (enter group 1)
- subslide with layer 1,2,2.1 (enter group 2)
- subslide with layer 1,2,3 (leave group 2, still within group 1)
- subslide with layer 1,5 (leave group 1, skip Layer 4)
```

If wanted, the background could also be added, otherwise
a global background is used.

### Flags

It is possible to add certain flags to alter the behaviour:
- If the layer is called `background`, it will be ignored. (There is a switch in the python code, but it is not exposed yet.)
- If the layer constaints the string `(skip)` it will be ignored.

There are a few additions planned, namely: `(delete:<Layer name>)` to remove a layer in the following subslides.

## Creating own html templates

The `default.html_template` file is just a `.html` file were the line `<!--slides-->` will be replaced by the generates slides.
So, any reveal.js html file can be transformed into a template by just inserting `<!--slides-->` in the body at the position of the slides.

## Including videos

The generated presentation can be edited afterwards. In the past, I often used this to add videos. See for example 
[here](https://steffenpl.github.io/MyPaintEdSlidesExamples/talks/2018/symplectic_methods/index.html#/14/8).

# Presentations created with MyPaintEdSlides

[Talk on Symplectic Numerical Integration, Universtiy of Auckland, 2018](https://steffenpl.github.io/MyPaintEdSlidesExamples/talks/2018/symplectic_methods/index.html#/)

[Short Talk on Parameter Idendification in ODE Models, University of Auckland, 2018](https://steffenpl.github.io/MyPaintEdSlidesExamples/talks/2018/param_id_in_ode/index.html)

[Student-Talk about Tangential Spaces, Technische Universität Kaiserslautern, 2018](https://steffenpl.github.io/MyPaintEdSlidesExamples/talks/2018/student_talk/index.html)

[Presentation about Fiber based Muscle Simulation (unfinished project), TU Kaiserslautern, 2018](https://steffenpl.github.io/MyPaintEdSlidesExamples/talks/2018/master_thesis/index.html)

[Presentation about Fiber based Muscle Simulation (master's thesis), Hausdorff Center of Mathematics, Bonn, 2018](https://steffenpl.github.io/MyPaintEdSlidesExamples/talks/2018/master_thesis_short/index.html)

[Presentation on Partially kinetic systems (aka 'particles on rails'), Kinetic Theory Coffee Break, 2020](https://steffenpl.github.io/MyPaintEdSlidesExamples/talks/2020/partially_kinetic_systems/index.html)



# Documentation

There is no documentation yet. If someone is interested in using it, please write me or open an issue.
Then, I will provide install instructions and more detailed documenation.
