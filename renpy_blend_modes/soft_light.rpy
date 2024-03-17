
init python:
  CC_SOFT_LIGHT_NAME = "crosscouloir.soft_light"

  _soft_light_blend_mode = BlendMode(CC_SOFT_LIGHT_NAME)
  _soft_light_blend_mode.vars = """
uniform float u_lod_bias;
uniform sampler2D tex0;
attribute vec2 a_tex_coord;
varying vec2 v_tex_coord;

uniform tex1 sampler2D;
"""
  _soft_light_blend_mode.fragment_functions = """
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
  _soft_light_blend_mode.vertex_shader = """
v_tex_coord = a_tex_coord;
"""
  _soft_light_blend_mode.fragment_shader = """
vec4 bgcolor = texture2D(tex0, v_tex_coord.st, u_lod_bias);
vec4 maskcolor = texture2D(tex1, v_tex_coord.st, u_lod_bias)
vec3 blended = blendSoftLight(bgcolor.xyz, maskcolor.xyz, maskcolor.w);
gl_FragColor = vec4(blended, bgcolor.w);
"""

  _soft_light_blend_mode.register()

  def cc_soft_light(base, tex, fit=True):
    return Model().child(base, fit=fit).texture(tex).shader(CC_SOFT_LIGHT_NAME)