from hashlib import new
from regex import F
from sqlalchemy import false, true
def tex_to_list(text_nodes):
    nodes=text_nodes.split(',')
    return nodes
ListAds=[]
for i in range(7500):
    ListAds.append([])
        
ways={}
with open("ways.txt") as f_obj:  
    for line in f_obj:
        k,v_text=line.strip().split('.')
        v=tex_to_list(v_text)
        ways[k.strip()]=v
 #diccionario de nodos       
new_id={}
number_to_index={}
with open("nodes.txt") as f_obj:  
    index=0
    for line in f_obj:
        new_id[line.strip()]=index
        number_to_index[index]=line.strip()
        index+=1
for  way in ways:
   keepFirst=false
   for node in ways[way]:
       current_index= new_id[node]
       if keepFirst==true:
           ListAds[current_index].append(back_index)
           ListAds[back_index].append(current_index)
           back_index=current_index
       if keepFirst==false:
         back_index= new_id[node]
         keepFirst=true
   i+=1    


            
for  lista in  ListAds:
    for i in lista:
       print(f"{number_to_index[i]}") 
    print("------------------------------------")       


    

print("finish")        