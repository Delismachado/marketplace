from flask import Flask, render_template, request
from catalogo import Marketplace, Category, Subcategory, Dados

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

mktplaces = []
result_mktplaces = Dados.get_mktplaces()
for i in result_mktplaces:
    mktplaces.append(Marketplace(i['mktplace']))

categorias = []
result_cat = Dados.get_cat()
for i in result_cat:
    for j in mktplaces:
        if i['mkplace'] == j.get_name():
            categorias.append(Category(i['categoria'], j))

subcategorias = []
result_subcat = Dados.get_subcat()
for i in result_subcat:
    for j in categorias:
        if i['categoria'] == j.get_name():
            subcategorias.append(Subcategory(i['subcategoria'], j))
            break

@app.route('/')
def index():
    return render_template('index.html', mktplaces = mktplaces)

    

@app.route('/category/<mktplaces>')
def category(mktplaces):
    print(mktplaces)
    Dados.log(f'listando marketplaces')
    return render_template('category.html', cat = categorias, mktplaces = mktplaces)

@app.route('/subcategory/<cat>')
def subcategory(cat):
    return render_template('subcategories.html', subcat = subcategorias, cat = cat)

@app.route('/cadastrar_marketplace')
def cadastro_Marketplace():
    msg = ''
    add_mkplace = request.args.get('market')
    if add_mkplace is not None:
        print(add_mkplace)
        add = Dados.set_maktplaces(add_mkplace)
        msg = f'{add_mkplace} cadastrado com sucesso'
        Dados.log(f'resgistro de marketplaces')
    return render_template('cadastro_marketplace.html',menssagem=msg)

@app.route('/cadastrar_categoria')
def cadastro_categoria():    
    pass

@app.route('/cadastrar_subcategoria')
def cadastro_subcategoria():
    pass

app.run(debug=True)