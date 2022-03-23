from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy  # add
from datetime import datetime  # add

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # add
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)  # add

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.name


#######  Crud  ########

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        new_user = User(name=name)

        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect('/')
        except:
            return "There was a problem adding new user."

    else:
        users = User.query.order_by(User.created_at).all()
        return render_template('index.html', users=users)

@app.route('/delete/<int:id>')
def delete(id):
    user = User.query.get_or_404(id)

    try:
        db.session.delete(user)
        db.session.commit()
        return redirect('/')
    except:
        return "There was a problem deleting data."

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    user = User.query.get_or_404(id)

    if request.method == 'POST':
        user.name = request.form['name']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return "There was a problem updating data."

    else:
        title = "Update Data"
        return render_template('update.html', title=title, user=user)


if __name__ == '__main__':
    app.run(debug=True)