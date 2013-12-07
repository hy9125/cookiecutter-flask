# -*- coding: utf-8 -*-
from flask.ext.testing import TestCase
from {{ cookiecutter.repo_name }}.settings import Config
from {{ cookiecutter.repo_name }}.app import create_app
from {{ cookiecutter.repo_name }}.database import db


class TestConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class DbTestCase(TestCase):
    """Base TestCase for tests that require a database."""

    def create_app(self):
        app = create_app(TestConfig)
        with app.app_context():
            db.create_all()
        return app

    def tearDown(self):
        db.session.remove()
        db.drop_all()
