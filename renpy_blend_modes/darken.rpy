init python:
    from renpy.uguu import GL_FUNC_ADD, GL_ONE, GL_ONE_MINUS_SRC_ALPHA, GL_MIN

    config.gl_blend_func["darken"] = (GL_MIN, GL_ONE, GL_ONE, GL_FUNC_ADD, GL_ONE, GL_ONE_MINUS_SRC_ALPHA)