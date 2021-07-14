from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/validate/<name>')
def validate_user(name):
    if name == 'Admin':
        return redirect(url_for('admin_page', name=name))
    elif name == 'Abdul-Malik':
        return redirect(url_for('user_page', name=name))
    else:
        if name == 'Guest':
            return redirect(url_for('guest_page', name=name))


@app.route('/user/<name>')
def user_page(name):
    return 'hello %s ' % name


@app.route('/admin/<name>')
def admin_page(name):
    return 'Welcome to the admin page %s ' % name


@app.route('/Guest/<name>')
def guest_page(name):
    return 'Welcome to the guest page' % name


@app.route('/payment/<float:salary>')
def payment(salary):
    if salary > 10500.50:
        return redirect('https://www.fnb.co.za')

    else:
        if salary < 10500.50:
            return redirect('https://www.sahomeloans.com')


if __name__ == '__main__':
    app.debug = True
    app.run()
