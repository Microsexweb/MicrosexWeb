from flask import Flask, render_template, request, jsonify
from ubc import unidad_basica_calculo
from util import hex_a_op, op_a_hex

app = Flask(__name__)

# Rutas existentes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/ubc')
def ubc():
    return render_template('ubc.html')

# Nuevo endpoint para cálculos UBC
@app.route('/calcular', methods=['POST'])
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

if __name__ == '__main__':
    app.run(debug=True)
