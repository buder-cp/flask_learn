from flask import Flask, render_template
import config

app = Flask(__name__)
app.config.from_object(config)


@app.route("/control")
def control():
    context = {
        "age": 188,
        'books': ['红楼梦', '三国演义', '水浒传', '西游记'],
        "person": {"name": "zhiliao", "age": 18}
    }
    return render_template("control.html", **context)


@app.route("/about")
def about():
    context = {
        "username": "周杰伦",
        'books': ['红楼梦', '三国演义']
    }

    return render_template("about.html", **context)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
