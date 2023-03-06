def Loe_failist(fail:str)->list:
    '''
    '''
    f=open(fail,'r',encoding="utf-8-sig")
    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip()) #По строчно добавляет информацию.
    f.close()
    return jarjend

def Kirjuta_failisse(fail:str,jarjend:list):
    '''
    '''
    f=open(fail,'w',encoding="utf-8-sig")
    for line in jarjend: #Перебираем строчки в списке
        f.write(line+'\n') #Добавляем по строчно в список.
    f.close()
