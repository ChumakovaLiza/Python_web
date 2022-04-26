from flask import Flask, redirect, make_response, abort

app = Flask(__name__)
a = [{'name': 'Alex', 'id': '1', 'surname': 'Turner', 'age': 36},
     {'name': 'Thom', 'id': '2', 'surname': 'Yorke', 'age': 53}]
b = ''


@app.route('/users')
def users():
    c = ''
    for i in range(len(a)):
        b = ''
        b = b + a[i]['name'] + ' ' + a[i]['surname'] + '<br>'
        c = c + '<a href="http://127.0.0.1:5000/user/%s" target="_blank"> %s</a>' % (a[i]['id'], b)
    response = make_response('<h1> %s</h1> ' %(c))
    return response


@app.route('/')
def home():
    return redirect('/users')


@app.route('/user/<idd>')
def user(idd):
    print(idd)
    for i in range(len(a)):
        if idd == a[i]['id']:
            response = make_response('<h1>ФИО:&nbsp %s &nbsp %s <br> Возраст:&nbsp %s </h1> ' % (a[i]['name'], a[i]['surname'], a[i]['age']))
            return response
    else:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)

