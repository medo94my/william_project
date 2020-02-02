from flask import render_template ,url_for , redirect , flash , request 
    from project1 import app , db , bcrypt
from project1.forms import RegistrationForm , LoginForm , CipherForm
from project1.Model import User
from flask_login import login_user, current_user, logout_user, login_required, LoginManager




@app.route('/' , methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        password = user.password
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            # session['logged_in'] = True
            # session['name'] = user.name
            login_user(user, remember = form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
            flash('You are logged in', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('home.html', title='Login', form=form)

@app.route('/register', methods = ['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(name = name , email = email , password = password_hash)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    else:
        print('wrong')
    return render_template('registration.html',form = form)

@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/cipher', methods = ['GET', 'POST']) 
@login_required
def cipher():
    form = CipherForm()
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher = ''
    if request.method == 'POST':
        shift = form.shift.data
        message = form.message.data
        for x in message:
            if x in alphabet:
                cipher += alphabet[(alphabet.index(x)+int(shift))%(len(alphabet))]
        
    
    return render_template('cipher.html', form = form , cipher = cipher)

@app.route('/revision notes')
@login_required
def guide():
    return render_template('guide.html')

@app.route('/admin')
def admin():
    return 'admin'


@app.route('/logout')
def logout():
    logout_user()
    return render_template('index.html')

