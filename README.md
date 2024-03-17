# renpy-blend-modes
Photoshop-style blend mode shaders for Ren'Py.

This library adapts Jamie Owen's [glsl-blend library](https://github.com/jamieowen/glsl-blend) to be used as Ren'Py shaders, allowing you to apply Photoshop-style image blending via a Ren'Py transform.

## Installation
This project consists of a series of .rpy files. This means the best way to include it into your Ren'Py project is to download the files and place them into your `game` directory. You do not need to include the files for any shaders you don't plan to use, however you must include `base.rpy`.

To download an archive of this project, click the green Code button on GitHub and select "Download ZIP".

## Prerequisites
You must have a version of Ren'Py which supports model-based rendering.

## Blend modes
A few additional simple blend modes have been added to the `config.gl_blend_func` dictionary. If you add the appropriate source files to your project, you'll be able to use any of these blend functions with the `blend` transform property. The following blend modes have been added in this way:

* `add`
* `linear_dodge` (synonym for `add`)
* `lighten`
* `darken`

## Blend shaders
More complex blend modes are implemented as GLSL shaders that will blend a texture image onto a base image using the specified blend mode. The easiest way to include any of these shaders is to use one of the included shader functions packaged with this library. Each shader function has the name `cc_<blend_mode_name>` (for example, `cc_screen` or `cc_soft_light`). They take the following arguments:
* `base` (Displayable): the base displayable, onto which other image data will be blended.
* `tex` (Displayable): the texture displayable, which will be blended onto the base displayable in the specified mode.
* `fit` (boolean, default `True`): if True, `tex` will be resized to be the same size as `base`. Weird stuff may happen if you pass `False`.

Here is an example of how shaders are used in transforms:
```
transform my_special_lighting(child=None):
  cc_soft_light(child, Solid("#ffffff7f"))
```

This transform applies a partially transparent pure white using the `cc_soft_light` displayable. Note that the transform takes the `child=None` argument: for the transform to work correctly, you must include this argument. Ren'Py will correctly set the value of `child` to be the base displayable the transform is applying to. `cc_soft_light`, and the other blend mode functions, return a displayable which will be the child displayable of your transform.

Once you've created the transform, you can use it the same way you'd use any other transform.
```
show protagonist_sprite at center, my_special_lighting
```

The following shaders are currently available:
* `cc_color_burn`
* `cc_color_dodge`
* `cc_difference`
* `cc_exclusion`
* `cc_linear_burn`
* `cc_overlay`
* `cc_screen`
* `cc_soft_light`
* `cc_vivid_light`

## Limitations
Animating between the blend modes is not supported. You may get wacky results, or it may cause crashes, or nothing may happen. Shader-based transforms may not work with layered images.

## Contributing
This project accepts pull requests. Please create a pull request if you would like to contribute. If you have any feature requests, please create a project issue and I will address it as soon as I can.

## License
This project is made available under the MIT license. Please see LICENSE.md for more information.
