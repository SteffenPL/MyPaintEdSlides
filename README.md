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
(see also https://arxiv.org/abs/1911.05468)

# MyPaintEdSlides

*Currently the package is not final!*

We sketch the basic idea behind the presentation generator.

For a given .ora file, we extract all layers and
assemble slides according to the following rule.

Example:

slides.ora:
- layer 0: name="background"
- layer 1: name="t"
- layer 2: name="a"
- layer 3: name="b:ta"
- layer 4: name="c:tb"

ref.ora
- layer 0: name="background"
- layer 1: name="a:\_"

This would generate a HTML presentation with
two slides, containting the following content:

slide 0:
- subslide 0: layer-{1,2,3}
- subslude 0: layer-{1,3,4}

slide 1:
- subslide 0: layer-{1}

If wanted, the background could also be added, otherwise
a global background is used.

The HTML is based on reveal.js, we only generate the body for the presentation.

# Current state

At the moment a general interface is missing. Therefore it is not 
ready to be used without modifying the python code :'(

Anyway, the first presentations are already there and a more user friendly version is in progress.

