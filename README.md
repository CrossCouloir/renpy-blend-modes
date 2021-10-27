# renpy-blend-modes
Photoshop-style blend mode shaders for Ren'Py.

This library adapts Jamie Owen's [glsl-blend library](https://github.com/jamieowen/glsl-blend) to be used as Ren'Py shaders, allowing you to apply Photoshop-style image blending via a Ren'Py transform.

## Installation
This project consists of a series of .rpy files. This means the best way to include it into your Ren'Py project is to download the files and place them into your `game` directory. You do not need to include the files for any shaders you don't plan to use, however you must include `base.rpy`.

## Usage
Each shader file specifies a list of arguments necessary to use the shader in a transform. Read the `USAGE` section of the comment at the top of a shader file to see what arguments need to be passed.

Here is an example of how shaders are used in transforms:
```
transform my_special_lighting:
  shader "crosscouloir.soft_light"
  u_light_color (0.5, 0.5, 0.5, 0.5)
```

This transform uses the `"crosscouloir.soft_light"` shader, defined in `soft_light.rpy`. As specified in the usage instructions for `soft_light`, there is one required parameter `u_light_color` which is a 4-tuple of floats between 0 and 1. The transform defined in the example above creates a soft light of uniform medium grey with a 50% intensity, which will create a subtle desaturation and give a neutral colour temperature to the underlying image.

Once your transform is created, you can use it like any other transform.
```
show protagonist_sprite at center, my_special_lighting
```

## Contributing
This project accepts pull requests. Please create a pull request if you would like to contribute. If you have any feature requests, please create a project issue and I will address it as soon as I can.

## License
This project is made available under the MIT license. Please see LICENSE.md for more information.
