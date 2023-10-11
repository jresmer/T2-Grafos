class Vertice:

  def __init__(self, index, label):
    self.__index = index
    self.__label = label

  @property
  def index(self):
    return self.__index

  @property
  def label(self):
    return self.__label

class Graph:

  def __init__(self):
    self.__vertices = set()
    self.__edges = dict()

  # TODO : Implementar função de leitura do arquivo
  def read_file(self, file_name):
    pass

class DiGraph(Graph):

  # TODO : Implementar função de leitura do arquivo
  def read_file(self, file_name):
    pass
