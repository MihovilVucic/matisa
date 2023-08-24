from app import app, db
from flask import render_template, flash, redirect, Flask, send_from_directory, url_for, request
from app.forms import LoginForm, BackNextForm, RegistrationForm, ResetPasswordRequestForm, ResetPasswordForm
import os
from app.utils import count_lections
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse
from app.email import send_password_reset_email

# Ruta landing stranice
@app.route('/')
def landing():
    return render_template('landing.html', title='Dobrodošli!')

# Ruta početne stranice
@app.route('/index')
@login_required
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Početna')

# Ruta log-in forme, prima i post za formu
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Ako je korisnik već ulogiran, preusmjeri na index
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        #flash('Prijava zatražena za korisnika {}, zapamti_me={} ,avatar={}'
              #.format(form.username.data, form.remember_me.data
                      #,form.avatar.data))
        # Učitaj username iz forme i provjeri postoji li u bazi
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            # Ako ne postoji ili pass nije dobar redirect na login
            flash('Invalid username or password')
            return redirect(url_for('login'))
        # Ako je sve ok, ulogiraj korisnika
        login_user(user, remember=form.remember_me.data)
        #  Preusmjeri ga na početnu stranicu sa koje je došao
        next_page = request.args.get('next')
        # Ako nije došao sa neke druge stranice ili nije sa ove domene, preusmjeri na index
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Prijava', form=form)

# Ruta za logout - automatski se mijenja sa loginom ako je korisnik ulogiran
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# Ruta lekcija - prima id lekcije i prema id-u dinamično odabire lekciju
@app.route('/lekcija/<path:lection_id>', methods=['GET', 'POST'])
@login_required
def lection(lection_id):
    # Konkateniraj path do prave lekcije
    lection_path = os.path.join(app.root_path, 'static', 'lections', lection_id + '.svg')
    
    # Ako lekcija postoji
    if os.path.exists(lection_path):
        # Provjeri postoje li lekcija prije i poslje (za gumbe) i loadaj ju
        total_number_of_lections = count_lections()
        previous_lection_id = int(lection_id) - 1
        next_lection_id = int(lection_id) + 1

        has_previous = previous_lection_id >= 1
        has_next = next_lection_id <= total_number_of_lections
        previous_lection_id_string = str(previous_lection_id)
        next_lection_id_string = str(next_lection_id)

        # Zabilježi lekciju da se korisnik može vratiti
        current_user.last_lession_id = lection_id
        db.session.commit()
        
        return render_template('lection.html', lection_id = lection_id, title = 'Lekcija' + lection_id, has_previous = has_previous,
                               has_next = has_next, previous_lection_id_string = previous_lection_id_string,
                               next_lection_id_string = next_lection_id_string)

    # Vrati 404 error template ako ne postoji lekcija
    return render_template('404.html', title='Lekcija nije pronađena')

# Ruta do menija lekcija
@app.route('/lekcije')
@login_required
def lections():
    return render_template('lection_menu.html', title='Lekcije')

# Ruta do repozitorija "arhiva"
@app.route('/arhiva')
@login_required
def archive():
    return render_template('archive.html', title='Arhiva')

# Ruta do zadataka
@app.route('/zadaci')
@login_required
def exercise():
    return render_template('exercise.html', title='Zadaci')

# Ruta do savjeta
@app.route('/tips')
@login_required
def tips():
    return render_template('tips.html', title='Pro tips')

# Ruta do registracije
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        if form.avatar.data:
            avatar_id = form.avatar.data
        else:
            avatar_id = 0
        user = User(username=form.username.data, email=form.email.data, avatar=form.avatar.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registracija je bila uspješna!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Registracija', form=form)

# Ruta do zahtjeva za pass reset forme
@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Provjerite email za upute')
        return redirect(url_for('login'))
    return render_template('reset_password_request.html',
                           title='Reset Password', form=form)

# Ruta za reset passa
@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Lozinka je resetirana.')
        return redirect(url_for('login'))
    return render_template('reset_password.html', form=form)











    

