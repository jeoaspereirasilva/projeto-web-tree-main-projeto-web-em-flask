from app import app
#pular duas linhas por recomendação da pep8

@app.route("/")
def index():
    return "Desenvolvimento Web com Python e Flask"
