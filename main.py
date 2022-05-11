from flask import Flask, redirect, make_response, abort, request, render_template

app = Flask(__name__)
a = [{'name': 'Alex', 'id': '1', 'surname': 'Turner', 'age': 36},
     {'name': 'Thom', 'id': '2', 'surname': 'Yorke', 'age': 53}]
b = ''


@app.route('/users')
def users():
    response = make_response(render_template('users.html', a=a, b=b))
    return response


@app.route('/')
def home():
    return redirect('/users')


@app.route('/user/<idd>')
def user(idd):
    print(idd)
    print(a)
    for i in range(len(a)):
        if idd == a[i]['id']:
            response = render_template('idd.html', a=a[i])
            return response
    else:
        abort(404)


@app.route('/add_user', methods=['post'])
def add_user():
    m = 0
    for i in range(len(a)):
        if int(a[i]['id']) > m:
            m = int(a[i]['id'])
    name = request.form.get('name')
    surname = request.form.get('surname')
    age = request.form.get('age')
    new_user = {'name': name, 'id': str(m+1), 'surname': surname, 'age': age}
    a.append(new_user)
    return redirect('/users')


if __name__ == '__main__':
    app.run(debug=True)

