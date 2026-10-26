from flask import Flask
import random

app = Flask(__name__)

facts_list = [
    "Muitas pessoas checam o celular mais de 100 vezes por dia.",
    "Notificações são criadas para prender nossa atenção e nos fazer voltar ao aplicativo.",
    "Usar telas antes de dormir pode atrapalhar a qualidade do sono por causa da luz azul.",
    "A rolagem infinita foi pensada para que a gente nunca encontre um ponto natural de parada.",
    "Fazer pausas regulares longe das telas ajuda a reduzir o cansaço mental e visual.",
    "Desativar notificações desnecessárias é uma das formas mais simples de diminuir a dependência do celular."
]

@app.route("/")
def home():
    return '''
    <h1>Olá! Bem-vindo ao site sobre dependência tecnológica</h1>
    <a href="/random_fact">Veja um fato aleatório!</a><br>
    <a href="/cara_coroa">Jogar cara ou coroa</a><br>
    <a href="/senha">Gerar uma senha</a><br>
    <a href="/charada">Resolver uma charada</a>
    '''

@app.route("/random_fact")
def random_fact():
    return f'<p>{random.choice(facts_list)}</p><a href="/">Voltar</a>'

@app.route("/cara_coroa")
def cara_coroa():
    resultado = random.choice(["Cara", "Coroa"])
    return f'<h1>🪙 {resultado}!</h1><a href="/">Voltar</a>'

@app.route("/senha")
def senha():
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"
    nova_senha = ""
    for i in range(12):
        nova_senha += random.choice(caracteres)
    return f'<h1>🔐 Sua senha: {nova_senha}</h1><a href="/">Voltar</a>'

@app.route("/charada")
def charada():
    return '''
    <div style="text-align:center; font-family:Arial; background:#2b1055; color:white; padding:40px; border-radius:15px;">
        <h1>🧙 Charada</h1>
        <h2>O que é, o que é: tem teclas mas não abre portas?</h2>
        <a href="/resposta" style="color:#ffd700;">Ver resposta</a>
    </div>
    <br><a href="/">Voltar</a>
    '''

@app.route("/resposta")
def resposta():
    return '''
    <div style="text-align:center; font-family:Arial; background:#2b1055; color:white; padding:40px; border-radius:15px;">
        <h1>🎉 Resposta</h1>
        <h2>O teclado!</h2>
        <a href="/charada" style="color:#ffd700;">Voltar para a charada</a>
    </div>
    <br><a href="/">Voltar ao início</a>
    '''

app.run(debug=True)
