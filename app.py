from flask import Flask, render_template, request
import openai
from sexpert import *
from decouple import config

app = Flask(__name__)
openai.api_key = config("API_KEY")
print(config("API_KEY"))

@app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        return render_template('index.html')


@app.route('/diagnostico', methods=['GET', 'POST'])
def diagn():
    lista_sintomas.clear()
    if request.method == 'GET':
        return render_template('prediagnostico.html')
    if request.method == 'POST':
        for i in range(1, 55):
            if request.form.get("sintoma"+str(i)): lista_sintomas.append(request.form["sintoma"+str(i)])
        if (len(lista_sintomas) > 0):
            #genero el diagnostico de la enfermedad segun los sintomas
            creacionMapaSintomas()
            motor= diagnostico()
            motor.reset()
            motor.run()
            #primer llamado a openAI para el tratamiento
            question = 'Yo: Dime un tratamiento de 300 palabras para '+motor.enf
            response = openai.Completion.create(
                engine = 'text-davinci-003',
                prompt = question,
                temperature = 0.5,
                max_tokens = 1000,
                top_p = 1,
                frequency_penalty = 0,
                presence_penalty = 0.6
            )
            tratamiento = response.choices[0].text.strip()
            question = 'Yo: Dime una definicion de '+motor.enf+' de 150 palabras'
            response = openai.Completion.create(
                engine = 'text-davinci-003',
                prompt = question,
                temperature = 0.5,
                max_tokens = 1000,
                top_p = 1,
                frequency_penalty = 0,
                presence_penalty = 0.6
            )
            definicion = response.choices[0].text.strip()
            return render_template('resultado.html', tratamiento=tratamiento, definicion=definicion, enfermedad= motor.enf, confianza=motor.confianza)
        else:
            return render_template('default.html')
    

if __name__ == '__main__':
    app.run(debug=True, port=config("PORT"))