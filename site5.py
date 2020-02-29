from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def colonization():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def advertise():
    return '''Человечество вырастает из детства.<br>
Человечеству мала одна планета.<br>
Мы сделаем обитаемыми безжизненные пока планеты.<br>
И начнем с Марса!<br>
Присоединяйся!'''


@app.route("/image_mars")
def image():
    return f'''<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src={url_for('static', filename="img/mars.png")} 
                        alt="здесь должна была быть картинка, но не нашлась">
                    <br>
                    <b>Вот она какая, красная планета</b>
                  </body>
                </html>'''


@app.route("/promotion_image")
def promotion_image():
    return f'''<!doctype html>
                    <html lang="ru">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" 
                        href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                        integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
                        <title>Колонизация</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src={url_for('static', filename="img/mars.png")} 
                            alt="здесь должна была быть картинка, но не нашлась">
                        <br>
                        <div class="alert alert-primary" role="alert">
                            Человечество вырастает из детства.
                        </div>
                        <div class="alert alert-success" role="alert">
                            Человечеству мала одна планета.
                        </div>
                        <div class="alert alert-danger" role="alert">
                            Мы сделаем обитаемыми безжизненные пока планеты.
                        </div>
                        <div class="alert alert-warning" role="alert">
                            И начнем с Марса!
                        </div>
                        <div class="alert alert-info" role="alert">
                            Присоединяйся!
                        </div>
                      </body>
                    </html>'''


@app.route("/astronaut_selection", methods=["GET", "POST"])
def selection_form():
    if request.method == "GET":
        return f'''<!DOCTYPE html>
                    <html>
                        <head>
                            <meta charset="utf-8"><link rel="stylesheet" 
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
                            <title>Отбор астронавтов</title>
                        </head>
                        <body>
                            <h1>Анкета претендента на участие в миссии</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите фамилию" name="email">
                                    <input type="password" class="form-control" id="password" placeholder="Введите имя" name="password">
                                </form>
                            </div>
                        </body>
                    </html>'''
    elif request.method == "POST":
        pass

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
