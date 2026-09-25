from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():

    resultado = ""

    descarte = {
        "plastico": "Plástico deve ser descartado na lixeira vermelha",
        "papel": "Lixeira azul - Folhas, jornais, revistas, cartazes, envelopes, papelão e caixas de papelão.",
        "vidro": "Vidro deve ser descartado na lixeira verde.",
        "metal": "Metal deve ser descartado na lixeira amarela.",
        "residuos eletronicos": "Procure pontos de coleta de resíduos eletroeletrônicos. Não coloque equipamentos eletrônicos no lixo comum.",
        "madeira": "Lixeira preta - Pallets, pedaços de madeira, caixas de madeira e outros resíduos de madeira.",
        "residuos organicos": "Lixeira marrom - Restos de alimentos, cascas de frutas, verduras, legumes, folhas e outros resíduos orgânicos.",
        "materiais medicos": "Procure lixeiras brancas para descartar materiais médicos.",
        "materiais perigosos": "Lixeira laranja - Resíduos que apresentam riscos à saúde ou ao meio ambiente, como alguns produtos químicos e materiais contaminados.",
        "residuos radioativos": "Lixeira roxa - Materiais contaminados ou provenientes de atividades que utilizam materiais radioativos.",
        "rejeitos": "Lixeira cinza - Materiais que não podem ser reciclados ou reaproveitados, como papel higiênico, guardanapos sujos e resíduos contaminados."
    }

    if request.method == "POST":
        material = request.form["material"].lower()
        resultado = descarte.get(material, "material não encontrado.")

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
