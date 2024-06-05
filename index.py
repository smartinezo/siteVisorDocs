from flask import Flask, render_template, request
import array as arr
import os, uuid
from azure.storage.fileshare import ShareServiceClient
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


from io import StringIO

app = Flask(__name__)


 
url_base_storage="https://docuvvalley.blob.core.windows.net/doc/"
conn_str = "DefaultEndpointsProtocol=https;AccountName=docuvvalley;AccountKey=GQYEvlBVA61fc2xD86lZY1+4+1f59XuWfNu316t3hiQyxSGO4smNL6n6yub+GhTiYJvIHFMY7CFg+ASt+iXZkQ==;EndpointSuffix=core.windows.net"
blob_service_client = BlobServiceClient.from_connection_string(conn_str)
container_client = blob_service_client.get_container_client('doc')
blob_list = container_client.list_blobs()
lista_directorios = []
lista_dir_arch = [] 
lista_ficheros=[]
url_fichero=""

for blob in blob_list:
    cont=blob.name
    tamano = len(blob.name)
    carpeta=cont[0:cont.find("/")]
    fichero=cont[cont.find("/")+1:tamano]
    if carpeta not in lista_directorios:
        lista_directorios.append(carpeta)
    lista_dir_arch.append([carpeta,fichero,url_base_storage+cont])
# Print the blob names in the container


#sas_url = "https://docuvvalley.blob.core.windows.net/doc?sp=r&st=2024-05-28T08:15:00Z&se=2024-05-28T16:15:00Z&sv=2022-11-02&sr=c&sig=7oQ9p7W0JsVoq8vVKlP6u0BKjplugHmHIWGwo46Imgs%3D"
#blob_client = BlobClient.from_blob_url(sas_url)
#blob_data = blob_client.download_blob()
#df = pd.read_csv(StringIO(blob_data.content_as_text()))
#print(df)

@app.route("/")
def index():
    # Obtén la lista de directorios en la ruta "C:/repositorio"

    return render_template("documentacion.html", lista_directorios=lista_directorios,lista_dir_archivos=lista_dir_arch, blob_list=blob_list, lista_ficheros=lista_ficheros)


@app.route('/contenido', methods=['GET', 'POST'])
def contenido():
    lista_ficheros=[]
    dest=""
    if request.method == 'POST':
       dest = request.form('destino') 
       return render_template("contenido.html",  lista_directorios=lista_directorios,lista_dir_archivos=lista_dir_arch, blob_list=blob_list, lista_ficheros=lista_ficheros)
    else :
        dest = request.args.get('destino')
        for reg in lista_dir_arch:
           if reg[0]==dest:
               lista_ficheros.append(reg[1])
               
       
        return render_template("contenido.html", destino=dest, lista_directorios=lista_directorios,lista_dir_archivos=lista_dir_arch, blob_list=blob_list, lista_ficheros=lista_ficheros)
        return render_template("contenido.html", lista_directorios=lista_directorios,fichlista_dir_archeros=lista_dir_arch, blob_list=blob_list)
    
@app.route('/visor', methods=['GET', 'POST'])
def visor():

       return render_template("contenido.html", lista_directorios=lista_directorios,fichlista_dir_archeros=lista_dir_arch, blob_list=blob_list)
       

  

if __name__ == "__main__":
    app.run(debug=True)
