from flask import Flask, render_template, redirect, url_for
from webapp.model import db, User
from webapp.forms import LoginForm
from webapp.config import Config
from webapp.test_grab import grab

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        title = 'From py-web to TD'

        form_login = LoginForm()
        
        if form_login.validate_on_submit():
            user_name = form_login.username.data
            user_exist = User.query.filter(User.login == user_name).count()
            if not user_exist:
                new_user = User(login=user_name)
                db.session.add(new_user)
                db.session.commit()

            return redirect(url_for('session', login=user_name))

        return render_template('index.html', page_title=title, form=form_login)


    @app.route('/grab_data')
    def grab_data():
        grab()
        #print (f"grab data with ")
        return ("nothing")

    @app.route('/grab_data_stop')
    def grab_data_stop():
        print ("stop gtab data")
        return ("nothing")

    @app.route('/finish')
    def goodbye():
        return render_template('finish.html')

    @app.route('/session/<login>')
    def session(login):
        return render_template('session.html', name=login)

    @app.route('/grab')
    def grab():
        return render_template('grab.html')


    return app