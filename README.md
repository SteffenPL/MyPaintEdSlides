# Draw your own presentations!

MyPaint is a great tool for digital drawing.
To my knowledge, there exists no tool so far, which automatically 
creates nice presentations out of MyPaint Layers.

# Presentations created with MyPaintEdSlides

[Talk on Symplectic Numerical Integration, Universtiy of Auckland, 2018](https://steffenpl.github.io/MyPaintEdSlides/test/output_complete/index.html)

[Short Talk on Parameter Idendification in ODE Models, University of Auckland, 2018](https://steffenpl.github.io/MyPaintEdSlides/test/param_id_in_ode_html/index.html)

[Student-Talk about Tangential Spaces, Technische Universität Kaiserslautern, 2018](https://steffenpl.github.io/MyPaintEdSlides/test/student_talk_html/index.html)

[Presentation about Fiber based Muscle Simulation (unfinished project), TU Kaiserslautern, 2018](https://steffenpl.github.io/MyPaintEdSlides/test/muscle_html/index.html)

[Presentation about Fiber based Muscle Simulation (master's thesis), Hausdorff Center of Mathematics, Bonn, 2018](https://steffenpl.github.io/MyPaintEdSlides/test/muscle_short_html/index.html)

[Presentation on Partially kinetic systems (aka 'particles on rails'), Kinetic Theory Coffee Break, 2020](https://steffenpl.github.io/MyPaintEdSlides/test/partially_kinetic_systems/index.html)


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
