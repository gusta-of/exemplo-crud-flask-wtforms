from flask import Flask, render_template, request, redirect, url_for
from app.models.forms import MyForm, VALUES
import os   

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('secret_key')


@app.route("/index/<int:id_entity>", methods=['GET', 'POST'])
def edit(id_entity):
    
    pessoa=''
    if request.method == 'GET':
        for entity in VALUES:
            if entity['id'] == id_entity:
                pessoa=entity['name']
    
    data = {'name': pessoa}
    form = MyForm(**data)

    if form.validate_on_submit():
        for i, entity in enumerate(VALUES):
            print(i, entity)
            if entity['id'] == id_entity:
                VALUES[i]['name'] = form.name.data
        return redirect(url_for('index'))

    return render_template('index.html', form=form, dados=VALUES)

@app.route("/index", methods=['GET', 'POST'])
def index(id=0):

    form = MyForm()
    if form.validate_on_submit():
        
        id = 1
        if not len(VALUES) == 0:
            id = int(VALUES[len(VALUES) -1]['id']) + 1

        print("NOVO", form.name.data)
        VALUES.append(
            {
                'id': id,
                'name': form.name.data 
            }
        ) 

        
        return redirect(url_for('index'))

    return render_template('index.html', form=form, dados=VALUES)
