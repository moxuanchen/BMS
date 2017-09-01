# -*- coding: utf-8 -*-

from flask import redirect
from flask import url_for
from core.database import db
from core.app import create_app
from flask_migrate import Migrate
from flask_migrate import MigrateCommand
from flask_script import Manager, Server, Shell


app = create_app()
migrate = Migrate(app, db)
manager = Manager(app)


@app.route('/')
def index():
    return redirect(url_for('school.school_signin'))


if __name__ == "__main__":
    manager.add_command("server", Server)
    manager.add_command("shell", Shell)
    manager.add_command('db', MigrateCommand)
    manager.run()
