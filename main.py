from flask import Flask, render_template, request
import logging

app = Flask(__name__)

# Configura el sistema de logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros_pintura = int(request.form['tarros_pintura'])

        # Calcula descuento
        if 18 <= edad <= 30:
            descuento_porcentaje = 0.15
        elif edad > 30:
            descuento_porcentaje = 0.25
        else:
            descuento_porcentaje = 0

        total_sin_descuento = tarros_pintura * 9000
        descuento = total_sin_descuento * descuento_porcentaje
        total_con_descuento = total_sin_descuento - descuento

        # Logs
        logger.info(f'Usuario {nombre} realizó una solicitud para el ejercicio 1.')
        logger.info(f'Edad: {edad}, Tarros de pintura: {tarros_pintura}')
        logger.info(f'Total sin descuento: ${total_sin_descuento}, Descuento aplicado: ${descuento}')

        return render_template('ejercicio1.html', nombre=nombre, total_sin_descuento=total_sin_descuento,
                               total_con_descuento=total_con_descuento, descuento=descuento)

    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje_bienvenida = None
    mensaje_error = None

    if request.method == 'POST':
        usuario = request.form.get('usuario')
        contrasena = request.form.get('contrasena')

        # Verificar usuario y contraseña
        if usuario == 'juan' and contrasena == 'admin':
            mensaje_bienvenida = 'Bienvenido administrador juan'
        elif usuario == 'pepe' and contrasena == 'user':
            mensaje_bienvenida = 'Bienvenido usuario pepe'
        else:
            mensaje_error = 'Usuario o contraseña incorrectos'

    return render_template('ejercicio2.html', mensaje_bienvenida=mensaje_bienvenida, mensaje_error=mensaje_error)

if __name__ == '__main__':
    app.run(debug=True)
