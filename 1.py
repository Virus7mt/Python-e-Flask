# Flasky e um framework de python - desenvolvimento de sites e API

# instalou uma biblioteca e está importando o flasky dentro da biblioteca
# A função render_template serve para o Flask ler um arquivo HTML externo e enviá-lo pronto para o navegador do usuário
from flask import Flask, render_template

# serve para criar o "coração" do seu site. É ela quem inicializa a sua aplicação web 
app = Flask(__name__)

# criar a 1° pagina no site

# route - Qual link vai ficar a página(meusite.com/)
# serve para criar um endereço (uma página) no site
# função - Oque você quer exibir na página
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html",nome_usuario=nome_usuario)

# colocar o site no ar

# serve para garantir que o seu site só vai começar a rodar se você executar este arquivo diretamente
if __name__ == "__main__":

# debug=True atualiza o site a cada mudança no código, automáticamente
    app.run(debug=True)