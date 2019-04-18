from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')
@app.route("/signup")
def signup():
    username_list = User.objects().distinct('email')
    if 'token' in session:
        return render_template('index.html')
    if request.method == 'GET':
        return render_template("signup.html", username_list=username_list)
    else:
        form = request.form
        e = form['email']
        u = form['username']
        p = form['password']
        # # Tạm bỏ email cùng các phần liên quan bên dưới. 
        # # Khi nào cần thì bật lại vì trên database vẫn để email với giá trị default.
        # e = form['email']
        new_user = User(email=e.strip(), username=u.strip(), password=p.strip()) #, email=e)
        new_user.save()
        session['token'] = u
        # Đăng ký xong thì trả về giao diện trang Welcome
        return render_template('welcome.html', fullname=f, u=u)
@app.route("/login")
def login():
     user_list = User.objects()
    user_list_2 = {}
    for e in user_list:
        user_list_2[e.username] = e.password
    users = json.dumps(user_list_2) # chuyển python dictionaty sang JSON object
    if 'token' in session:
        return render_template('homepage.html')
    if request.method == 'GET':
        return render_template('login.html', users=users)
    else:
        form = request.form
        e = form['email']
        p = form['password']
        # phần code bên dưới bị comment vì đã xử được trực tiếp bằng javascript trong html
        user_check = User.objects(email=e).first()
        # Check xem có nhập username và password hay không và nhập đúng hay không:
        if user_check is None:
            return render_template('login.html', warning=warning, users=users)
        else:
            if p != user_check.password:
                return render_template('login.html', warning=warning, users=users)'
        if warning != '':
            return render_template('login.html', warning=warning, users=users)
        else:
        session['token'] = e
        # Đăng nhập đúng thì trả về giao diện trang Welcome
        return render_template('index.html', fullname=User.objects(email=e).first().fullname, u=u e=e) 

@app.route("/experts")
def experts():
    return render_template('ex.html')
if __name__ ==  "__main__":
    app.run(debug=True)