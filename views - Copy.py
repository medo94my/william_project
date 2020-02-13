from flask import render_template ,url_for , redirect , flash , request 
from project1 import app , db , bcrypt, Vernam
from project1.forms import RegistrationForm , LoginForm,adminForm , CipherForm ,QuestionForm ,VernamForm, VernamdecryptForm
from project1.Model import User ,Question, Answers
from flask_login import login_user, current_user, logout_user, login_required, LoginManager
import random, math

decryptMessage = " "

@app.route('/' , methods=['GET','POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        password = user.password
        if user and bcrypt.check_password_hash(user.password,form.password.data):
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

@app.route('/Vernam', methods = ['GET', 'POST']) 
@login_required
def vernam():
    global decryptMessage
    form = VernamForm()
    

    x=''
    if request.method == 'POST':
        vernam = Vernam.Vernamencryption
        message = form.message.data
        x ,y = getmessage(message)
        decryptMessage = message
    return render_template('vernam.html', form = form ,x =x )

@app.route('/Vernam2', methods = ['GET', 'POST']) 
@login_required
def Decrypt():
    
    form = VernamdecryptForm()
    if request.method == 'POST':
        global decryptMessage
        message = form.encryptedmessage.data
        x ,y = getmessage(message) 
        decryptMessage = getdecryptmessage(y,message)
        
    return render_template('encryptlayout.html', form = form, decryptMessage=decryptMessage )

def encrypt(message,KEY):
    cipher = ''
    count = 0
    for char in message:
        cipher += chr(ord(char) * ord(KEY[count]))
        count += 1
        if count == len(message):
            count = 0
    return cipher

def getmessage(message):
    message = message
    digits = "0123456789"
    KEY = ''
    for x in range(len(message)):
        KEY += digits[math.floor(random.random()*10)]
    a = encrypt(message, KEY)
    return a, KEY

def decrypt(encryptedmessage, KEY):
    deciphered = ''
    pointer = 0
    
    
    for char in encryptedmessage:
        deciphered += chr(ord(char) // ord(KEY[pointer]))
        pointer += 1
        if pointer == len(encryptedmessage):
            pointer = 0
    global decryptMessage
    deciphered = decryptMessage
    print("Your original message: " + deciphered)
    return deciphered

def getdecryptmessage(KEY,w):
    encryptedmessage = w
    b = decrypt(encryptedmessage, KEY)
    return b

def menu():
    while True:
        response = input("\n\n Vernam Cipher \n\n [cipher] to cipher \n [decrypt] to decrypt \n\n" )
        if response == "cipher":
            a, KEY = getmessage()
        elif response == "decrypt":
            getdecryptmessage(KEY)
        



    

@app.route('/resources')
@login_required
def resources():
    return render_template('resource.html')

@app.route('/Questionnaire' , methods = ['GET', 'POST'])
@login_required
def questionnaire():
    data=Question.query.all()
    form = QuestionForm()
    if form.validate_on_submit():
        answer = form.answer.data
        answer2 = form.answer2.data
        answer3 = form.answer3.data
        answer4= form.answer4.data
        answer5 = form.answer5.data
        by=current_user.id
        question = request.form['id_mf']
        answerlist=[]

        ans = Answers(q_id=question , Answers1 = answer, Answers2 = answer2, Answers3 = answer3, Answers4 = answer4, Answers5 = answer5
         , Submitted_by =by)
        db.session.add(ans)
        db.session.commit()
        flash('Your Answer has been submitted!', 'success')
        return redirect(url_for('login'))
    else:
        print(form.errors)
    return render_template('question.html', form = form, data=data)

@app.route('/admin',methods=['GET','POST'])
def admin():
    form = adminForm()
    if form.validate_on_submit():
        admin =  form.admin.data
        password = form.password.data
        if admin=='admin' and password =='admin':
           

            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('Dashboard'))
            flash('You are logged in', 'success')
            return redirect(url_for('Dashboard'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('admin/admin_login.html',form=form)

@app.route('/Dashboard')
def Dashboard():
    return render_template('admin/index.html')
@app.route('/Dashboard/ui')
def ui():
    data=Answers.query.all()
    return render_template('admin/ui.html', data=data)


@app.route('/Dashboard/user-recorded')
def blank():
    data=User.query.all()
    return render_template('admin/blank.html',data=data)


@app.route('/logout')
def logout():
    logout_user()
    return render_template('index.html')

