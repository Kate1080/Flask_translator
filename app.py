from flask import Flask, render_template, request

app = Flask(__name__)

my_words = {"hello": "Привет", "i": "Я", "you": "Ты/Вы", "we": "Мы", "he": "Он", "she": "Она", "they": "Они", "it": "Оно", "mother": "Мама", "father": "Папа", "brother": "Брат", "sister": "Сестра", "grandmother": "Бабушка", "grandfather": "Дедушка"}

@app.route('/hello')
def hello_world():
    return "hello world"

@app.route('/hello/<name>')
def hello_with_name(name):
    return f"hello {name}"

# @app.route('/')
# def index():
#     return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def dict_page():
    if request.method == 'POST':
        word = request.form["word"].lower()
        return render_template('result.html',word=my_words[word])

    return render_template('dict.html')


if __name__ == '__main__':
    app.run()
