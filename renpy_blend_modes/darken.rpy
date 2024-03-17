init python:
    CC_DARKEN_NAME = "crosscouloir.darken"

    _darken_blend_mode = BlendMode(CC_DARKEN_NAME)

    _darken_blend_mode.vars = """
uniform float u_lod_bias;
uniform sampler2D tex0;
attribute vec2 a_tex_coord;
varying vec2 v_tex_coord;

uniform tex1 sampler2D;
"""
    _darken_blend_mode.fragment_functions = """
float blendDarken(float base, float blend) {
    return min(blend,base);
}

vec3 blendDarken(vec3 base, vec3 blend) {
    return vec3(blendDarken(base.r,blend.r),blendDarken(base.g,blend.g),blendDarken(base.b,blend.b));
}

vec3 blendDarken(vec3 base, vec3 blend, float opacity) {
    return (blendDarken(base, blend) * opacity + base * (1.0 - opacity));
}
"""
    _darken_blend_mode.vertex_shader = """
v_tex_coord = a_tex_coord;
"""
    _darken_blend_mode.fragment_shader = """
vec4 bgcolor = texture2D(tex0, v_tex_coord.st, u_lod_bias);
vec4 maskcolor = texture2D(tex1, v_tex_coord.st, u_lod_bias)
vec3 blended = blendDarken(bgcolor.xyz, maskcolor.xyz, maskcolor.w);
gl_FragColor = vec4(blended, bgcolor.w);
"""
    _darken_blend_mode.register()

    def cc_darken(base, tex, fit=True):
        return Model().child(base, fit=fit).texture(tex).shader(CC_DARKEN_NAME)