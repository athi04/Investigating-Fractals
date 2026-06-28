# Investigating Fractals

Code accompanying my MMath dissertation on fractal geometry and complex dynamics.
The project produces images of several classic fractals and includes two
interactive, browser-based explorers for the Julia and Mandelbrot sets. The
written dissertation covers Hausdorff measure and dimension, box-counting
dimension, iterated function systems, and the Fatou–Julia theory behind the
Julia and Mandelbrot sets.

## Contents

| File | What it does |
| --- | --- |
| `cantor_set.py` | Draws the **Cantor set** by recursively removing the middle third of each interval and plotting successive layers. |
| `sierpinski.py` | Draws the **Sierpinski gasket** by recursively subdividing a triangle into its three corner sub-triangles. Exports high-resolution PNG and SVG. |
| `julia.html` | **Interactive Julia set explorer.** Renders the filled Julia set for a chosen complex parameter *c*, computed in the browser. |
| `mandelbrot.html` | **Interactive Mandelbrot set explorer.** Renders the Mandelbrot set with zoom, computed in the browser. |

## Background

A fractal is a set whose structure repeats across scales, typically with a
fractional (non-integer) dimension. This repository illustrates two families of
construction:

- **Iterated function systems** — the Cantor set and Sierpinski gasket are both
  fixed points of a small set of contraction maps. Repeatedly applying the maps
  drives any starting shape toward the fractal attractor; here that recursion is
  unrolled directly in code.
- **Complex dynamics** — the Julia and Mandelbrot sets arise from iterating the
  quadratic map *z → z² + c*. The Julia set fixes *c* and asks which starting
  points *z* stay bounded; the Mandelbrot set fixes *z = 0* and asks which
  parameters *c* keep the orbit bounded. Each pixel in the explorers is coloured
  by how quickly its orbit escapes.

## Running the Python scripts

```
pip install matplotlib numpy
python cantor_set.py
python sierpinski.py
```

Each script opens a figure and saves image files next to the script.
`sierpinski.py` writes both a 600 dpi PNG and a vector SVG.

## Running the interactive explorers

`julia.html` and `mandelbrot.html` are self-contained, no build step or server
needed. Either open the file directly in a browser, or view them live via
GitHub Pages (Settings → Pages → deploy from the `main` branch).
