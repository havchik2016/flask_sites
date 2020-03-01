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
                                    <textarea class="form-control" id="about" rows="1" name="surname" placeholder="Введите фамилию"></textarea>
                                    <textarea class="form-control" id="about" rows="1" name="name" placeholder="Введите имя"></textarea>
                                    <br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <br>
                                    <div class="form-group">
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="education">
                                          <option>Начальное</option>
                                          <option>Основное среднее</option>
                                          <option>Среднее профессиональное</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div> 
                                     Какие у Вас есть профессии?
                                     <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="prof1" name="accept1">
                                        <label class="form-check-label" for="prof1">Инженер-исследователь</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="prof2" name="accept2">
                                        <label class="form-check-label" for="prof2">Инженер-строитель</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="prof3" name="accept3">
                                        <label class="form-check-label" for="prof3">Пилот</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="prof4" name="accept4">
                                        <label class="form-check-label" for="prof4">Метеоролог</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="prof5" name="accept5">
                                        <label class="form-check-label" for="prof5">Инженер по жизнеобеспечению</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="prof6" name="accept6">
                                        <label class="form-check-label" for="prof6">Инженер по радиационной защите</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="prof7" name="accept7">
                                        <label class="form-check-label" for="prof7">Врач</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="prof8" name="accept8">
                                        <label class="form-check-label" for="prof8">Экзобиолог</label>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                    <label for="photo">Приложите фотографию</label>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                        </body>
                    </html>'''
    elif request.method == "POST":
        return "Форма отправлена успешно!"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
