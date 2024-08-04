import shutil
import os
from pathlib import Path

path = 'C:\working_directory'
file = os.listdir(path)
print(file)

for item in file:
  name, extension = os.path.splitext(item)
  extension = extension[1:]
  
  if extension=='':
    continue
  
  if os.path.exists(path+'/'+extension): 
    shutil.move(path+'/'+item, path+'/'+extension+'/'+item) 

  else:
    os.makedirs(path +'/'+ extension)
    shutil.move(path +'/'+ item,path +'/'+ extension +'/'+ item)
