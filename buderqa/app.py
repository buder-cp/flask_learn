from flask import Flask, session, g
import config
from exts import db, mail
# from blueprints.qa import bp as qa_bp
from blueprints import qa_bp
from blueprints import user_bp
from flask_migrate import Migrate
from models import UserModel

'''
视频：
https://www.bilibili.com/video/BV17r4y1y7jJ?p=1&vd_source=2f20084a1b171b68d7181958bc52e4fb
【代码+软件】：公众号：pythonjs，关键字：51python，免费领取。（可以加群咨询问题）
【Flask Web全栈开发实战图书】：https://u.jd.com/7I3B1VB（与视频配套，比视频更完整）
【课件】：https://www.zlkt.net/book/detail/10（如无法访问请更换网络）
'''

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
mail.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(qa_bp)
app.register_blueprint(user_bp)


@app.before_request
def before_request():
    user_id = session.get("user_id")
    if user_id:
        try:
            user = UserModel.query.get(user_id)
            # 给g绑定一个叫做user的变量，他的值是user这个变量
            # setattr(g,"user",user)
            g.user = user
        except:
            g.user = None


# 请求来了 -> before_request -> 视图函数 -> 视图函数中返回模板 -> context_processor

@app.context_processor
def context_processor():
    if hasattr(g, "user"):
        return {"user": g.user}
    else:
        return {}


if __name__ == '__main__':
    app.run()
