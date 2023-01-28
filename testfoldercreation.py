import os
import functools
db = {"":"",'ofxvo': {'name': 'Kai', 'dn': 'Kai [he/him]'}}
            
def read_db(root_dir):
    dact = {}
    root_dir = root_dir.rstrip(os.sep)
    start = root_dir.rfind(os.sep) + 1
    for path, dirs, files in os.walk(root_dir):
        folders = path[start:].split(os.sep)
        subdir = dact.fromkeys(files)
        parent = functools.reduce(dict.get, folders[:-1], dact)
        parent[folders[-1]] = subdir
    dact = dact["db"]
    for folder in dact:
        for file in dact[folder]:
            if dact[folder][file] == None:
                ffile = open("./db/"+folder+"/"+file)
                dact[folder][file] = ffile.read()
                ffile.close()
    return dact
print(read_db("./db"))
