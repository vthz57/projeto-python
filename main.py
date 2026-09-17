from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():

    resultado = ""

    if request.method == "POST":

        material = request.form["material"].lower()

        if material == "plastico":
            "Plástico deve ser descartado na lixeira vermelha"

        elif material == "Papel":
            resultado = "Lixeira azul — Folhas, jornais, revistas, cartazes, envelopes, papelão e caixas de papelão."

        elif material == "vidro":
            resultado = "Vidro deve ser descartado na lixeira verde."

        elif material == "metal":
            resultado = "Metal deve ser descartado na lixeira amarela."

        elif material == "residuos eletronicos":
            resultado = "Procure pontos de coleta de resíduos eletroeletrônicos. Não coloque equipamentos eletrônicos no lixo comum."

        elif material == "madeira":
            resultado = "Lixeira preta — Pallets, pedaços de madeira, caixas de madeira e outros resíduos de madeira."

        elif material == "residuos organicos":
            resultado = "Lixeira marrom - Restos de alimentos, cascas de frutas, verduras, legumes, folhas e outros resíduos orgânicos."

        elif material == "materiais medicos":
            resultado = "Procure lixeiras brancas para descartar materiais medicos."

        elif material == "materiais perigosos":
            resultado =  "Lixeira laranja - Resíduos que apresentam riscos à saúde ou ao meio ambiente, como alguns produtos químicos e materiais contaminados."

        elif material == "Resíduos radioativos":
            resultado = "Lixeira roxa - Materiais contaminados ou provenientes de atividades que utilizam materiais radioativos."

        elif material == "rejeitos":
            resultado = "Lixeira cinza - Materiais que não podem ser reciclados ou reaproveitados, como papel higiênico, guardanapos sujos e resíduos contaminados."
            
        else:
            resultado = "Material não encontrado."

    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)

