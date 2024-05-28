import os
path_dir_base = 'C:/repositorio'
contenido = os.listdir(path_dir_base)




directorios = []
for dir in contenido:
    path_subdir = path_dir_base + "/" + dir
    contenidoSubDir =  os.listdir(path_subdir)
    for subdir in contenidoSubDir:
        print (subdir)

        