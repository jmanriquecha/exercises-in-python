print('*** Alcance de las variables ***')

# Variable global
contador_global = 0

# 
def incrementar_contador():
    # Declaramos variable local
    contador_local = 0
    
    # Usar la variable global
    global contador_global
    
    # Incrementamos variable global
    contador_global += 1
    
    # Incrementamos variable local
    contador_local += 1

    # Imprimimos contadores
    print(f'Contador local: {contador_local}, Contador global: {contador_global}\n')
    
    
# Llamamos varias veces funcion   
incrementar_contador()
incrementar_contador()
incrementar_contador()
    
    

incrementar_contador