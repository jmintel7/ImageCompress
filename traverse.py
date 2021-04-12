import os
import time
import shutil
from image_compress import image_reduce
from video_compress import video_reduce

home = os.path.join(os.path.expanduser('~'),'Pictures')
location = os.path.join(home,'To Upload','Raw')
compressedLocation = os.path.join(home,"To Upload","Compressed")
locationLength = len(location)


#contains a list of files already compressed
doneFile = os.path.join(home,'To Upload')
doneFile = os.path.join(doneFile, 'completed.txt')
doneList = []
if os.path.exists(doneFile):
    with open(doneFile,'r') as fr:
        doneList = fr.read()
        doneList = doneList.split("\n")
# if(os.path.exists(compressedLocation)):
#     shutil.rmtree(compressedLocation)

#to get the list of total files
totalFiles = 0
for subdir, dirs, files in os.walk(location):
    totalFiles += len(files)

count = 0
for subdir, dirs , files in os.walk(location):
    if len(files) == 0:
        continue
    folder = compressedLocation + subdir[locationLength:]
    # print(f"compressed folder: {folder}")
    if not os.path.exists(folder):
        os.makedirs(folder)
    textFile = os.path.join(folder, 'files.txt')
    compFile = os.path.join(folder, 'file_Compression.txt')
    # if os.path.exists(textFile):
    #     os.remove(textFile)
    # if os.path.exists(compFile):
    #     os.remove(compFile)
    print(f"Folder: {subdir}")
    for file in files:
        flag = False
        video = False
        t1 = time.time()
        source = os.path.join(subdir, file)
        destination = os.path.join(folder,file)
        extension = os.path.splitext(source)[1]
        if extension.endswith('.JPG') or extension.endswith('.JPEG'):
            
            if source in doneList:  #if already converted
                pass
            else:
                flag = True
                image_reduce(source, destination)
        elif extension.endswith('.mp4'):
            print(f"\nvideo file: {source}")
            if source in doneList:
                print("Video already converted")
            else:
                video_reduce(source, destination)
                video = flag = True
        else:
            with open(destination,'wb') as fw:
                with open(source,'rb') as fr:
                    other = fr.read()
                fw.write(other)
                flag = True


        t2 = time.time()
        if flag:
            with open(textFile,'a') as fw:
                text1 = f"{file} converted in {round(t2-t1,2)} seconds"
                fw.write(text1+"\n")
            act_size = os.stat(source).st_size
            comp_size = os.stat(destination).st_size
            ratio = (comp_size/act_size) * 100
            with open(compFile,'a') as fw:
                text2 = f"{file} compressed to {int(ratio)}%"
                fw.write(text2)
                text3 = f"Original: {round(act_size/(1024),2)} kB    Compressed: {round(comp_size/(1024),2)} kB"
                text4 = f"Original: {round(act_size/(1024*1024),2)} MB    Compressed: {round(comp_size/(1024*1024),2)} MB"
                if video:
                    fw.write('. '+text4+"\n")
                elif ratio > 40:
                    fw.write('. '+text3+"\n")
                else:
                    fw.write("\n")
            if video:
                print(text1)
                print(text2)
                print(text4)
        count += 1
        prev = 0 if count==1 else prev
        percent = int(count/totalFiles * 100)
        if percent%5 == 0 and prev != percent:
            print(F"{percent}% of files processed")
            prev = percent
            
        if source not in doneList:
            with open(doneFile,"a") as fapp:
                fapp.write(str(source)+"\n")
            
print(f"Total files: {totalFiles}   converted files: {count}")





