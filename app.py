from flask import Flask, render_template, request, redirect, url_for, jsonify

import sqlite3

app = Flask(__name__)

def connect_to_database():
    conn = sqlite3.connect('inventario.db')
    return conn

def add_server(nome, endereco_ip, sistema_operacional=None, especificacoes_hardware=None):
    conn = connect_to_database()
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO servidores (nome, endereco_ip, sistema_operacional, especificacoes_hardware) "
        "VALUES (?, ?, ?, ?)",
        (nome, endereco_ip, sistema_operacional, especificacoes_hardware)
    )
    
    conn.commit()
    
    conn.close()


def list_servers():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM servidores")
    servers = cursor.fetchall()
    conn.close()
    return servers

def update_server(server_id, nome=None, endereco_ip=None, sistema_operacional=None, especificacoes_hardware=None):
    conn = connect_to_database()
    cursor = conn.cursor()

    updates = []
    values = []

    if nome:
        updates.append("nome = ?")
        values.append(nome)
    if endereco_ip:
        updates.append("endereco_ip = ?")
        values.append(endereco_ip)
    if sistema_operacional:
        updates.append("sistema_operacional = ?")
        values.append(sistema_operacional)
    if especificacoes_hardware:
        updates.append("especificacoes_hardware = ?")
        values.append(especificacoes_hardware)

    if updates:
        query = f"UPDATE servidores SET {', '.join(updates)} WHERE id = ?"
        values.append(server_id)
        cursor.execute(query, values)

    conn.commit()
    conn.close()

def remove_server(server_id):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM servidores WHERE id = ?", (server_id,))
    conn.commit()
    conn.close()

@app.route('/')
def index():
    servers = list_servers()
    return render_template('index.html', servers=servers)
        
@app.route('/add_server', methods=['POST'])
def add_server_route():
    nome = request.form.get('nome')
    endereco_ip = request.form.get('endereco_ip')
    sistema_operacional = request.form.get('sistema_operacional', None)
    especificacoes_hardware = request.form.get('especificacoes_hardware', None)
    
    add_server(nome, endereco_ip, sistema_operacional, especificacoes_hardware)
    
    return redirect(url_for('index'))

@app.route('/remove_server', methods=['POST'])
def remove_server_route():
    server_id = request.form.get('server_id')
    remove_server(server_id)
    return redirect(url_for('index'))

@app.route('/update_server_form/<int:server_id>')
def update_server_form(server_id):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM servidores WHERE id = ?", (server_id,))
    server = cursor.fetchone()
    conn.close()
    
    # Renderizar um formulário com os dados atuais do servidor
    return render_template('update_server.html', server=server)

@app.route('/update_server', methods=['POST'])
def update_server_route():
    server_id = request.form.get('server_id')
    nome = request.form.get('nome')
    endereco_ip = request.form.get('endereco_ip')
    sistema_operacional = request.form.get('sistema_operacional')
    especificacoes_hardware = request.form.get('especificacoes_hardware')

    # Chama a função 'update_server' com os valores do formulário e o ID do servidor
    update_server(server_id, nome, endereco_ip, sistema_operacional, especificacoes_hardware)

    return redirect(url_for('index'))



@app.route('/edit_server/<int:server_id>')
def edit_server(server_id):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM servidores WHERE id = ?", (server_id,))
    server = cursor.fetchone()
    conn.close()

    return render_template('update_server.html', server=server)



if __name__ == '__main__':
    app.run(debug=True)
