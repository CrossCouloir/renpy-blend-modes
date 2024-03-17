init python:
    CC_EXCLUSION_NAME = "crosscouloir.exclusion"

    _exclusion_blend_mode = BlendMode(CC_EXCLUSION_NAME)

    _exclusion_blend_mode.vars = """
uniform float u_lod_bias;
uniform sampler2D tex0;
attribute vec2 a_tex_coord;
varying vec2 v_tex_coord;

uniform sampler2D tex1;
"""
    _exclusion_blend_mode.fragment_functions = """
vec3 blendExclusion(vec3 base, vec3 blend) {
    return base+blend-2.0*base*blend;
}

vec3 blendExclusion(vec3 base, vec3 blend, float opacity) {
    return (blendExclusion(base, blend) * opacity + base * (1.0 - opacity));
}
"""
    _exclusion_blend_mode.vertex_shader = """
v_tex_coord = a_tex_coord;
"""
    _exclusion_blend_mode.fragment_shader = """
vec4 bgcolor = texture2D(tex0, v_tex_coord.st, u_lod_bias);
vec4 maskcolor = texture2D(tex1, v_tex_coord.st, u_lod_bias);
vec3 blended = blendExclusion(bgcolor.xyz, maskcolor.xyz, maskcolor.w);
gl_FragColor = vec4(blended, bgcolor.w);
"""
    _exclusion_blend_mode.register()

    def cc_exclusion(base, tex, fit=True):
        return Model().child(base, fit=fit).texture(tex).shader(CC_EXCLUSION_NAME)