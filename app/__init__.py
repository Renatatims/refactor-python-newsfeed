from app.routes import home, dashboard, api
from flask import Flask
from app.db import init_db
from app.utils import filters

def create_app(test_config=None):
  # set up app config
  app = Flask(__name__, static_url_path='/')
  app.url_map.strict_slashes = False
  app.config.from_mapping(
    SECRET_KEY='p87-y20-t20-news.feed'
  )
  @app.route('/hello')
  def hello():
    return 'hello world'
  # register routes
  app.register_blueprint(home)
  app.register_blueprint(dashboard)

  # register filter functions with the Jinja template environment
  app.jinja_env.filters['format_url'] = filters.format_url
  app.jinja_env.filters['format_date'] = filters.format_date
  app.jinja_env.filters['format_plural'] = filters.format_plural

  # register api
  app.register_blueprint(api)
  
  init_db(app)
 
  return app