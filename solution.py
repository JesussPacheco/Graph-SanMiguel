def tex_to_list(text_nodes):
    nodes=text_nodes.split(',')
    return nodes
ways={}
with open("ways.txt") as f_obj:  
    for line in f_obj:
        k,v_text=line.strip().split('.')
        v=tex_to_list(v_text)
        ways[k.strip()]=v
#print(ways['27455207'])  
    #for calle in ways:
     #   print(calle) 
prueba={1:[123,41234],2:[8612,145,444],8:[999,88,33]}
for i in ways:
    print(f"{i} : {ways[i]}")
     