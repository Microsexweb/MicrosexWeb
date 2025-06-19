from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    matricula = request.args.get('matricula')
    return render_template('main.html', matricula=matricula)

@app.route('/ubc')
def ubc():
    return render_template('ubc.html')

@app.route('/logout')
def logout():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
