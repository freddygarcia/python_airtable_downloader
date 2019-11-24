from flask import Blueprint, redirect, jsonify, request, render_template, flash, g, send_file, session
from flask import current_app as app
from app.main_module import api_consumer
from app.main_module import files_exporter

routes = Blueprint('routes', __name__, url_prefix='/')


@routes.route("/")
def index():
    files_exporter.check_old_files(session)
    return render_template('index.html')


@routes.route('/files', methods=['POST'])
def download_files():
    base_id = request.form.get('base')
    api_key = request.form.get('key')
    questions = api_consumer.get_questions(base_id, api_key)

    if not questions['success']:
        code = questions['code']
        reason = questions['content']
        return jsonify(reason), questions['code']

    files = files_exporter.export_questions(questions)
    files = files_exporter.files_to_json(session, files)
    return jsonify(files), 200


@routes.route('/file/<document_id>', methods=['GET'])
def download_file(document_id):

    files = session.get('files')
    if files:
        f = files.get(document_id)
        if f:
            filepath = f['file']
            filename = f['name'] + '.xlsx'

            return send_file(
                filepath,
                attachment_filename=filename,
                as_attachment=True
            )

    return "Wrong id", 404


def init_app(app):
    app.register_blueprint(routes)
