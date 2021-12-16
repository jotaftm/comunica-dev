from click import argument, echo
from flask.cli import AppGroup
from flask import Flask
import secrets

from app.models.users_model import UserModel


def cli_admin(app: Flask):
    cli = AppGroup('cli_admin')

    @cli.command('create')
    @argument('name')
    @argument('cpf')
    @argument('email')
    def cli_create_admin(name: str, cpf: str='test', email: str='test'):
        echo(f'email: {email}, cpf:{cpf}')

        user_check = UserModel.query.filter_by(cpf=cpf).first()
        if user_check:
            echo('')
            echo(f'ERROR: CPF {cpf} already registered.')
            return None

        user_check = UserModel.query.filter_by(email=email).first()
        if user_check:
            echo('')
            echo(f'ERROR: Email {email} already registered.')
            return None
        
        password = secrets.token_hex(8)

        new_admin = UserModel(name=name, cpf=cpf, email=email, user_role='admin', password=password)
        new_admin.save()
        echo('User created successfully.')
        echo(f'email: {email}')
        echo(f'cpf: {cpf}')
        echo(f'password: {password}')

    app.cli.add_command(cli)


def init_app(app: Flask):
    cli_admin(app)
