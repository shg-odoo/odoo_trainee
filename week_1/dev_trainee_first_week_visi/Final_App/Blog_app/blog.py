from flask import Flask , render_template , url_for , flash , redirect
from forms import RegistrationForm , LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '3ad5523379e40a00aa399864b8b6373d'
posts = [
    {
        "author"      : "Vishal Sindham",
        "title"       : "Don't reject me i am a learner " ,
        "content"     : "Sometimes a blog is a blog " ,
        "date_posted" : "July 09 2021"

    } ,
    {
        "author"      : "Vishal Sindham",
        "title"       : "Here I am  " ,
        "content"     : "All you have to do here Just give a sign  " ,
        "date_posted" : "July 10 2021"

    }
]

@app.route("/")
@app.route("/home") 
def home():
    return render_template("home.html" , posts=posts )


@app.route("/about")
def about():
    return render_template("about.html" , title="Passed value ")

@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html',title='Login',form=form)


if __name__ == "__main__":
    app.run(debug=True)