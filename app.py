from flask import Flask, jsonify, render_template
import subprocess
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Route pour exécuter index.py et lire launch_data1.json
@app.route('/executer_code_1', methods=['POST'])
def executer_code_1():
    try:
        # Exécute le fichier index.py pour générer launch_data1.json
        result1 = subprocess.run(['python', 'index.py'], capture_output=True, text=True)
        result2 = subprocess.run(['python', 'parser.py'], capture_output=True, text=True)


        # Vérifie si le fichier JSON a été créé
        with open('launch_data1.json', 'r') as json_file:
            launch_data = json.load(json_file)

        return jsonify({'message': '', 'launch_data': launch_data})

    except Exception as e:
        return jsonify({'message': f"Erreur lors de l'exécution : {str(e)}"})


# Route pour exécuter index2.py et lire launch_data2.json
@app.route('/executer_code_2', methods=['POST'])
def executer_code_2():
    try:
        # Exécute le fichier index2.py pour générer launch_data2.json
        result = subprocess.run(['python', 'index2.py'], capture_output=True, text=True)

        # Vérifie si le fichier JSON a été créé
        with open('launch_data2.json', 'r') as json_file:
            launch_data = json.load(json_file)

        return jsonify({'message': '', 'launch_data': launch_data})

    except Exception as e:
        return jsonify({'message': f"Erreur lors de l'exécution : {str(e)}"})


if __name__ == '__main__':
    app.run(debug=True)
