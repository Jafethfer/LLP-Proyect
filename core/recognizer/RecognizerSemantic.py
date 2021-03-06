# -*- coding: utf-8 -*-

import re
from ..lark import Transformer, v_args, Tree


@v_args(inline=True)
class RecognizerSemantic(Transformer):
    def __init__(self):
        self.variables = {}
        self.functions = {}

    def createfunction(self, name, params, instructions, end):
        #? Para saber cuantos parametros se definen en la funcion
        if isinstance(params,Tree):
            value = len(params.children)
        else: value = 1

        self.functions[name] = value
        
    def callfunction(self, name, params):
        if name in self.functions:
            if isinstance(params, Tree):
                if self.functions[name] == len(params.children):
                    pass
            elif self.functions[name] == 1:
                pass
            else:
                raise Exception("faltan parametros")
        else:
            raise Exception("No existe la funcion")

    def sum(self,A,B):

        pass#return float(A) + float(B) 

    def sub(self,A,B):

        pass#return float(A) + float(B)

    def mul(self,A,B):

        pass#return float(A) * float(B)

    def div(self,A,B):

        pass#return float(A) / float(B)

    def mod(self,A,B):

        pass#return float(A) % float(B)

    def assignvar(self,name,value):

        self.variables[name] = value

    def getvar(self,name):

        pass#return self.variables[name]   

    def print(self,param):
        pass#print("%s" % self.cleanParam(param))

    def printvar(self,name):

        pass#print("%s" % self.getvar(name))

    def cleanParam(self,param):

        if re.match(r"^(\"[^\"]*\")|('[^']*'))$",param):

            return param[1:-1]
            return param                        


