arq_1 = ""
arq_2 = ""
arq_3 = ""
arq_4 = ""

list_file1 = [] # Akamai IPs
list_dup = []

def listdup(entry):
    with open(arq_4, 'a') as dupfile:
        dupfile.write(f"{entry}\n")
        

with open(arq_1, 'r') as file1:
    with open(arq_2, 'r') as file2:
        with open(arq_3, 'w') as outfile:
            for line in set(file1): # file with 209
                a = line.rstrip(' \n')
                list_file1.append(a)

            for line2 in set(file2): # file with 500 IPs
                b = line2.rstrip(' \n')

                if b in list_file1:
                    listdup(b)
                    print(f"IP {b} duplicated")
                else:
                    outfile.write(f"{b}\n")


                