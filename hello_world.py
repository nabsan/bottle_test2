from bottle import route,request, run,template,get
 
# routeデコレーター
# これを使用してURLのPathと関数をマッピングする。
@route('/hello')
def hello():
  return "Hello World222222222!"

@route('/greet/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}', name=name)

@route('/hello2/<name:int>')
def hello2(name):
    return str(name)

@route('/hello3/<name:path>')
def hello3(name):
    return str(name)

@get("/login")
def login():
    nam=request.query.id
    return str(nam)

@route("/login2")
def login2():
   return """
    <form action="/login2" method="post">
    Username: <input name="username" type="text" />
    Password: <input name="password" type="password" />
    <input value="Login" type="submit" />
    </form>
    """

@route('/login2',method='POST')
def do_login():
    username = request.forms.get("username")
    password = request.forms.get("password")
    if check_login(username, password):
        return "<p>Your ligin infomation was correct.</p>"
    else:
        return "<p>Login failed.</p>"


def check_login(username, password):
    if username == "user" and password == "pass":
        return True
    else:
        return False

# ビルトインの開発用サーバーの起動
# ここでは、debugとreloaderを有効にしている
run(host='localhost', port=8080, debug=True, reloader=True)

