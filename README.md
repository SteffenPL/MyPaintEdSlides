# Draw your own presentations!

MyPaint is a great tool for digital drawing.
To my knowledge, there exists no tool so far, which automatically 
creates nice presentations out of MyPaint layers.

All this small project does is to take a file of raster layers (.ora format) and a html template
to convert this into a reveal.js html presentation.

Demo:
[Talk on Symplectic Numerical Integration, Universtiy of Auckland, 2018](https://steffenpl.github.io/MyPaintEdSlidesExamples/talks/2018/symplectic_methods/index.html#/)



# Usage

In very, very short:
 1. use MyPaint (or Krita) to create the slides, save as `.ora` into one folder. The slides will appear in alphabetical order.
 2. copy the `demo` folder to a place which will later contain the final presentation. (We need the backgrounds and the reveal.js files)
 3. run ```python ora_interface.py "<input folder>" <output_folder>```

Now, the output folder contains the `index.html` which is the presentation.

# Tutorial


## How to generate slides

1. Clone the repository 
`git clone https://github.com/SteffenPL/MyPaintEdSlides.git`

2. Open the new folder MyPaintedSlides
`cd MyPaintEdSlides`

3. 

## How to create the slides (with MyPaint)

Reveal.js supports slides (left-right) and subslides (up-down).

We use seperate `.ora` files to differentiate between slides and
within one `.ora` file we use groups to generate the subslides.

This is best explained with an example:

000_title.ora:
- layer 0: name="background"
- layer 1
- layer 2

001_slide.ora:
- layer 0: name="background"
- layer 1
- group 1:
  - layer 2
  - group 2:
    - layer 3
  - layer 4
- layer 5


This would generate a HTML presentation with
two slides, containting the following content:

slide 0:
- subslide with layer 1
- subslide with layer 1,2

slide 1:
- subslide with layer 1
- subslide with layer 1,2 (enter group 1)
- subslide with layer 1,2,3 (enter group 2)
- subslide with layer 1,2,4 (leave group 2, still within group 1)
- subslide with layer 1,5 (leave group 1)

If wanted, the background could also be added, otherwise
a global background is used.

### Flags

It is possible to add certain flags to alter the behaviour:
- 


## Creating own html templates


## Including videos



# Presentations created with MyPaintEdSlides

[Talk on Symplectic Numerical Integration, Universtiy of Auckland, 2018](https://steffenpl.github.io/MyPaintEdSlidesExamples/talks/2018/symplectic_methods/index.html#/)

[Short Talk on Parameter Idendification in ODE Models, University of Auckland, 2018](https://steffenpl.github.io/MyPaintEdSlidesExamples/talks/2018/param_id_in_ode/index.html)

[Student-Talk about Tangential Spaces, Technische Universität Kaiserslautern, 2018](https://steffenpl.github.io/MyPaintEdSlidesExamples/talks/2018/student_talk/index.html)

[Presentation about Fiber based Muscle Simulation (unfinished project), TU Kaiserslautern, 2018](https://steffenpl.github.io/MyPaintEdSlidesExamples/talks/2018/master_thesis/index.html)

[Presentation about Fiber based Muscle Simulation (master's thesis), Hausdorff Center of Mathematics, Bonn, 2018](https://steffenpl.github.io/MyPaintEdSlidesExamples/talks/2018/master_thesis_short/index.html)

[Presentation on Partially kinetic systems (aka 'particles on rails'), Kinetic Theory Coffee Break, 2020](https://steffenpl.github.io/MyPaintEdSlidesExamples/talks/2020/partially_kinetic_systems/index.html)




# MyPaintEdSlides

*Currently the package is not final!*

We sketch the basic idea behind the presentation generator.

For a given .ora file, we extract all layers and
assemble slides according to the following rule.

Example:

000_title.ora:
- layer 0: name="background"
- layer 1
- layer 2
- layer 3

001_slide.ora:
- layer 0: name="background"
- layer 1
- group 1:
  - layer 2
  - group 2:
    - layer 3
  - layer 4
- layer 5


This would generate a HTML presentation with
two slides, containting the following content:

slide 0:
- subslide with layer 1
- subslide with layer 1,2
- subslide with layer 1,2,3

slide 1:
- subslide with layer 1
- subslide with layer 1,2 (enter group 1)
- subslide with layer 1,2,3 (enter group 2)
- subslide with layer 1,2,4 (leave group 2, still within group 1)
- subslide with layer 1,5 (leave group 1)

If wanted, the background could also be added, otherwise
a global background is used.

The HTML is based on reveal.js, this python script does only generate the body for the presentation
and composes the layers according to their groups.

# Documentation

There is no documentation yet. If someone is interested in using it, please write me or open an issue.
Then, I will provide install instructions and more detailed documenation.
