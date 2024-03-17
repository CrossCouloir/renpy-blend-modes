init python:
    CC_SCREEN_NAME = "crosscouloir.screen"

    _screen_blend_mode = BlendMode(CC_SCREEN_NAME)

    _screen_blend_mode.vars = """
uniform float u_lod_bias;
uniform sampler2D tex0;
attribute vec2 a_tex_coord;
varying vec2 v_tex_coord;

uniform sampler2D tex1;
"""
    _screen_blend_mode.fragment_functions = """
float blendScreen(float base, float blend) {
    return 1.0-((1.0-base)*(1.0-blend));
}

vec3 blendScreen(vec3 base, vec3 blend) {
    return vec3(blendScreen(base.r,blend.r),blendScreen(base.g,blend.g),blendScreen(base.b,blend.b));
}

vec3 blendScreen(vec3 base, vec3 blend, float opacity) {
    return (blendScreen(base, blend) * opacity + base * (1.0 - opacity));
}
"""
    _screen_blend_mode.vertex_shader = """
v_tex_coord = a_tex_coord;
"""
    _screen_blend_mode.fragment_shader = """
vec4 bgcolor = texture2D(tex0, v_tex_coord.st, u_lod_bias);
vec4 maskcolor = texture2D(tex1, v_tex_coord.st, u_lod_bias);
vec3 blended = blendScreen(bgcolor.xyz, maskcolor.xyz, maskcolor.w);
gl_FragColor = vec4(blended, bgcolor.w);
"""
    _screen_blend_mode.register()

    def cc_screen(base, tex, fit=True):
        return Model().child(base, fit=fit).texture(tex).shader(CC_SCREEN_NAME)