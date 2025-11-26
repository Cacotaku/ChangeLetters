import os

from string import printable, punctuation

#function to clean screen
def _apagarTela():
    os.system('cls' if os.name == 'nt' else 'clear')
    pass

#Variable verifying if you want to continue (0 - No)
optionUseProgram = -1

while(optionUseProgram != 0):

    #clean screen
    _apagarTela()

    #index
    I = 0

    #Variable verifying if you want to transform letters to uppercase or lowercase (1 - uppercase | 2 - lowercase)
    optionChangeLetters = 0
       
    #Inserting name to fix
    name = input("Digite o nome:\n")

    #verifying witch option to change letters
    optionChangeLetters = int(input("Deseja transformar o texto em: \n1 - Letras Maiúsculas \n2 - Letras Minúsculas\n")) 

    #transform name into lower case
    name = name.lower()

    #defining names length
    nameLength = len(name)

    #Variable used to fill with fixed characters
    nameFixed = ""

    while(I < nameLength):

        if(name[I] == "ã"):
            nameFixed = nameFixed + "a"

        elif(name[I] == "â"):
            nameFixed = nameFixed + "a"   
        
        elif(name[I] == "á"):
            nameFixed = nameFixed + "a" 

        elif(name[I] == "á"):
            nameFixed = nameFixed + "a"    
        
        elif(name[I] == "ê"):
            nameFixed = nameFixed + "e"
        
        elif(name[I] == "é"):
            nameFixed = nameFixed + "e"

        elif(name[I] == "í"):
            nameFixed = nameFixed + "i"
        
        elif(name[I] == "ó"):
            nameFixed = nameFixed + "o"

        elif(name[I] == "õ"):
            nameFixed = nameFixed + "o"

        elif(name[I] == "ô"):
            nameFixed = nameFixed + "o"

        elif(name[I] == "ú"):
            nameFixed = nameFixed + "u"

        elif(name[I] == "ç"):
            nameFixed = nameFixed + "c"

        elif(name[I] in punctuation ):
            nameFixed = nameFixed    
        
        elif(name[I] not in printable ):
            nameFixed = nameFixed
        
        else:
            nameFixed = nameFixed + name[I]

        I = I + 1

    if(optionChangeLetters == 1):
        #turning name into upper case
        nameUpper = nameFixed.upper()    

        #print name
        print(nameUpper)

    elif(optionChangeLetters == 2):
        #turning name into lower case
        nameLower = nameFixed.lower()

        #print name
        print(nameLower)
    
    else:
        print("Opção incorreta. Selecionar opção válida.")        

    #Verify if you want to continue
    optionUseProgram = int(input("Deseja transformar outro nome?\nSim - 1 | Não - 0\n"))