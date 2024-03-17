init python:
    from renpy.uguu import GL_FUNC_ADD, GL_MAX, GL_ONE, GL_ONE_MINUS_SRC_ALPHA

    config.gl_blend_func["lighten"] = (GL_MAX, GL_ONE, GL_ONE, GL_FUNC_ADD, GL_ONE, GL_ONE_MINUS_SRC_ALPHA)