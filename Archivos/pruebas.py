from graphviz import Digraph
import os
import webbrowser

dot = Digraph()

dot.attr(bgcolor='#15415D')
dot.attr(rankdir='LR', size='8,5')
# 
dot.attr('node', shape='circle', color = 'orange',fillcolor = 'white',style ='filled')
dot.node('S0')

#ID
dot.attr('node', shape='doublecircle', color = 'orange',fillcolor = 'white',style ='filled')
dot.edge('S0', 'S3', label='[a-zA-Z]', color = 'orange', fontcolor="white")
dot.edge('S3', 'S3', label='[a-zA-Z-0-9]', color = 'orange', fontcolor="white")
#Numeros
dot.attr('node', shape='doublecircle', color = 'orange',fillcolor = 'white',style ='filled')
dot.edge('S0', 'S1', label='[0-9]', color = 'orange', fontcolor="white")
dot.edge('S1', 'S2', label='.', color = 'orange', fontcolor="white")
dot.edge('S2', 'S2', label='[0-9]', color = 'orange', fontcolor="white")
# cadenas
dot.attr('node', shape='circle', color = 'orange',fillcolor = 'white',style ='filled')
dot.edge('S0', 'S4', label='"', color = 'orange', fontcolor="white")
dot.edge('S4', 'S4', label='[^"]', color = 'orange', fontcolor="white")
dot.attr('node', shape='doublecircle', color = 'orange',fillcolor = 'white',style ='filled')
dot.edge('S4', 'S5', label='"', color = 'orange', fontcolor="white")
# comentarios
dot.attr('node', shape='circle', color = 'orange',fillcolor = 'white',style ='filled')
dot.edge('S0', 'S6', label='<', color = 'orange', fontcolor="white")
dot.edge('S6', 'S7', label='!', color = 'orange', fontcolor="white")
dot.edge('S7', 'S8', label='-', color = 'orange', fontcolor="white")
dot.edge('S8', 'S9', label='-', color = 'orange', fontcolor="white")
dot.edge('S9', 'S9', label='[^-]', color = 'orange', fontcolor="white")
dot.edge('S9', 'S10', label='-', color = 'orange', fontcolor="white")
dot.edge('S10', 'S11', label='-', color = 'orange', fontcolor="white")
dot.attr('node', shape='doublecircle', color = 'orange',fillcolor = 'white',style ='filled')
dot.edge('S11', 'S12', label='>', color = 'orange', fontcolor="white")


dot.attr('node', shape='doublecircle', color = 'orange',fillcolor = 'white',style ='filled')
dot.edge('S0', 'S113', label='SA', color = 'orange', fontcolor="white")

print(dot.source)
dot.render('test-output/round-table.jpg', view=True)


''' contenido = "socxzcxzcxchimilco"

ruta = os.path.dirname(__file__) + "/nuevo1.html"
archivo = open(ruta,'w')
archivo.write(contenido)

print(os.path.abspath(__file__))
# Esta es la dasnfbdfij
print(os.path.dirname(__file__))  '''
""" webbrowser.open_new_tab(os.path.dirname(__file__) +"/archivo.html") """


v = "/home/sebastian/Escritorio/Destino"