new_id={}
x=0
with open("nodes.txt") as f_obj:  
    for line in f_obj:
        new_id[line.strip()]=x
        x+=1


for x in  new_id:
    print(f"{x}: ", new_id[x])

            
