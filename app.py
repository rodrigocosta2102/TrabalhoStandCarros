from flask import Flask, request, render_template, redirect, url_for, flash
from modelscarro import Carro
from persistencia import carregar_carros, gravar_carros
import re

app = Flask(__name__, template_folder='templates')
app.secret_key = "supersecretkey"  # Necessário para flash messages

CARROS_FILE = "carros.txt"

MARCAS_MODELOS = {
    "Mercedes": ["A-Class", "C-Class", "E-Class"],
    "BMW": ["Serie 3", "Serie 5", "Serie 7"],
    "Bugatti": ["Chiron", "Veyron", "La Voiture Noire"],
    "Porsche": ["911", "Cayenne", "Panamera"],
    "Ferrari": ["488 GTB", "Portofino", "F8 Tributo"],
    "Lexus": ["RX", "ES", "LS"]
}

LISTA_CORES = {
    "Preto", "Azul", "Vermelho", "Laranja", "Cinzento", "Branco", "Verde"
}

@app.route('/')
def index():
    lista_carros = carregar_carros(CARROS_FILE)
    total_carros = len(lista_carros)
    total_marcas = len(set(carro.marca for carro in lista_carros))
    total_modelos = len(set(carro.modelo for carro in lista_carros))
    return render_template('index.html', total_carros=total_carros, total_marcas=total_marcas,
                           total_modelos=total_modelos)


@app.route('/carros/', methods=['GET'])
def carros():
    lista_carros = carregar_carros(CARROS_FILE)  # Carregar a lista sempre que a página for acessada
    return render_template('carros.html', carros=lista_carros)


@app.route('/carros/add', methods=['POST'])
def add_carro():
    lista_carros = carregar_carros(CARROS_FILE)  # Carregar os carros antes de adicionar

    marca = request.form['marca'].strip()
    modelo = request.form['modelo'].strip()
    cor = request.form['cor'].strip()
    ano = request.form.get('ano', "").strip()
    preco = request.form.get('preco', "").strip()
    potencia = request.form.get('potencia', "").strip()
    disponibilidade = True if request.form.get('disponibilidade') == 'on' else False
    matricula = request.form['matricula'].strip().upper()

    # Validações
    if not marca or marca not in MARCAS_MODELOS:
        flash('Erro: Marca inválida!', 'error')
        return redirect(url_for('carros'))

    if not modelo or modelo not in MARCAS_MODELOS.get(marca, []):
        flash('Erro: Modelo inválido!', 'error')
        return redirect(url_for('carros'))

    if not cor or cor not in LISTA_CORES:
        flash('Erro: Cor inválida!', 'error')
        return redirect(url_for('carros'))

    try:
        ano = int(ano)
        if ano < 1886 or ano > 2025:
            flash('Erro: Ano inválido!', 'error')
            return redirect(url_for('carros'))
    except ValueError:
        flash('Erro: Ano deve ser um número!', 'error')
        return redirect(url_for('carros'))

    try:
        preco = float(preco)
        if preco <= 0:
            flash('Erro: Preço deve ser maior que 0!', 'error')
            return redirect(url_for('carros'))
    except ValueError:
        flash('Erro: Preço inválido!', 'error')
        return redirect(url_for('carros'))

    try:
        potencia = int(potencia)
        if potencia <= 0:
            flash('Erro: Potência deve ser maior que 0!', 'error')
            return redirect(url_for('carros'))
    except ValueError:
        flash('Erro: Potência inválida!', 'error')
        return redirect(url_for('carros'))

    regex_matricula = r'^[A-Z]{2}-\d{2}-[A-Z]{2}$'
    if not re.match(regex_matricula, matricula):
        flash('Erro: Matrícula inválida! Use o formato AA-00-AA.', 'error')
        return redirect(url_for('carros'))

    if any(carro.matricula == matricula for carro in lista_carros):
        flash('Erro: Matrícula já cadastrada!', 'error')
        return redirect(url_for('carros'))

    novo_carro = Carro(marca, modelo, cor, ano, preco, potencia, disponibilidade, matricula)
    lista_carros.append(novo_carro)
    gravar_carros(CARROS_FILE, lista_carros)

    flash('Carro adicionado com sucesso!', 'success')
    return redirect(url_for('carros'))


@app.route('/carros/remove/<matricula>', methods=['POST'])
def remove_carro(matricula):
    lista_carros = carregar_carros(CARROS_FILE)  # Carregar os carros antes de remover

    # Verifica se o carro existe antes de remover
    carro_existente = any(carro.matricula == matricula for carro in lista_carros)
    if not carro_existente:
        flash('Erro: Carro não encontrado!', 'error')
        return redirect(url_for('carros'))

    lista_carros = [carro for carro in lista_carros if carro.matricula != matricula]
    gravar_carros(CARROS_FILE, lista_carros)

    flash(f'Carro com matrícula {matricula} removido com sucesso!', 'success')
    return redirect(url_for('carros'))


@app.route('/carros/edit/<matricula>', methods=['GET', 'POST'])
def edit_carro(matricula):
    lista_carros = carregar_carros(CARROS_FILE)  # Carregar os carros antes de editar
    carro = next((c for c in lista_carros if c.matricula == matricula), None)

    if not carro:
        flash('Erro: Carro não encontrado!', 'error')
        return redirect(url_for('carros'))

    if request.method == 'POST':
        cor = request.form['cor'].strip()
        ano = request.form.get('ano', "").strip()
        preco = request.form.get('preco', "").strip()
        potencia = request.form.get('potencia', "").strip()
        disponibilidade = True if request.form.get('disponibilidade') == 'on' else False
        nova_matricula = request.form['matricula'].strip().upper()

        #Validações
        if not cor or cor not in LISTA_CORES:
            flash('Erro: Cor inválida!', 'error')
            return redirect(url_for('carros'))

        try:
            ano = int(ano)
            if ano < 1886 or ano > 2025:
                flash('Erro: Ano inválido!', 'error')
                return redirect(url_for('carros'))
        except ValueError:
            flash('Erro: Ano deve ser um número!', 'error')
            return redirect(url_for('carros'))

        try:
            preco = float(preco)
            if preco <= 0:
                flash('Erro: Preço deve ser maior que 0!', 'error')
                return redirect(url_for('carros'))
        except ValueError:
            flash('Erro: Preço inválido!', 'error')
            return redirect(url_for('carros'))

        try:
            potencia = int(potencia)
            if potencia <= 0:
                flash('Erro: Potência deve ser maior que 0!', 'error')
                return redirect(url_for('carros'))
        except ValueError:
            flash('Erro: Potência inválida!', 'error')
            return redirect(url_for('carros'))

        regex_matricula = r'^[A-Z]{2}-\d{2}-[A-Z]{2}$'
        if not re.match(regex_matricula, nova_matricula):
            flash('Erro: Matrícula inválida! Use o formato AA-00-AA.', 'error')
            return redirect(url_for('edit_carro', matricula=carro.matricula))

        #Impede duplicação de matrícula
        if nova_matricula != carro.matricula and any(c.matricula == nova_matricula for c in lista_carros):
            flash('Erro: Já existe um carro com esta matrícula!', 'error')
            return redirect(url_for('edit_carro', matricula=carro.matricula))


        carro.cor = cor
        carro.ano = ano
        carro.preco = preco
        carro.potencia = potencia
        carro.disponibilidade = disponibilidade
        carro.matricula = nova_matricula

        gravar_carros(CARROS_FILE, lista_carros)
        flash('Carro editado com sucesso!', 'success')
        return redirect(url_for('carros'))

    return render_template('edit_carro.html', carro=carro)


if __name__ == '__main__':
    app.run(debug=True)
