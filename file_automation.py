from pathlib import Path

basepath = Path('C:\working_directory')
files_in_basepath = basepath.iterdir()
for item in files_in_basepath:
  if item.is_file():
    print(item.name)