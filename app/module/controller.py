from flask import (make_response, render_template, request, session,
                    redirect, url_for, flash, abort, logging)
from app import app
from wtforms import Form, BooleanField, StringField, TextAreaField, PasswordField, validators
from wtforms.validators import InputRequired, Email, Length
from .models import mysql, MySQLdb
from flask_uploads import UploadSet, configure_uploads, IMAGES
# from werkzeug.utils import secure_filename
# from werkzeug.datastructures import  FileStorage
import os
from passlib.hash import sha256_crypt
from functools import wraps
from lockfile import LockFile
import timeit
import datetime
import stripe
import locale
# from .data import Articles
# article = Articles()

# app.config['SERVER_NAME'] = 'localhost:5000'
app.secret_key = os.urandom(24)
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['UPLOADED_PHOTOS_DEST'] = 'app/static/image/product'
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

pub_key = 'pk_test_CtG1FPd25LngxMhmPJN8ZMN2'
secret_key = 'sk_test_ff9IHNRghmcBnbiLUmp4fLnn'
stripe.api_key = secret_key

# Visitor
# counter = 1

# # CEK USER ADA GAK
# def get_user_id(username):
#   rv = query_db('select id from users where username = ?',
#                 [username], one=True)
#   return rv[0] if rv else None



# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('未经授权，请登录', 'danger')
            return redirect(url_for('login'))
    return wrap

def not_admin_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'admin_logged_in' in session:
            return f(*args, *kwargs)
        else:
            return redirect(url_for('user'))

    return wrap

def wrappers(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)

    return wrapped


def content_based_filtering(id_phone):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM product_phone WHERE id_phone=%s", (id_phone,))  # getting id row
    data = cur.fetchone()  # get row info
    data_cat = data['brand']  # get id category ex shirt
    print('Showing result for Product Id: ' + id_phone)
    category_matched = cur.execute("SELECT * FROM product_phone WHERE brand=%s", (data_cat,))  # get all shirt category
    print('Total product matched: ' + str(category_matched))
    cat_product = cur.fetchall()  # get all row
    cur.execute("SELECT * FROM product_phone_level WHERE id_level=%s", (id_phone,))  # id level info
    id_level = cur.fetchone()
    recommend_id = []
    cate_level = ['colors', 'camera', 'internal', 'network', 'battery', 'announced', 'status', 'dimensions', 'weight', 'size',
                  'resolution']
    for product_f in cat_product:
        cur.execute("SELECT * FROM product_phone_level WHERE id_phone=%s", (product_f['id_phone'],))
        f_level = cur.fetchone()
        print('found f_level : ' + str(f_level['id_phone']))
        print('found id_phone : ' + str(id_phone))


        match_score = 0
        if f_level['id_phone'] != int(id_phone):
            for cat_level in cate_level:
                if f_level[cat_level] == id_level[cat_level]:
                    match_score += 1
            if match_score == 11:
                recommend_id.append(f_level['id_phone'])
    print('Total recommendation found: ' + str(recommend_id))
    if recommend_id:
        cur = mysql.connection.cursor()
        placeholders = ','.join((str(n) for n in recommend_id))
        query = 'SELECT * FROM product_phone WHERE id_phone IN (%s)' % placeholders
        cur.execute(query)
        recommend_list = cur.fetchall()
        return recommend_list, recommend_id, category_matched, id_phone
    else:
        return ''

def addcart():
    cur = mysql.connection.cursor()
    if 'uid' not in session:
        carts= 0
    else:
       uid = session['uid']
       cur.execute("SELECT COUNT(*) FROM cart WHERE id_users = " + str(uid) +";")
       # cur.fetchone() return a dict with a single key:value pair
       carts =  [v for v in cur.fetchone().values()][0]
    return carts

def OrdersQueue():
    cur = mysql.connection.cursor()
    if 'uid' not in session:
        orders= 0
    else:
       cur.execute("SELECT COUNT(*) FROM orders WHERE status = 'check' ")
       # cur.fetchone() return a dict with a single key:value pair
       orders =  [v for v in cur.fetchone().values()][0]
    return orders

# Articles search TESTING
@app.route('/article/search', methods=['POST', 'GET'])
def search_article():
    # form = OrderForm(request.form)
    if 'q' in request.args:
        q = request.args['q']
        # Create cursor
        cur = mysql.connection.cursor()
        # Get message
        query_string = "SELECT * FROM articles WHERE title LIKE %s"
        result = cur.execute(query_string, ('%' + q + '%',))
        if result > 0:
            articles = cur.fetchall()
            flash('Showing result for: ' + q, 'success')
            return render_template('search_result.html', articles=articles)
        else:
            abort(404)
        # Close Connection
        cur.close()
    else:
        error = '再次搜索'
        return render_template('search.html', error=error)

def visitors():
    lock = LockFile("app/module/visitors.txt")
    with lock:
        with open("app/module/visitors.txt", "r+") as f:
            fileContent = f.read()
            if fileContent == "":
                count = 1
            else:
                count = int(fileContent) + 1
            f.seek(0)
            f.write(str(count))
            f.truncate()
            return (count)


@app.route('/products/search', methods=['POST', 'GET'])
def search_product():
    # form = OrderForm(request.form)
    noOfItems = addcart()
    order = OrdersQueue()
    if 'q' in request.args:
        q = request.args['q']
        # Create cursor
        cur = mysql.connection.cursor()
        # Get message SELECT * FROM product_phone ORDER BY id_phone DESC "
        query_string = "SELECT * FROM product_phone WHERE phone LIKE %s"
        result = cur.execute(query_string, ('%' + q + '%',))
        curso = mysql.connection.cursor()
        curso.execute("SELECT brand FROM product_phone GROUP BY brand")
        brandNav = curso.fetchall()
        if result > 0:
            product = cur.fetchall()
            info = '显示结果: ' + q
            return render_template('view_search_product.html',order=order, brandNav=brandNav, info=info, product=product, noOfItems=noOfItems)
        else:
            info = '搜索不可用: ' + q
            return render_template('view_search_product.html',order=order, brandNav=brandNav, info=info, noOfItems=noOfItems)
        # Close Connection
        cur.close()
    else:
        return redirect(url_for('index'))
        # error = 'Search again'
        # return render_template('search.html', error=error)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM product_phone ORDER BY RAND() LIMIT 4")
    product = cur.fetchall()
    cur.execute("SELECT brand,id_phone,picture FROM product_phone GROUP BY brand ORDER BY RAND() LIMIT 3")
    brand = cur.fetchall()

    cur.execute("SELECT * FROM articles ORDER BY create_date DESC Limit 2")
    articles = cur.fetchall()

    cur.execute("SELECT * FROM admin_address")
    footer = cur.fetchone()
    # count = visitors()
    noOfItems = addcart()
    order = OrdersQueue()
    cur.close()

    return render_template("index.html", order=order, articles=articles, brand=brand, product=product, noOfItems=noOfItems, footer=footer)

# @app.route('/article/<int>/')
# def article_int(int):
#     return redirect(url_for('article', article = int))

@app.route('/article/', defaults={'title' : 0})
@app.route('/article/<path:title>')
def article(title):
    noOfItems = addcart()
    order = OrdersQueue()
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM articles WHERE title = %s", [title])
    article = cur.fetchone()
    curso = mysql.connection.cursor()
    curso.execute("SELECT title, id FROM articles ORDER BY RAND() LIMIT 5")
    artNav = curso.fetchall()
    cur.close()
    return render_template('article.html',order=order, article=article, artNav=artNav, noOfItems=noOfItems)

# @app.route('/comment',  methods=['POST', 'GET'])
# @is_logged_in
# def comment():
#     if request.method == 'POST':
#         uid = session['uid']
#         comment = request.form['comment']
#         idart = request.form['idart']
#         cur = mysql.connection.cursor()
#         print(idart)
#         cur.execute("INSERT INTO comment(id_articles, id_user, content_c) VALUES(%s, %s, %s)", (idart, uid, comment))
#         mysql.connection.commit()
#     return ''


@app.route('/orders')
@is_logged_in
@not_admin_logged_in
def orders_confirm():
    order = OrdersQueue()
    if 'confirm' in request.args:
        id_users = request.args['confirm']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO orders_receipt(id_orders, id_phone, id_users, username, phone, price) SELECT id_orders, id_phone, id_users, username, phone, price FROM orders WHERE status='check' AND id_users =" + str(id_users))
        cur.execute("UPDATE orders SET status=%s WHERE id_users=%s AND status='check'",('confirm', id_users))
        mysql.connection.commit()
        return redirect(url_for('dashboard'))
    if 'shipping' in request.args:
        id_users = request.args['shipping']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM orders WHERE id_users=%s AND status='check'", (id_users,))
        orders = cur.fetchall()
        totalP = 0
        for ord in orders:
            d = ord['date'].strftime("%d-%b-%Y")
            o = ord['id_orders']
            u = ord['id_users']
            totalP += ord['price']
            locale.setlocale( locale.LC_ALL, '' )
            totalPrice = locale.format("%.2f", totalP, 1)
        # cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE id=%s", (id_users,))
        users = cur.fetchone()
        cur.execute("SELECT * FROM admin_address")
        address = cur.fetchone()
        return render_template('pages/admin_shipping_order.html',order=order, address=address, d=d, o=o,u=u,users=users,totalPrice=totalPrice, orders=orders)
    if 'print' in request.args:
        id_users = request.args['print']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM orders WHERE id_users=%s AND status='check'", (id_users,))
        orders = cur.fetchall()
        totalP = 0
        for ord in orders:
            d = ord['date'].strftime("%d-%b-%Y")
            o = ord['id_orders']
            u = ord['id_users']
            totalP += ord['price']
            locale.setlocale( locale.LC_ALL, '' )
            totalPrice = locale.format("%.2f", totalP, 1)
        # cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE id=%s", (id_users,))
        users = cur.fetchone()
        cur.execute("SELECT * FROM admin_address")
        address = cur.fetchone()
        return render_template('pages/print.html',address=address, d=d, o=o,u=u,users=users,totalPrice=totalPrice, orders=orders)
    else:
        return redirect(url_for('dashboard'))


class SettingAdminForm(Form):
    username = StringField('用户名', [validators.length(min=3, max=50)],
                       render_kw={'autofocus': True, 'placeholder': '用户名'})
    email = StringField('电子邮件', [validators.DataRequired(), validators.Email(), validators.length(min=4, max=25)],
                       render_kw={'placeholder': '电子邮件'})
    telp = StringField('手机号码', [validators.DataRequired()])
    password = PasswordField('新密码', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message=' - 密码不匹配'),
        validators.Length(min=5, max=20, message=' - 最少5个字符')
    ])
    confirm = PasswordField('重复新密码')
    accept_tos = BooleanField(' ', [validators.DataRequired()])

@app.route('/datausers',  methods=['POST', 'GET'])
@is_logged_in
@not_admin_logged_in
def datausers():
    order = OrdersQueue()
    form = SettingAdminForm(request.form)
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    if 'edit' in request.args:
        id = request.args['edit']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM users WHERE id=%s", (id,))
        result = curso.fetchone()
        if request.method == 'POST':
            username = form.username.data
            email = form.email.data
            telp = form.telp.data
            cur = mysql.connection.cursor()
            exe = cur.execute("UPDATE users SET username=%s, email=%s, phonenumber=%s WHERE id=%s", (username, email, telp, id))
            mysql.connection.commit()
            cur.close()
            if exe:
                flash('资料已更新', 'success')
                return redirect(url_for('datausers'))
            else:
                flash('更新', 'success')
                return redirect(url_for('datausers'))
        return render_template('pages/admin_adminuser_edit.html', order=order, result=result, form=form)
    if 'password' in request.args:
        id = request.args['password']
        if request.method == 'POST':
            password = sha256_crypt.encrypt(str(form.password.data))
            cur = mysql.connection.cursor()
            exe = cur.execute("UPDATE users SET password=%s WHERE id=%s", (password, id))
            mysql.connection.commit()
            cur.close()
            if exe:
                flash('资料更新', 'success')
                return redirect(url_for('datausers'))
            else:
                flash('更新', 'success')
                return redirect(url_for('datausers'))
        return render_template('pages/admin_adminuser_edit.html',order=order, form=form)
    else:
        return render_template("pages/admin_data_users.html",order=order, users=users)


class SettingAddUsers(Form):
    username = StringField('用户名', [InputRequired(), validators.Length(min=5, max=20, message=' - 最少5个字符和最多20个字符')])
    email = StringField('电子邮件', [InputRequired(),
        Email(message=' - Invalid Email')])
    password = PasswordField('密码', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message=' - 密码不匹配'),
        validators.Length(min=5, max=20, message=' - 最少5个字符')
    ])
    confirm = PasswordField('重复输入密码')
    accept_tos = BooleanField(' ', [validators.DataRequired()])

@app.route('/addusers',  methods=['POST', 'GET'])
@is_logged_in
@not_admin_logged_in
def addusers():
    order = OrdersQueue()
    form = SettingAddUsers(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(str(form.password.data))

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(type, username, email, password) VALUES(%s, %s, %s, %s)", ('1', username, email, password))
        mysql.connection.commit()
        cur.close()

        flash('管理员添加了', 'success' )
        return redirect(url_for('datausers'))
    return render_template('pages/admin_add_users.html',order=order, form=form)


@app.route('/datasales')
@is_logged_in
@not_admin_logged_in
def datasales():
    order = OrdersQueue()
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM orders_receipt")
    orders = cur.fetchall()
    cur.execute("SELECT * FROM payment")
    pay = cur.fetchall()
    if 'print' in request.args:
        id_users = request.args['print']
        cur.execute("SELECT * FROM orders_receipt WHERE id_users=%s", (id_users,))
        print = cur.fetchall()
        totalP = 0
        for ord in print:
            d = ord['date'].strftime("%d-%b-%Y")
            o = ord['id_orders']
            u = ord['id_users']
            totalP += ord['price']
            locale.setlocale( locale.LC_ALL, '' )
            totalPrice = locale.format("%.2f", totalP, 1)
        # cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE id=%s", (id_users,))
        users = cur.fetchone()
        cur.execute("SELECT * FROM admin_address")
        address = cur.fetchone()
        return render_template("pages/printdatasales.html", pay=pay, order=order, address=address, d=d, o=o,u=u,users=users,totalPrice=totalPrice, print=print)
    return render_template('pages/admin_datasales.html', pay=pay, order=order, orders=orders)

@app.route('/dashboard')
@is_logged_in
def dashboard():
    if session['type'] == 1:
        order = OrdersQueue()
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM orders")
        orders = cur.fetchall()
        cur.execute("SELECT * FROM admin_address")
        adr = cur.fetchone()
        return render_template("pages/dashboard.html", adr=adr, orders=orders, order=order)
    else:
        return redirect(url_for('user', username=session['username']))

@app.route('/user/', defaults={'username' : 0})
@app.route('/user/<string:username>')
@is_logged_in
def user(username):
    if session['type'] == 0:
        noOfItems = addcart()
        uid = session['uid']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM orders WHERE id_users=%s", (uid,))
        orders = cur.fetchall()
        d = '--/--/----'
        totalPrice = 0
        totalP = 0
        cn = ''
        for row in orders:
            d = row['date'].strftime("%d-%b-%Y")
            cn = row['status']
            totalP += row['price']
            locale.setlocale( locale.LC_ALL, '' )
            totalPrice = locale.format("%.2f", totalP, 1)
        cur.execute("SELECT COUNT(*) FROM orders WHERE id_users = " + str(uid) +";")
        o =  [v for v in cur.fetchone().values()][0]
        if 'cancel' in request.args:
            cancel = request.args['cancel']
            cur.execute("UPDATE orders SET status=%s WHERE id_orders=%s",('cancel', cancel))
            mysql.connection.commit()
            return redirect(url_for('user'))
        if 'delete' in request.args:
            delete = request.args['delete']
            cur.execute("DELETE FROM orders WHERE id_orders = " + str(delete))
            mysql.connection.commit()
            return redirect(url_for('user'))
        if 'confirm' in request.args:
            confirm = request.args['confirm']
            cur.execute("UPDATE orders_receipt SET status=%s WHERE id_users=%s",('confirm', confirm))
            cur.execute("DELETE FROM orders WHERE id_users = " + str(confirm))
            mysql.connection.commit()
            return redirect(url_for('user'))
        return render_template('user_dashboard.html',d=d, o=o, cn=cn, totalPrice=totalPrice, orders=orders, noOfItems=noOfItems, username=username)
    else:
        return redirect(url_for('dashboard'))


class SettingUserPassword(Form):
    password = PasswordField('新密码', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message=' - Passwords do not match'),
        validators.Length(min=5, max=20, message=' - Min 5 characters')
    ])
    confirm = PasswordField('重复新密码')
    accept_tos = BooleanField(' ', [validators.DataRequired()])

@app.route('/setting/users/')
@app.route('/setting/users',  methods=['POST', 'GET'])
@is_logged_in
def Setting():
    noOfItems = addcart()
    form = SettingUserPassword(request.form)
    if 'password' in request.args:
        q = request.args['password']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM users WHERE id=%s", (q,))
        result = curso.fetchone()
        if result:
            if result['id'] == session['uid']:
                if request.method == 'POST' and form.validate():
                    password = sha256_crypt.encrypt(str(form.password.data))

                    # Create Cursor
                    cur = mysql.connection.cursor()
                    exe = cur.execute("UPDATE users SET password=%s WHERE id=%s",
                                      (password, q))
                    mysql.connection.commit()
                    cur.close()

                    if exe:
                        updateprofile = '资料已更新, '
                        return render_template('user_dashboard.html', result=result, form=form, updateprofile=updateprofile, noOfItems=noOfItems)
                    else:
                        flash('档案未更新', 'danger')
                return render_template('user_setting_password.html', result=result, form=form, noOfItems=noOfItems)
            else:
                flash('擅自', 'danger')
                return redirect(url_for('login'))
        else:
            flash('擅自! 请登录', 'danger')
            return redirect(url_for('login'))
    else:
        flash('擅自', 'danger')
        return redirect(url_for('login'))

class SettingUserForm(Form):
    username = StringField('用户名', [validators.length(min=3, max=50)],
                       render_kw={'autofocus': True, 'placeholder': '用户名'})
    email = StringField('电子邮件', [validators.DataRequired(), validators.Email(), validators.length(min=4, max=25)],
                       render_kw={'placeholder': '电子邮件'})
    consignee = StringField('收货人', [validators.DataRequired()])
    telp = StringField('手机号码', [validators.DataRequired()])
    prov = StringField('省份', [validators.DataRequired()])
    city = StringField('城市', [validators.DataRequired()])
    region = StringField('区/县', [validators.DataRequired()])
    street = StringField('街道/镇', [validators.DataRequired()])
    detail = StringField('详细地址', [validators.DataRequired()])

@app.route('/setting/user/')
@app.route('/setting/user',  methods=['POST', 'GET'])
@is_logged_in
def settings():
    noOfItems = addcart()
    form = SettingUserForm(request.form)
    if 'user' in request.args:
        q = request.args['user']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM users WHERE id=%s", (q,))
        result = curso.fetchone()
        if result:
            if result['id'] == session['uid']:
                if request.method == 'POST' and form.validate():
                    username = form.username.data
                    email = form.email.data
                    consignee = form.consignee.data
                    telp = form.telp.data
                    prov = form.prov.data
                    city = form.city.data
                    region = form.region.data
                    street = form.street.data
                    detail = form.detail.data

                    # Create Cursor
                    cur = mysql.connection.cursor()
                    exe = cur.execute("UPDATE users SET username=%s, email=%s, consignee=%s, phonenumber=%s, provinces=%s, city=%s, region=%s, street=%s, d_address=%s WHERE id=%s",
                                      (username, email, consignee, telp, prov, city, region, street, detail, q))
                    mysql.connection.commit()
                    cur.close()

                    if exe:
                        updateprofile = '资料已更新, '
                        return render_template('user_dashboard.html', result=result, form=form, updateprofile=updateprofile, noOfItems=noOfItems)
                    else:
                        flash('档案未更新', 'danger')
                return render_template('user_setting.html', result=result, form=form, noOfItems=noOfItems)
            else:
                flash('擅自', 'danger')
                return redirect(url_for('login'))
        else:
            flash('擅自! 请登录', 'danger')
            return redirect(url_for('login'))
    else:
        flash('擅自', 'danger')
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password_temp = request.form['password']

        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM users WHERE email = %s", [email])
        if result > 0:
            data = cur.fetchone()
            password = data['password']
            username = data['username']
            type = data['type']
            uid = data['id']

            if sha256_crypt.verify(password_temp, password):
                if type == 1:
                    session['admin_logged_in'] = True
                    session['logged_in'] = True
                    session['username'] = username
                    session['logged_in_type'] = 1
                    session['type'] = type
                    session['uid'] = uid
                    flash('您现在已登录', 'success')
                    return redirect(url_for('dashboard'))
                    # app.logger.info('PASSWORD MATH')
                else:
                    session['logged_in'] = True
                    session['username'] = username
                    session['logged_in_type'] = 1
                    session['type'] = type
                    session['uid'] = uid
                    flash('您现在已登录', 'success')
                    return redirect(url_for('user', username=username))
            else:
                error = '登录无效'
                return render_template('login.html', error=error)
                # app.logger.info('PASSWORD NO MATH')
            # Close connection
            cur.close()
        else:
            error = '找不到用户名'
            return render_template('login.html', error=error)
            # app.logger.info('USER GAK ADA')
    return render_template('login.html')

class RegisterForm(Form):
    username = StringField('用户名', [InputRequired(), validators.Length(min=4, max=20, message=' - Min 4 and Max 20 characters long')])
    email = StringField('电子邮件', [InputRequired(),
        Email(message=' - Invalid Email')])
    password = PasswordField('密码', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message=' - Passwords do not match'),
        validators.Length(min=5, max=20, message=' - Min 5 characters')
    ])
    confirm = PasswordField('重复输入密码')
    accept_tos = BooleanField(' ', [validators.DataRequired()])

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(str(form.password.data))

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(username, consignee, email, password) VALUES(%s, %s, %s, %s)", (username, username, email, password))
        mysql.connection.commit()
        cur.close()

        flash('您现在已注册并可以登录', 'success' )
        return render_template('login.html', form=form)

    return render_template('register.html', form=form)


@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('您现在已退出', 'success')
    return redirect(url_for('login'))

# SELECT p.id_phone, brand, phone, price, picture, id_cart, id_users
# FROM product_phone as p INNER JOIN cart as c
# ON p.id_phone = c.id_phone
# WHERE c.id_users = 2

@app.route("/cart")
@is_logged_in
def cart():
    noOfItems = addcart()
    cur = mysql.connection.cursor()
    uid = session['uid']
    # uid = 2
    result = cur.execute("SELECT brand, phone, price, picture, p.id_phone, id_cart, date, id_users FROM product_phone as p INNER JOIN cart as c ON p.id_phone = c.id_phone WHERE c.id_users = " + str(uid))
    products = cur.fetchall()
    totalPrice = 0
    totalP = 0
    for row in products:
        totalP += row['price']
        locale.setlocale( locale.LC_ALL, '' )
        totalPrice = locale.format("%.2f", totalP, 1)
        # totalPrice = locale.currency( totalP,symbol=False, grouping=True )
        # totalPrice = currency.pretty(totalP, 'CNY', trim=True)

    if result > 0:
        return render_template("cart.html", result=result, totalPrice=totalPrice, products=products, noOfItems=noOfItems)
    else:
        msg = "您的购物车目前是空的"
        return render_template("cart.html", result=result, msg=msg, totalPrice=totalPrice, products=products, noOfItems=noOfItems)

@app.route("/tes")
def tes():
    locale.setlocale( locale.LC_ALL, '' ) #CNY
    # totalPrice = locale.currency( 2800, grouping=True )
    aaaa = locale.format("%.2f", 2800, 1)
    # totalPrice = moneyfmt('1234',sep=',', dp='.')
    # totalPrice = currency.pretty(8880, 'CNY', trim=True)
    return  aaaa

@app.route("/removeFromCart")
@is_logged_in
def removeFromCart():
    if 'productId' in request.args:
        id_cart = request.args['productId']
        uid = session['uid']
        try:
            cur = mysql.connection.cursor()
            cur.execute("DELETE FROM cart WHERE id_users = " + str(uid) + " AND id_cart = " + str(id_cart))
            mysql.connection.commit()
            print("removed successfully")
        except:
            cur.rollback()
            print("ERRORS Delete")
    cur.close()
    return redirect(url_for('cart'))

@app.route("/checkout", methods=['POST','GET'])
@is_logged_in
def checkout():
    noOfItems = addcart()
    if 'shipping' in request.args:
        shipping = request.args['shipping']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE id=%s", (shipping,))
        result = cur.fetchone()
        if result:
            uid = session['uid']
            cur.execute("SELECT phone, price, p.id_phone, id_cart FROM product_phone as p INNER JOIN cart as c ON p.id_phone = c.id_phone WHERE c.id_users = " + str(uid))
            products = cur.fetchall()
            totalP = 0
            for row in products:
                totalP += row['price']
                locale.setlocale( locale.LC_ALL, '' )
                totalPrice = locale.format("%.2f", totalP, 1)
            if request.method == 'POST':
                consignee = request.form['consignee']
                phonenumber = request.form['phonenumber']
                provinces = request.form['provinces']
                city = request.form['city']
                region = request.form['region']
                street = request.form['street']
                d_address = request.form['d_address']

                curso = mysql.connection.cursor()
                exe = curso.execute("UPDATE users SET consignee=%s, phonenumber=%s, provinces=%s, city=%s, region=%s, street=%s, d_address=%s WHERE id=%s", (consignee, phonenumber, provinces, city, region, street, d_address, shipping))
                mysql.connection.commit()
                curso.close()
                if exe:
                    flash('送货更新成功！', 'success')
                    return render_template("payout.html", totalP=totalP, pub_key=pub_key, products=products, totalPrice=totalPrice, result=result, noOfItems=noOfItems)
                else:
                    return render_template("payout.html", totalP=totalP, pub_key=pub_key, products=products, totalPrice=totalPrice, result=result, noOfItems=noOfItems)

            return render_template("shipping.html", products=products, totalPrice=totalPrice, result=result, noOfItems=noOfItems)
        else:
            flash('未经授权！请登录', 'danger')
            return redirect(url_for('login'))
    else:
        return redirect(url_for('cart'))

@app.route('/pay', methods=['POST'])
@is_logged_in
def pay():
    if request.method == 'POST':
        customer = stripe.Customer.create(
            email=request.form['stripeEmail'],
            source=request.form['stripeToken']
            )

        uid = session['uid']
        cur = mysql.connection.cursor()
        cur.execute("SELECT phone, price, description, p.id_phone, id_cart, c.id_users FROM product_phone as p INNER JOIN cart as c ON p.id_phone = c.id_phone WHERE c.id_users = " + str(uid))
        products = cur.fetchall()
        totalPrice = 0
        for row in products:
            totalPrice += row['price']
            charge = stripe.Charge.create(
                 customer=customer.id,
                 amount=totalPrice,
                 currency='JPY',
                 description='Product Payed'
                 )
            id_phone = row['id_phone']
            phone = row['phone']
            price = row['price']
            uname = session['username']
            status = 'check'
            cur.execute("INSERT INTO `orders` (id_users, id_phone, username, phone, price, status) VALUES(%s, %s, %s, %s, %s, %s)", (uid, id_phone, uname, phone, price, status))
        cur.execute("DELETE FROM cart WHERE id_users = " + str(uid))
        mysql.connection.commit()
        flash('产品支付成功检查命令', 'success')
        return redirect(url_for('dashboard'))
    else:
        abort(404)

# @app.route('/thanks')
# # @is_logged_in
# def thanks():
#     flash('Product Payed successful Check Order', 'success')
#     return redirect(url_for('dashboard'))

@app.route('/alipay', methods=['POST'])
@is_logged_in
def alipay():
    if request.method == 'POST':
        uid = session['uid']
        idusers = request.form['idusers']
        idphone = request.form['idphone']
        username = request.form['username']
        total = request.form['total']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO payment (username, methods, id_users, id_phone, total) VALUES(%s, %s, %s, %s, %s)", (username, 'Alipay', idusers, idphone, total))
        cur.execute("SELECT phone, price, description, p.id_phone, id_cart, c.id_users FROM product_phone as p INNER JOIN cart as c ON p.id_phone = c.id_phone WHERE c.id_users = " + str(uid))
        products = cur.fetchall()
        totalPrice = 0
        for row in products:
            totalPrice += row['price']
            id_phone = row['id_phone']
            phone = row['phone']
            price = row['price']
            uname = session['username']
            status = 'check'
            cur.execute("INSERT INTO `orders` (id_users, id_phone, username, phone, price, status) VALUES(%s, %s, %s, %s, %s, %s)", (uid, id_phone, uname, phone, price, status))
        cur.execute("DELETE FROM cart WHERE id_users = " + str(uid))
        mysql.connection.commit()
        flash('产品支付成功检查命令', 'success')
        return redirect(url_for('dashboard'))
    else:
        abort(404)

@app.route('/weixin', methods=['POST'])
@is_logged_in
def weixin():
    if request.method == 'POST':
        uid = session['uid']
        idusers = request.form['idusers']
        idphone = request.form['idphone']
        username = request.form['username']
        total = request.form['total']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO payment (username, methods, id_users, id_phone, total) VALUES(%s, %s, %s, %s, %s)", (username, 'Weixin', idusers, idphone, total))
        cur.execute("SELECT phone, price, description, p.id_phone, id_cart, c.id_users FROM product_phone as p INNER JOIN cart as c ON p.id_phone = c.id_phone WHERE c.id_users = " + str(uid))
        products = cur.fetchall()
        totalPrice = 0
        for row in products:
            totalPrice += row['price']
            id_phone = row['id_phone']
            phone = row['phone']
            price = row['price']
            uname = session['username']
            status = 'check'
            cur.execute("INSERT INTO `orders` (id_users, id_phone, username, phone, price, status) VALUES(%s, %s, %s, %s, %s, %s)", (uid, id_phone, uname, phone, price, status))
        cur.execute("DELETE FROM cart WHERE id_users = " + str(uid))
        mysql.connection.commit()
        flash('产品支付成功检查命令', 'success')
        return redirect(url_for('dashboard'))
    else:
        abort(404)
# BUAT ADMIN


class AdminAddress(Form):
    name = StringField('名字', [validators.length(min=3, max=50)],
                       render_kw={'autofocus': True, 'placeholder': 'Username'})
    address = StringField('地址', [validators.DataRequired()])
    telp = StringField('手机号码', [validators.DataRequired()])
    email = StringField('电子邮件', [validators.DataRequired(), validators.Email(), validators.length(min=4, max=25)],
                       render_kw={'placeholder': 'Email'})
    twitter = StringField('<i class="fa fa-twitter-square"></i> Twitter', [validators.DataRequired()])
    facebook = StringField('<i class="fa fa-facebook-square"></i> Facebook', [validators.DataRequired()])
    instagram = StringField('<i class="fa fa-instagram"></i> Instagram', [validators.DataRequired()])
    weixin = StringField('<i class="fa fa-weixin"></i> Weixin', [validators.DataRequired()])
    title = StringField('标题', [validators.DataRequired()])
    content = StringField('内容', [validators.DataRequired()])
    motive = StringField('动机', [validators.DataRequired()])

@app.route('/setting', methods=['POST', 'GET'])
@not_admin_logged_in
@is_logged_in
def setting_admin():
    order = OrdersQueue()
    form = AdminAddress(request.form)
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM admin_address")
    adr = cur.fetchone()
    if 'address' in request.args:
        id = request.args['address']
        if request.method == 'POST':
            name = form.name.data
            email = form.email.data
            telp = form.telp.data
            address = form.address.data

            cur = mysql.connection.cursor()
            exe = cur.execute("UPDATE admin_address SET name=%s, email=%s, phonenumber=%s, address=%s WHERE id_aa=%s", (name, email, telp, address, id))
            mysql.connection.commit()
            cur.close()
            if exe:
                flash('设置地址已更新', 'success')
                return redirect(url_for('setting_admin'))
            else:
                flash('更新', 'success')
                return redirect(url_for('setting_admin'))
        return render_template('pages/settings.html', order=order, adr=adr, form=form)
    if 'media' in request.args:
        id = request.args['media']
        if request.method == 'POST':
            twitter = form.twitter.data
            facebook = form.facebook.data
            instagram = form.instagram.data
            weixin = form.weixin.data
            cur = mysql.connection.cursor()
            exe = cur.execute("UPDATE admin_address SET twitter=%s, facebook=%s, instagram=%s, weixin=%s WHERE id_aa=%s", (twitter, facebook, instagram, weixin, id))
            mysql.connection.commit()
            cur.close()
            if exe:
                flash('设置社交媒体已更新', 'success')
                return redirect(url_for('setting_admin'))
            else:
                flash('更新', 'success')
                return redirect(url_for('setting_admin'))
        return render_template('pages/settings.html', order=order, adr=adr, form=form)
    if 'about' in request.args:
        id = request.args['about']
        if request.method == 'POST':
            title = request.form['title']
            content = request.form['content']
            motive = request.form['motive']
            file = request.files['picture']
            pic = file.filename
            photo = pic.replace("'", "")
            picture = photo.replace(" ", "_")
            if picture.lower().endswith(('.png', '.jpg', '.jpeg')):
                save_photo = photos.save(file, folder='about')
                if save_photo:
                    cur = mysql.connection.cursor()
                    exe = cur.execute("UPDATE admin_address SET title=%s, content=%s, motive=%s, picture=%s WHERE id_aa=%s", (title, content, motive, picture, id))
                    mysql.connection.commit()
                    cur.close()
                    if exe:
                        flash('设置关于已更新', 'success')
                        return redirect(url_for('setting_admin'))
                    else:
                        flash('更新', 'success')
                        return redirect(url_for('setting_admin'))
                else:
                    flash('图片不保存', 'danger')
                    return redirect(url_for('setting_admin'))
            else:
                flash('文件不受支持', 'danger')
                return redirect(url_for('setting_admin'))
        return render_template('pages/settings.html', order=order, adr=adr, form=form)
    else:
        return render_template('pages/settings.html', order=order, adr=adr, form=form)


@app.route('/product')
@not_admin_logged_in
@is_logged_in
def product():
    order = OrdersQueue()
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM product_phone ORDER BY id_phone DESC ")
    product = cur.fetchall()
    if result > 0:
        return render_template('pages/admin_product.html', order=order, product=product, result=result)
    else:
        return render_template('pages/admin_product.html', order=order, product=product, result=result)


@app.route('/add_product', methods=['POST', 'GET'])
@not_admin_logged_in
@is_logged_in
def add_product():
    order = OrdersQueue()
    if request.method == 'POST':
        brand = request.form.get('brand')
        phone = request.form['phone']
        available = request.form['available']
        price = request.form['price']
        description = request.form['description']
        file = request.files['picture']
        colors = request.form['colors']
        camera = request.form['camera']
        internal = request.form['internal']
        network = request.form['network']
        battery = request.form['battery']
        announced = request.form['announced']
        status = request.form['status']
        dimensions = request.form['dimensions']
        weight = request.form['weight']
        size = request.form['size']
        resolution = request.form['resolution']
        if brand and available and phone and price and colors and camera and internal and description and network and battery and announced and status and dimensions and weight and size and resolution and file:
            pic = file.filename
            photo = pic.replace("'", "")
            picture = photo.replace(" ", "_")
            if picture.lower().endswith(('.png', '.jpg', '.jpeg')):
                save_photo = photos.save(file, folder=brand)
                if save_photo:
                    # Create Cursor
                    curs = mysql.connection.cursor()
                    curs.execute("INSERT INTO product_phone(brand,phone,available,price,description,picture)"
                                 "VALUES(%s, %s, %s, %s, %s, %s)",
                                 (brand, phone, available, price, description, picture))
                    id_phone = curs.lastrowid
                    id_level = curs.lastrowid
                    curs.execute("INSERT INTO product_phone_level(id_level,id_phone,colors,camera,internal,network,battery,announced,status,dimensions,weight,size,resolution)"
                                 "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                 (id_level, id_phone, colors, camera, internal, network, battery, announced, status, dimensions, weight, size, resolution))
                    mysql.connection.commit()
                    # Close Connection
                    curs.close()

                    flash('产品添加成功', 'success')
                    return redirect(url_for('add_product'))
                else:
                    flash('图片不保存', 'danger')
                    return redirect(url_for('add_product'))
            else:
                flash('文件不受支持', 'danger')
                return redirect(url_for('add_product'))
        else:
            flash('请填写所有表格', 'danger')
            return redirect(url_for('add_product'))
    else:
        return render_template('pages/admin_add_product.html', order=order)

@app.route('/edit-product', methods=['POST', 'GET'])
@not_admin_logged_in
@is_logged_in
def edit_product():
    order = OrdersQueue()
    if 'id' in request.args:
        id_phone = request.args['id']
        curso = mysql.connection.cursor()
        res = curso.execute("SELECT * FROM product_phone WHERE id_phone=%s", (id_phone,))
        product_phone = curso.fetchall()
        curso.execute("SELECT * FROM product_phone_level WHERE id_phone=%s", (id_phone,))
        product_phone_level = curso.fetchall()
        if res:
            if request.method == 'POST':
                brand = request.form.get('brand')
                phone = request.form['phone']
                available = request.form['available']
                price = request.form['price']
                description = request.form['description']
                colors = request.form['colors']
                camera = request.form['camera']
                internal = request.form['internal']
                network = request.form['network']
                battery = request.form['battery']
                announced = request.form['announced']
                status = request.form['status']
                dimensions = request.form['dimensions']
                weight = request.form['weight']
                size = request.form['size']
                resolution = request.form['resolution']
                # Create Cursor
                if brand and phone and available and price and description:
                    if colors and camera and internal and network and battery and announced and status and dimensions and weight and size and resolution:
                        # Create Cursor
                        cur = mysql.connection.cursor()
                        phoneproduct = curso.execute("UPDATE product_phone SET brand=%s, phone=%s, available=%s, price=%s, description=%s WHERE id_phone=%s",
                                    (brand, phone, available, price, description, id_phone))
                        spesifikasi = cur.execute("UPDATE product_phone_level SET colors=%s, camera=%s, internal=%s, network=%s, battery=%s, announced=%s, status=%s, dimensions=%s, weight=%s, size=%s, resolution=%s WHERE id_phone=%s", (colors, camera, internal, network, battery, announced, status, dimensions, weight, size, resolution, id_phone))
                        mysql.connection.commit()
                        print(" product", phoneproduct)
                        print(" spec", spesifikasi)
                        if phoneproduct and spesifikasi:
                            flash('数据已更新', 'success')
                            return render_template('pages/admin_edit_product.html',order=order, product_phone=product_phone, product_phone_level=product_phone_level)
                        else:
                            flash('数据已更新', 'success')
                            return render_template('pages/admin_edit_product.html',order=order, product_phone=product_phone, product_phone_level=product_phone_level)
                    else:
                        flash('填写所有字段', 'danger')
                        return render_template('pages/admin_edit_product.html',order=order, product_phone=product_phone, product_phone_level=product_phone_level)
                else:
                    flash('填写所有字段', 'danger')
                    return render_template('pages/admin_edit_product.html',order=order, product_phone=product_phone, product_phone_level=product_phone_level)
            else:
                return render_template('pages/admin_edit_product.html',order=order, product_phone=product_phone, product_phone_level=product_phone_level)
        else:
            abort(404)
    else:
        abort(404)


@app.route('/delete-product/<string:id_phone>', methods=['POST'])
@not_admin_logged_in
@is_logged_in
def delete_product(id_phone):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM product_phone WHERE id_phone = %s", [id_phone])
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('product'))

@app.route('/viewproduct')
def viewproduct():
    noOfItems = addcart()
    order = OrdersQueue()
    if 'view' in request.args:
        id_phone = request.args['view']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM product_phone WHERE id_phone=%s", (id_phone,))
        product = curso.fetchall()
        curso.execute("SELECT * FROM product_phone_level WHERE id_phone=%s", (id_phone,))
        product_level = curso.fetchall()
        x = content_based_filtering(id_phone)
        wrappered = wrappers(content_based_filtering, id_phone)
        execution_time = timeit.timeit(wrappered, number=0)
        print('Execution time: ' + str(execution_time) + ' usec')
        if 'uid' in session:
            uid = session['uid']
            # Create cursor
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM product_phone_view WHERE user_id=%s AND product_id_phone=%s", (uid, id_phone))
            result = cur.fetchall()
            if result:
                now = datetime.datetime.now()
                now_time = now.strftime("%y-%m-%d %H:%M:%S")
                cur.execute("UPDATE product_phone_view SET date=%s WHERE user_id=%s AND product_id_phone=%s",
                            (now_time, uid, id_phone))
            else:
                cur.execute("INSERT INTO product_phone_view(user_id, product_id_phone) VALUES(%s, %s)", (uid, id_phone))
                mysql.connection.commit()
        return render_template('view_product.html',order=order, x=x, phoneproduct=product, product_level=product_level, noOfItems=noOfItems)
    elif 'brand' in request.args:
        br = request.args['brand']
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM product_phone WHERE brand=%s", (br,))
        brand = cursor.fetchall()
        if br in brand:
            br = br['brand']
        cursor.execute("SELECT brand FROM product_phone GROUP BY brand")
        brandNav = cursor.fetchall()
        return render_template('view_brand_product.html', order=order, brand=brand, brandNav=brandNav, br=br, noOfItems=noOfItems)

    else:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM product_phone")
        brand = cursor.fetchall()
        cursor.execute("SELECT brand FROM product_phone GROUP BY brand")
        brandNav = cursor.fetchall()
        return render_template('view_brand_product.html',order=order, brand=brand,brandNav=brandNav, noOfItems=noOfItems)

@app.route('/addToCart')
@is_logged_in
def addToCart():
    if 'add' in request.args:
        uid = session['uid']
        id_phone = request.args['add']
        try:
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO cart(id_phone, id_users) VALUES(%s, %s)", (id_phone, uid))
            mysql.connection.commit()
        except Exception as e:
            flash("Error Add To Cart")
            print(e)
        return redirect(url_for('viewproduct'))
    else:
        return redirect(url_for('index'))

@app.route('/articles')
@not_admin_logged_in
@is_logged_in
def articles():
    order = OrdersQueue()
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM articles WHERE author = %s ORDER BY id DESC ", [session['username']])
    articles = cur.fetchall()
    if result > 0:
        return render_template('pages/admin_articles.html', order=order, articles=articles, result=result)
    else:
        msg = '找不到文章'
        return render_template('pages/admin_articles.html', msg=msg)

class ArticleForm(Form):
    title = StringField('', [InputRequired(), validators.Length(min=1)])
    body = TextAreaField('', [InputRequired('Min 10 characters'), validators.Length(min=10)])

@app.route('/add-article', methods=['GET', 'POST'])
@is_logged_in
def add_article():
    order = OrdersQueue()
    form = ArticleForm(request.form)
    if request.method == 'POST' and form.validate():

        title = form.title.data
        body = form.body.data
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO articles(title, body, author) VALUES(%s, %s, %s)",(title, body, session['username']))
        mysql.connection.commit()
        cur.close()

        send = '文章创建'
        return render_template('pages/admin_add_article.html', form=form, send=send, order=order)

    return render_template('pages/admin_add_article.html', form=form, order=order)

# Edit Article
@app.route('/edit-article/', defaults={'id' : 'id'})
@app.route('/edit-article/<int:id>', methods=['GET', 'POST'])
@is_logged_in
def edit_article(id):
    order = OrdersQueue()
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM articles WHERE id = %s", [id])
    article = cur.fetchone()
    cur.close()
    # Get form
    form = ArticleForm(request.form)
    form.title.data = article['title']
    form.body.data = article['body']

    if request.method == 'POST' and form.validate():
        title = request.form['title']
        body = request.form['body']
        cur = mysql.connection.cursor()
        app.logger.info(title)
        cur.execute ("UPDATE articles SET title=%s, body=%s WHERE id=%s",(title, body, id))
        mysql.connection.commit()
        cur.close()

        send = '文章更新'
        return render_template('pages/admin_edit_article.html', send=send, form=form, order=order)
    return render_template('pages/admin_edit_article.html', form=form, order=order)

# Delete Article
@app.route('/delete-article/<string:id>', methods=['POST'])
@is_logged_in
def delete_article(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM articles WHERE id = %s", [id])
    mysql.connection.commit()
    cur.close()

    delete = '文章已删除'
    return redirect(url_for('articles'))
    # return render_template('articles.html', delete=delete)


@app.route('/about')
def About():
    noOfItems = addcart()
    order = OrdersQueue()
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM admin_address")
    about = cur.fetchone()
    return render_template('about.html', about=about, noOfItems=noOfItems, order=order)

@app.route('/faq')
def Faq():
    noOfItems = addcart()
    order = OrdersQueue()
    return render_template('faq.html', noOfItems=noOfItems, order=order)
# UNTUK SEMUA USER
@app.route('/visitors')
def visitors():

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM product_phone ORDER BY RAND() LIMIT 4")
    product = cur.fetchall()
    cur.execute("SELECT brand,picture FROM product_phone GROUP BY brand ORDER BY RAND() LIMIT 3")
    brand = cur.fetchall()

    cur.execute("SELECT * FROM articles ORDER BY create_date DESC Limit 2")
    articles = cur.fetchall()
    cur.close()
    lock = LockFile("app/module/visitors.txt")
    with lock:
        with open("app/module/visitors.txt", "r+") as f:
            fileContent = f.read()
            if fileContent == "":
                count = 1
            else:
                count = int(fileContent) + 1
            f.seek(0)
            f.write(str(count))
            f.truncate()
            return render_template("index.html", articles=articles, brand=brand, product=product, count=count)

@app.errorhandler(404)
def notfound(error):
    return render_template("404.html")
