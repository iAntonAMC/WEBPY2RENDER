import web
import requests


API_URL = "https://gruesome-spooky-coffin-p5765vr65pg29pww-8000.app.github.dev/personsas/"  

# Rutas 
urls = ("/", "Index")

app = web.application(urls, globals())
render = web.template.render("./")

class Index:
	def GET(self):
		response = requests.get(API_URL)
		if response.status_code == 200:
			data = response.json()  
			print("RESPUESTA API:", data)
		else:
			data = []

		return render.index(data)
		
if __name__ == "__main__":
    app.run()
