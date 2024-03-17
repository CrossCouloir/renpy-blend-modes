
init python:
  CC_VIVID_LIGHT_NAME = "crosscouloir.vivid_light"

  _vivid_light_blend_mode = BlendMode(CC_VIVID_LIGHT_NAME)
  _vivid_light_blend_mode.vars = """
uniform float u_lod_bias;
uniform sampler2D tex0;
attribute vec2 a_tex_coord;
varying vec2 v_tex_coord;

uniform tex1 sampler2D;
"""
  _vivid_light_blend_mode.fragment_functions = """
float blendColorBurn(float base, float blend) {
  return (blend==0.0)?blend:max((1.0-((1.0-base)/blend)),0.0);
}

float blendColorDodge(float base, float blend) {
  return (blend==1.0)?blend:min(base/(1.0-blend),1.0);
}

float blendVividLight(float base, float blend) {
  return (blend<0.5)?blendColorBurn(base,(2.0*blend)):blendColorDodge(base,(2.0*(blend-0.5)));
}

vec3 blendVividLight(vec3 base, vec3 blend) {
  return vec3(blendVividLight(base.r,blend.r),blendVividLight(base.g,blend.g),blendVividLight(base.b,blend.b));
}

vec3 blendVividLight(vec3 base, vec3 blend, float opacity) {
  return (blendVividLight(base, blend) * opacity + base * (1.0 - opacity));
}
"""
  _vivid_light_blend_mode.vertex_shader = """
v_tex_coord = a_tex_coord;
"""
  _vivid_light_blend_mode.fragment_shader = """
vec4 bgcolor = texture2D(tex0, v_tex_coord.st, u_lod_bias);
vec4 maskcolor = texture2D(tex1, v_tex_coord.st, u_lod_bias)
vec3 blended = blendVividLight(bgcolor.xyz, maskcolor.xyz, maskcolor.w);
gl_FragColor = vec4(blended, bgcolor.w);
"""

  _vivid_light_blend_mode.register()

  def cc_vivid_light(base, tex, fit=True):
    return Model().child(base, fit=fit).texture(tex).shader(CC_VIVID_LIGHT_NAME)