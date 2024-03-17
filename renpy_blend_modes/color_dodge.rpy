init python:
    CC_COLOR_BURN_NAME = "crosscouloir.color_dodge"

    _color_dodge_blend_mode = BlendMode(CC_COLOR_DODGE_NAME)

    _color_dodge_blend_mode.vars = """
uniform float u_lod_bias;
uniform sampler2D tex0;
attribute vec2 a_tex_coord;
varying vec2 v_tex_coord;

uniform tex1 sampler2D;
"""
    _color_dodge_blend_mode.fragment_functions = """
float blendColorDodge(float base, float blend) {
    return (blend==1.0)?blend:min(base/(1.0-blend),1.0);
}

vec3 blendColorDodge(vec3 base, vec3 blend) {
    return vec3(blendColorDodge(base.r,blend.r),blendColorDodge(base.g,blend.g),blendColorDodge(base.b,blend.b));
}

vec3 blendColorDodge(vec3 base, vec3 blend, float opacity) {
    return (blendColorDodge(base, blend) * opacity + base * (1.0 - opacity));
}
"""
    _color_dodge_blend_mode.vertex_shader = """
v_tex_coord = a_tex_coord;
"""
    _color_dodge_blend_mode.fragment_shader = """
vec4 bgcolor = texture2D(tex0, v_tex_coord.st, u_lod_bias);
vec4 maskcolor = texture2D(tex1, v_tex_coord.st, u_lod_bias)
vec3 blended = blendColorDodge(bgcolor.xyz, maskcolor.xyz, maskcolor.w);
gl_FragColor = vec4(blended, bgcolor.w);
"""
    _color_dodge_blend_mode.register()

    def cc_color_dodge(base, tex, fit=True):
        return Model().child(base, fit=fit).texture(tex).shader(CC_COLOR_DODGE_NAME)