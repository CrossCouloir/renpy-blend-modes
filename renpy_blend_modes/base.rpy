
init python:
  class BlendMode:
    def __init__(self, name,
        vars="",
        vertex_functions="",
        fragment_functions="",
        vertex_shader="",
        fragment_shader=""):
      self.name = name
      self.vars = vars
      self.vertex_functions = vertex_functions
      self.fragment_functions = fragment_functions
      self.vertex_shader = vertex_shader
      self.fragment_shader = fragment_shader
      self._registered = False

    def register(self):
      if not self._registered:
        renpy.register_shader(self.name,
          variables=self.vars,
          vertex_functions=self.vertex_functions,
          fragment_functions=self.fragment_functions,
          vertex_200=self.vertex_shader,
          fragment_200=self.fragment_shader)
        self._registered = True
