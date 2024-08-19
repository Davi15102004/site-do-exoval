from flask import Flask, render_template

app = Flask(__name__)

# Dados dos tapetes por categoria
tapetes = {
    'cozinha': [
        {'nome': 'Tapete de Cozinha A', 'descricao': 'Descrição do Tapete de Cozinha A', 'preco': 'R$ 50,00'},
        {'nome': 'Tapete de Cozinha B', 'descricao': 'Descrição do Tapete de Cozinha B', 'preco': 'R$ 60,00'}
    ],
    'banheiro': [
        {'nome': 'Tapete de Banheiro A', 'descricao': 'Descrição do Tapete de Banheiro A', 'preco': 'R$ 40,00'},
        {'nome': 'Tapete de Banheiro B', 'descricao': 'Descrição do Tapete de Banheiro B', 'preco': 'R$ 45,00'}
    ],
    'estampa': [
        {'nome': 'Tapete Estampado A', 'descricao': 'Descrição do Tapete Estampado A', 'preco': 'R$ 70,00'},
        {'nome': 'Tapete Estampado B', 'descricao': 'Descrição do Tapete Estampado B', 'preco': 'R$ 80,00'}
    ]
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/catalog')
def catalog():
    return render_template('catalog.html')

@app.route('/product/<int:product_id>')
def product(product_id):
    # No futuro, você pode buscar os detalhes do produto de um banco de dados
    return render_template('product.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/categoria/<categoria>')
def categoria(categoria):
    tapetes_categoria = tapetes.get(categoria, [])
    return render_template('categoria.html', tapetes=tapetes_categoria, categoria=categoria)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
