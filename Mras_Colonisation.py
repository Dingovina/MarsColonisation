from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def empty():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    s = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
         'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                        {'<br>'.join(s)}
                  </body>
                </html>"""


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}" 
       alt="здесь должна была быть картинка, но не нашлась">
                  </body>
                </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.png')}" 
           alt="здесь должна была быть картинка, но не нашлась">
                        <div class="alert alert-dark" role="alert">
                          Человечество вырастает из детства.
                        </div>
                        <div class="alert alert-success" role="alert">
                          Человечеству мала одна планета.
                        </div>
                        <div class="alert alert-secondary" role="alert">
                          Мы сделаем обитаемыми безжизненные пока планеты.
                        </div>
                        <div class="alert alert-warning" role="alert">
                          И начнем с Марса!
                        </div>
                        <div class="alert alert-danger" role="alert">
                          Присоединяйся!
                        </div>


                      </body>
                    </html>"""


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static',
                                                                                  filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h2 class="high">Анкета претендента</h2>
                            <h3 class="high">на участие в миссии</h3>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="about" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="about" class="form-control" id="name" placeholder="Введите имя" name="surname">
                                    <br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="EducationSelect" name="Education">
                                          <option>Дошкольное</option>
                                          <option>Начальное</option>
                                          <option>Среднее общее</option>
                                          <option>Среднее профессиональное</option>
                                          <option>Высшее</option>
                                        </select>
                                    </div>
                                    <br>
                                    <div class="form-group">
                                        <label for="form-check" id="question">Какая у Вас профессия?</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="prof" id="i-i">
                                          <label class="form-check-label">
                                            инженер-исследователь
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="prof" id="meteo">
                                          <label class="form-check-label">
                                            метеоролог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="prof" id="pilot">
                                          <label class="form-check-label">
                                            пилот
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="prof" id="builder">
                                          <label class="form-check-label">
                                            строитель
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="prof" id="eczo" >
                                          <label class="form-check-label">
                                            экзобиолог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="prof" id="doc">
                                          <label class="form-check-label">
                                            врач
                                          </label>
                                        </div>
                                    </div>
                                    <br>
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
                                    <br>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <br>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <br>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Вы готовы остаться на Марсе?</label>
                                    </div>
                                    <br>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['education'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form.get('accept'))
        print(request.form['prof'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
