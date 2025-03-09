import os

def generar_arbol_proyecto(ruta, nivel=0, prefijo=''):
    # Obtiene los archivos y carpetas en la ruta
    elementos = os.listdir(ruta)
    
    # Filtra las carpetas .git y .langgraph_api
    elementos = [e for e in elementos if e not in ['.git', '.langgraph_api', '__pycache__']]
    
    for idx, elemento in enumerate(elementos):
        ruta_completa = os.path.join(ruta, elemento)
        
        # Si no es el último elemento, usa la línea con '├──'
        if idx < len(elementos) - 1:
            simbolo = '├──'
            siguiente = '│   '
        else:
            simbolo = '└──'
            siguiente = '    '
        
        # Imprime el nombre del archivo o directorio con el nivel de indentación
        if os.path.isdir(ruta_completa):
            print(f'{prefijo}{simbolo} 📁 {elemento}')
            # Si es un directorio, llama recursivamente a la función
            generar_arbol_proyecto(ruta_completa, nivel + 1, prefijo + siguiente)
        else:
            print(f'{prefijo}{simbolo} 📄 {elemento}')

# Ruta de inicio del proyecto, puedes cambiarla a la ruta que necesites
ruta_inicio = '.'

# Llama a la función para generar el árbol del proyecto
generar_arbol_proyecto(ruta_inicio)
