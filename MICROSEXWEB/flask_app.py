from flask import Flask, render_template, redirect, url_for, request, jsonify
from ubc import unidad_basica_calculo
from util import hex_a_op, op_a_hex, hex_a_bin

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

@app.route('/ubc', methods=['POST'])
def calcular():
    data = request.get_json()

    # Convertir hex a arrays de bits (usando util.py)
    A = hex_a_op(data['A'])
    B = hex_a_op(data['B'])
    senal_control = data['senal_control']  # Ej: [1,0,1,0,1,0]

    # Procesar en la UBC
    resultado, acarreo, _ = unidad_basica_calculo(A, B, 0, senal_control)

    # Convertir resultado a hex
    resultado_hex = op_a_hex(resultado)

    return jsonify({
        "resultado": resultado_hex,
        "acarreo": acarreo[-1]  # Último bit de acarreo
    })

@app.route('/conv_hex', methods=['POST'])
def conv_hex():
    return jsonify ({ 
        "bin_a": hex_a_bin(request.get_json()['a']), 
        "bin_b": hex_a_bin(request.get_json()['b']),
    })
if __name__ == '__main__':
    app.run(debug=True)
