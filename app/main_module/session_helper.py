import datetime


def check_old_files(session: dict):
    # 20 minutes
    MAX_FILE_LIFETIME_SECONDS = 1200

    if not session.get('files'):
        session['files'] = {}

    files = session['files'].copy()
    for _file in files:
        time_diff = datetime.datetime.now(
        ) - session['files'][_file]['created_at']

        if time_diff.total_seconds() > MAX_FILE_LIFETIME_SECONDS:
            del session['files'][_file]


def save_files_in_session(session: dict, g_files: dict):

    if not session.get('files'):
        session['files'] = {}

    for _file in g_files:
        files = g_files[_file]
        session['files'].update(files)
