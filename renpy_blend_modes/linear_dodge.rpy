init python:
    from renpy.uguu import GL_FUNC_ADD, GL_ONE, GL_ONE_MINUS_SRC_ALPHA

    # Add and linear dodge are equivalent
    config.gl_blend_func["linear_dodge"] = (GL_FUNC_ADD, GL_ONE, GL_ONE, GL_FUNC_ADD, GL_ONE, GL_ONE_MINUS_SRC_ALPHA)
    config.gl_blend_func["add"] = (GL_FUNC_ADD, GL_ONE, GL_ONE, GL_FUNC_ADD, GL_ONE, GL_ONE_MINUS_SRC_ALPHA)