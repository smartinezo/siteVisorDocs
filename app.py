from flask import Flask, render_template, request
import array as arr
import os, uuid
from azure.storage.fileshare import ShareServiceClient

app = Flask(__name__)
path_dir_base = 'C:/repositorio'
path_dir_86 = 'C:/repositorio/86'
directorios = os.listdir(path_dir_base)
ficheros = os.listdir(path_dir_86)

@app.route("/")
def index():
    # Obtén la lista de directorios en la ruta "C:/repositorio"

    for dir in directorios:
        path_subdir = path_dir_base + "/" + dir
        contenidoSubDir =  os.listdir(path_subdir)
    
    return render_template("documentacion.html", directorios=directorios)


@app.route('/contenido', methods=['GET', 'POST'])
def contenido():
    dest=""
    if request.method == 'POST':
       dest = request.form('destino')
       path_dir_base = 'C:/repositorio/'+dest
       contenido = os.listdir(path_dir_base)
       return render_template("contenido.html", contenido=contenido, directorios=directorios)
    else :
       dest = request.args.get('destino')
       path_dir_base = 'C:/repositorio/'+dest
       contenido = os.listdir(path_dir_base)
       return render_template("contenido.html", contenido=contenido)
    
    

  

if __name__ == "__main__":
    app.run(debug=True)
