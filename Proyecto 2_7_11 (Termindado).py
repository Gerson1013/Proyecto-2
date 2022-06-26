import json 
print("*****************************************************************\n")
print("Bienvenido agente al Sistema de Suministros de la CIA\n")
print("*****************************************************************\n")
#EL codigo es el codigo de la materia 790
code=str(input("Ingrese el codigo para ingresar al sistema:"))

import os 
flag=True
list_of_provisions=[]
encrypted_list=[]
dictionary={}
flag_two=True
flag_three=True
header=[('ID','Materiales')]
list_no_encrypted=[]
dictionary_no_encrypted={}

#Funciones a utilizar 
################################################################################################
#Funcin de encryption_code
encryption_code={
    
    'q':'z',
    'z':'w',
    'w':'x',
    'x':'e',
    'e':'c',
    'c':'r',
    'r':'v',
    'v':'t',
    't':'b',
    'b':'y',
    'y':'n',
    'n':'u',
    'u':'m',
    'm':'i',
    'i':'k',
    'k':'o',
    'o':'l',
    'l':'p',
    'p':'a',
    'a':'s',
    's':'d',
    'd':'f',
    'f':'g',
    'g':'h',
    'h':'j',
    'j':'q',
}


def encryptador(word):
    new_word = ''
    for letra in  word:
        new_word += encryption_code[letra]
    return new_word    
#####################################################################################################    
#Funcion formato
def wordfill(word, size):
    if len(word) % 2 == 0:
        result = ' ' * int((size - len(word))/2) + word + ' ' * int((size - len(word))/2)
    else:
        result = ' ' * int((size - len(word))/2) + word + ' ' * int((size - len(word))/2) + ' '

    return result 
######################################################################################################    
#Funcion Encabezado     

def function_header(word):
    with open('Suministros.txt', 'w') as file:
        
        for row in header:
            
            str_0 = wordfill((row[0]), 20)
            str_1 = wordfill(row[1], 20)
        
            file.write('|{}|\t{}|\n'.format(str_0, str_1))
            file.write('='*45 + '\n')
######################################################################################################
#Funcion llenado de texto
def function_items(word):
    with open('Suministros.txt', 'a') as file:
        for row in data:
            
            str_0 = wordfill(str(row[0]), 20)
            str_1 = wordfill(row[1], 20)
        
            file.write('|{}|\t{}|\n'.format(str_0, str_1))
            file.write('_'*45 + '\n')

####################################################################################################
#Funcion Inversa



reverse_key = {}
for key, value in encryption_code.items():
    reverse_key[value] = key
    
def desencriptar(word):
    word_no_encrypted = ""
    for l in word:
        word_no_encrypted += reverse_key[l]

    return  word_no_encrypted
#####################################################################################################    

    

if code=="790":
    while flag:
        #El usuario debera llenar al menos 3 materiales para que se despliegue el menu  
        while len(list_of_provisions)<3:
                
            new_item=input("Ingrese un material:") 
            new_item_lower=new_item.lower()

            if len(new_item_lower)<=15:
                
                list_of_provisions.append(new_item_lower)
                flag=False
            if len(new_item_lower)>15:
                flag_three=False
                while not flag_three  :
                    new_item=input("Ingrese un material.:")
                    new_item_lower=new_item.lower()
                    if len(new_item)<=15:
                        
                        list_of_provisions.append(new_item_lower)
                        flag_three=True
                        if len(list_of_provisions)==3:
                            flag=False

                    
    for i in list_of_provisions:
        encryptador(i)
        encrypted_list.append(encryptador(i))  
        
    #Transformar lista en diccionario 
        
        
    a = 1
    for i in encrypted_list:
        dictionary[a] =i
        a = a + 1
    #transformar de diccionario a una lista de tuplas 
    data=list(dictionary.items())
    #Probando si el diccionario funciona 
    print(data)
    
    while flag_two:
        print("--------------------------------------------------------------------------")
        print("Opcion 1: Leer archivo encriptado\n")
        print("Opcion 2:Agregar elemento al inventario\n")
        print("Opcion 3:Eliminar elemento del inventario\n")
        print("Opcion 4:leer elemento elemento encriptado\n")
        print("Opcion 5:Cerrar programa\n")
        print("Opcion 6:Archivo JSON\n")
        print("--------------------------------------------------------------------------\n")

        
        question=(input("ingese la opcion que desea ejecutar:"))
        
        if question=="1":
            
                
            function_header(question)
            function_items(question)
            
            with open("Suministros.txt",'r') as file:
                print(file.read())
                
           
                
                    
                    
        
        if question=="2":
            
            new_item=input("Ingrese un material:") 
            new_item_lower=new_item.lower()

            if len(new_item_lower)<=15:
                
                list_of_provisions.append(new_item_lower)
                flag=False
            if len(new_item_lower)>15:
                flag_three=False
                while not flag_three:
                    new_item=input("Ingrese un material:")
                    new_item_lower=new_item.lower()
                    if len(new_item)<=15:
                        
                        list_of_provisions.append(new_item_lower)
                        flag_three=True  
            dictionary[len(list_of_provisions)]=encryptador(new_item_lower)
            encrypted_list.append(encryptador(new_item_lower))
            data=list(dictionary.items())
            print(data)
            
               
                        
        
    
        if question=="3":
            i_d=int(input("Ingrese el id del elemento que desea eleminar:"))
            
            del(dictionary[i_d])
            
            data=list(dictionary.items())
            
            encrypted_list.pop(i_d-1)
        
        if question=="4":
            
            
            
            for i in encrypted_list:
                list_no_encrypted.append(desencriptar(i))
                
                
                
            print(list_no_encrypted)
            list_no_encrypted.clear()
            
                
                
            
            
        if question=="5":
            
            function_header(question)
            function_items(question)
            
            with open("Suministros.txt","r") as file:
                flag_two=False

                
            print("-##############|EL EQUIPO DETONARA EN 5 SEGUNDOS |###############-")    
                
        if question=="6":
            with open("Suministros.json","w") as file:
                json.dump(data,file)
    
if code!="790":
    print("*****************************************************************\n")
    print("!!!!!!!!!!!!!!!CLAVE ERRONEA!!!!!!!!!!!!!!!\n")
    print("*****************************************************************\n")

    


