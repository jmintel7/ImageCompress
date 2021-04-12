import os
doneFile = r"C:\Users\Jis_Mathew\Pictures\To Upload"
doneFile = os.path.join(doneFile, 'completed.txt')
with open(doneFile,'r') as fr:
    file = fr.read()
file=file.split("\n")
print(len(file))
file=list(set(file))
print(len(file))
file = ("\n").join(file)
with open(doneFile,'w') as fw:
    fw.write(file)