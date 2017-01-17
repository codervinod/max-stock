# -*- coding: utf-8 -*-
from flask import Flask
from whitenoise import WhiteNoise

import v1


def create_app():
  app = Flask(__name__, static_folder='static')
  app.register_blueprint(
    v1.bp,
    url_prefix='/v1')
  app.wsgi_app = WhiteNoise(app.wsgi_app, root='static/')
  return app


app = create_app()

if __name__ == '__main__':
  create_app().run(debug=True, port=9872)
