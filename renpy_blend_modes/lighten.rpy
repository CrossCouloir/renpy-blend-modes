init python:
    CC_LIGHTEN_NAME = "crosscouloir.lighten"

    _lighten_blend_mode = BlendMode(CC_LIGHTEN_NAME)

    _lighten_blend_mode.vars = """
uniform float u_lod_bias;
uniform sampler2D tex0;
attribute vec2 a_tex_coord;
varying vec2 v_tex_coord;

uniform tex1 sampler2D;
"""
    _lighten_blend_mode.fragment_functions = """
float blendLighten(float base, float blend) {
    return max(blend,base);
}

vec3 blendLighten(vec3 base, vec3 blend) {
    return vec3(blendLighten(base.r,blend.r),blendLighten(base.g,blend.g),blendLighten(base.b,blend.b));
}

vec3 blendLighten(vec3 base, vec3 blend, float opacity) {
    return (blendLighten(base, blend) * opacity + base * (1.0 - opacity));
}
"""
    _lighten_blend_mode.vertex_shader = """
v_tex_coord = a_tex_coord;
"""
    _lighten_blend_mode.fragment_shader = """
vec4 bgcolor = texture2D(tex0, v_tex_coord.st, u_lod_bias);
vec4 maskcolor = texture2D(tex1, v_tex_coord.st, u_lod_bias)
vec3 blended = blendLighten(bgcolor.xyz, maskcolor.xyz, maskcolor.w);
gl_FragColor = vec4(blended, bgcolor.w);
"""
    _lighten_blend_mode.register()

    def cc_lighten(base, tex, fit=True):
        return Model().child(base, fit=fit).texture(tex).shader(CC_LIGHTEN_NAME)