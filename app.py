#importar la libreria flask,redirect
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
 
#Areglo que almacenara la lista 
list = []
 # funcion del controlador 
@app.route("/")
def home():
	return render_template("index.html", list=list)


# se crean los metosos get y post que sirbe para redirigir al controlador agregar
@app.route("/agregar", methods=["GET", "POST"])
def agregar():
	if request.method == "GET":
		return render_template("agregar.html")
	else:
		contac = request.form.get("contac")
		list.append(contac)
		return redirect("/")

#metodo principal
if __name__ == "__main__":
	app.run(debug=True)
