
init python:
  """
  Soft Light shader

  This shader implements the soft light blend mode. It allows you to use any RGBA colour
  as a lighting source for the transformed image. The RGB component controls the colour
  of the lighting, and the A component controls the intensity of the lighting. With an
  A value of 0, the colour of the base image will be unchanged.

  This implementation uses the Photoshop soft light algorithm. Since it is not possible
  to supply anything other than a solid color as the overlay image, you will not be able
  to observe the discontinuity at b=0.5.

  USAGE:
    Args:
      u_light_color: the colour of the light. This is a 4-tuple of floats between 0 and 1
        representing the RGBA values. If you are using colour values in the 0-255
        spectrum, divide them by 255.
  """


  soft_light_blend_mode = BlendMode("crosscouloir.soft_light")
  soft_light_blend_mode.vars = """
uniform float u_lod_bias;
uniform sampler2D tex0;
uniform vec4 u_light_color;
attribute vec2 a_tex_coord;
varying vec2 v_tex_coord;
"""
  soft_light_blend_mode.frag_functions = """
float blendSoftLight(float base, float blend) {
  return (blend<0.5)?(2.0*base*blend+base*base*(1.0-2.0*blend)):(sqrt(base)*(2.0*blend-1.0)+2.0*base*(1.0-blend));
}

vec3 blendSoftLight(vec3 base, vec3 blend) {
  return vec3(blendSoftLight(base.r,blend.r),blendSoftLight(base.g,blend.g),blendSoftLight(base.b,blend.b));
}

vec3 blendSoftLight(vec3 base, vec3 blend, float opacity) {
  return (blendSoftLight(base, blend) * opacity + base * (1.0 - opacity));
}
"""
  soft_light_blend_mode.vertex_shader = """
v_tex_coord = a_tex_coord;
"""
  soft_light_blend_mode.fragment_shader = """
vec4 bgcolor = texture2D(tex0, v_tex_coord.st, u_lod_bias);
vec3 blended = blendSoftLight(bgcolor.xyz, u_light_color.xyz, u_light_color.w)
gl_FragColor = vec4(blended, bgcolor.w);
"""

  soft_light_blend_mode.register()
