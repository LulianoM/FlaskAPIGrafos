from flask.cli import FlaskGroup

from application.app import create_app

app = create_app("production")

cli = FlaskGroup(app)


if __name__ == "__main__":
    cli()
