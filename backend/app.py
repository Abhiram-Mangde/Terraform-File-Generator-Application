
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

import os
import json
from jinja2 import Environment, BaseLoader

app = Flask(__name__, static_folder='../frontend', static_url_path='/static')
CORS(app)

def load_templates():
    db_path = os.path.join(os.path.dirname(__file__), 'templates_db.json')
    with open(db_path, 'r') as f:
        return json.load(f)

TEMPLATES_DB = load_templates()


@app.route('/generate', methods=['POST'])
def generate_terraform():
    data = request.get_json()
    resource_type = data.get('resourceType')
    cpu = data.get('cpu')
    ram = data.get('ram')
    disk = data.get('disk')

    if resource_type not in TEMPLATES_DB:
        return jsonify({'error': 'Invalid resource type.'}), 400

    env = Environment(
        loader=BaseLoader(),
        variable_start_string='[[',
        variable_end_string=']]',
        block_start_string='[%',
        block_end_string='%]'
    )
    try:
        files = {}
        for key in ['main', 'variables', 'provider', 'outputs']:
            if key in TEMPLATES_DB[resource_type]:
                template_str = TEMPLATES_DB[resource_type][key]
                template = env.from_string(template_str)
                if resource_type == 'vm':
                    files[key] = template.render(cpu=cpu, ram=ram, disk=disk)
                else:
                    files[key] = template.render()
        return jsonify(files)
    except Exception as e:
        return jsonify({'error': f'Template error: {str(e)}'}), 500

# Serve frontend files
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
