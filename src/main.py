import json
import os
from git import Repo
from pathlib import Path

clone_folder = 'vcpkg'
repo_url = 'https://github.com/microsoft/vcpkg.git'
libraries_filename = 'libraries.json'
clone_path = Path(__file__).parent.absolute().parent.absolute() / clone_folder

if clone_path.exists():
  print('\"' + clone_folder + '\"' + ' folder exists, you have to manually remove it to download the current one.')
  print('Generating ' + '\"' + libraries_filename + '\"' + ' with previously downloaded data.')
  # shutil.rmtree(clone_path)
else:
  print('Cloning repository ' + repo_url)
  Repo.clone_from(repo_url, clone_folder)

ports_path = clone_path / 'ports'
ports_folders = os.listdir(ports_path)

libraries = []

for folder in ports_folders:
  pth = ports_path / folder / 'vcpkg.json'
  file = open(pth, encoding = 'utf8')
  dep_json = json.load(file)
  libraries.append(dep_json)
  file.close()
  dep_json = None
  print(folder)

json_str = json.dumps(libraries, indent = 2)
json_file = open(libraries_filename, 'w', encoding = 'utf8')
json_file.write(json_str)
json_file.close()
