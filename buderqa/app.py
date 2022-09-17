from flask import Flask
import config
from exts import db, mail
# from blueprints.qa import bp as qa_bp
from blueprints import qa_bp
from blueprints import user_bp

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
mail.init_app(app)

app.register_blueprint(qa_bp)
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run()
