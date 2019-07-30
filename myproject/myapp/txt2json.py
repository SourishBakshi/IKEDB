json_file=open("C:/Python27/myproject/myapp/kedb.json",'w')
json_file.write("[")
i=0
with open("C:/Python27/myproject/myapp/KEDB.txt","r") as f:
        for line in f:
            if i!=0:
                json_file.write(',')
            json_file.write('{"name": "'+line[:-1]+'"}')
            i=i+1
json_file.write(']')
f.close()
json_file.close()