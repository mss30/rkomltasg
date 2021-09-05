from flask import Flask, send_file

from utils import random_objects_generator, generate_objects_report

# Default server port is 5000
app = Flask(__name__)

app.config['OUTPUT_FILE_NAME'] = 'output.txt'
app.config['OUTPUT_FILE_MAX_SIZE'] = 2000000


@app.route('/generate')
def generate_objects():
    try:
        random_objects_generator(output_file_name=app.config['OUTPUT_FILE_NAME'],
                                 output_file_max_size=app.config['OUTPUT_FILE_MAX_SIZE'])
        return {'operation': 'success', 'message': 'Objects file generated on server'}, 200
    except Exception:
        return {'error': 'Something went wrong while generating object file'}, 500


@app.route('/download')
def download_file():
    try:
        return send_file(path_or_file=app.config['OUTPUT_FILE_NAME'], as_attachment=True)
    except FileNotFoundError:
        return {'operation': 'failed', 'error': 'File not found on server'}, 500
    except Exception:
        return {'operation': 'failed', 'error': 'Something went wrong while downloading the file'}, 500


@app.route('/report')
def generate_report():
    try:
        return generate_objects_report(app.config['OUTPUT_FILE_NAME']), 200
    except FileNotFoundError:
        return {'operation': 'failed', 'error': 'Please use generate api to generate the file first'}, 500
    except Exception:
        return {'operation': 'failed', 'error': 'Something went wrong while generating report'}, 500
