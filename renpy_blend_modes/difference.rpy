init python:
    CC_DIFFERENCE_NAME = "crosscouloir.difference"

    _difference_blend_mode = BlendMode(CC_DIFFERENCE_NAME)

    _difference_blend_mode.vars = """
uniform float u_lod_bias;
uniform sampler2D tex0;
attribute vec2 a_tex_coord;
varying vec2 v_tex_coord;

uniform tex1 sampler2D;
"""
    _difference_blend_mode.fragment_functions = """
vec3 blendDifference(vec3 base, vec3 blend) {
    return abs(base-blend);
}

vec3 blendDifference(vec3 base, vec3 blend, float opacity) {
    return (blendDifference(base, blend) * opacity + base * (1.0 - opacity));
}
"""
    _difference_blend_mode.vertex_shader = """
v_tex_coord = a_tex_coord;
"""
    _difference_blend_mode.fragment_shader = """
vec4 bgcolor = texture2D(tex0, v_tex_coord.st, u_lod_bias);
vec4 maskcolor = texture2D(tex1, v_tex_coord.st, u_lod_bias)
vec3 blended = blendDifference(bgcolor.xyz, maskcolor.xyz, maskcolor.w);
gl_FragColor = vec4(blended, bgcolor.w);
"""
    _difference_blend_mode.register()

    def cc_difference(base, tex, fit=True):
        return Model().child(base, fit=fit).texture(tex).shader(CC_DIFFERENCE_NAME)