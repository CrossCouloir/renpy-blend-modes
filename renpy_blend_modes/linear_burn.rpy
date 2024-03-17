init python:
    CC_LINEAR_BURN_NAME = "crosscouloir.linear_burn"

    _linear_burn_blend_mode = BlendMode(CC_LINEAR_BURN_NAME)

    _linear_burn_blend_mode.vars = """
uniform float u_lod_bias;
uniform sampler2D tex0;
attribute vec2 a_tex_coord;
varying vec2 v_tex_coord;

uniform sampler2D tex1;
"""
    _linear_burn_blend_mode.fragment_functions = """
float blendLinearBurn(float base, float blend) {
    return max(base+blend-1.0,0.0);
}

vec3 blendLinearBurn(vec3 base, vec3 blend) {
    return max(base+blend-vec3(1.0),vec3(0.0));
}

vec3 blendLinearBurn(vec3 base, vec3 blend, float opacity) {
    return (blendLinearBurn(base, blend) * opacity + base * (1.0 - opacity));
}
"""
    _linear_burn_blend_mode.vertex_shader = """
v_tex_coord = a_tex_coord;
"""
    _linear_burn_blend_mode.fragment_shader = """
vec4 bgcolor = texture2D(tex0, v_tex_coord.st, u_lod_bias);
vec4 maskcolor = texture2D(tex1, v_tex_coord.st, u_lod_bias);
vec3 blended = blendLinearBurn(bgcolor.xyz, maskcolor.xyz, maskcolor.w);
gl_FragColor = vec4(blended, bgcolor.w);
"""
    _linear_burn_blend_mode.register()

    def cc_linear_burn(base, tex, fit=True):
        return Model().child(base, fit=fit).texture(tex).shader(CC_LINEAR_BURN_NAME)