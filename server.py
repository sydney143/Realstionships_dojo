from flask import Flask,render_template,request,redirect
from mysqlconnection import connectToMySQL

app = Flask(__name__)

@app.route('/')
def new_dojo():
    mysql= connectToMySQL('dojo')
    new_dojos = mysql.query_db ('SELECT * FROM dojos;')
    print(new_dojos)
    return render_template("dojo.html", all_dojos=new_dojos)

@app.route("/create_dojo", methods=["POST"])
def add_dojo():
    
    query ="INSERT INTO dojos(name, created_at, updated_at) VALUES(%(name)s,NOW(), NOW());"
    data={
            'name': request.form['name']
    }
    mysql= connectToMySQL('dojo')
    mysql.query_db(query,data)
    return redirect("/")


@app.route('/new_ninja')
def new_ninja():
    mysql=connectToMySQL('dojo')
    dojo=mysql.query_db('SELECT * FROM dojos')
    return render_template('new_ninja.html', dojos = dojo)

@app.route('/create_ninja', methods=['POST'])
def create_ninja():
    query ="INSERT INTO ninjas(first_name,last_name,age, created_at, updated_at) VALUES(%(first_name)s,%(last_name)s,%(age)s,NOW(), NOW());"
    data={
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'age': request.form['age']
    }
    mysql=connectToMySQL('dojo')
    dojo=mysql.query_db('SELECT * FROM dojos')
    return redirect("/")


@app.route('/show/<int:dojo_id>')
def show_ninja(dojo_id):

    data = {
        'id': dojo_id
    }

    mysql=connectToMySQL('dojo')
    ninjas=mysql.query_db('SELECT * FROM ninjas JOIN dojos ON ninjas.dojo_id =%(id)s WHERE dojos.id= %(id)s;', data)
    print(ninjas)
    return render_template('dojo_show.html', ninjas=ninjas)


    



if __name__== "__main__":
    app.run(debug=True)