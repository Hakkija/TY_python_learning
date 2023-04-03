from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        server_name = request.form['server_name']
        admin_name = request.form['admin_name']
        admin_password = request.form['admin_password']
        server_ip = request.form['server_ip']
        user_name = request.form['user_name']
        user_password = request.form['user_password']

        cmd = f"ansible-playbook -i {server_ip}, playbook.yml --extra-vars 'server_name={server_name} admin_name={admin_name} admin_password={admin_password} user_name={user_name} user_password={user_password}'"

        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

        if result.returncode != 0:
            return render_template('index.html', error=result.stderr.decode())
        else:
            return render_template('index.html', message="Successfully provisioned server!")
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
