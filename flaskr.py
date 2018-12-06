import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

# configuration
DATABASE = 'projects.db'
#DEBUG = True
#SECRET_KEY = 
#USERNAME = 
#PASSWORD = 

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()

@app.route("/")
def hello():
    cur = g.db.execute('select * from entries order by id desc')
    entries = [dict(uid=row[0], title=row[1], text=row[2], author=row[3], supervisor=row[4], image_url=row[5], url=row[6]) for row in cur.fetchall()]
    print(entries)
    return render_template('hello-boot.html', entries=entries)

@app.route("/projects/<project>/")
def show_project(project):
    return render_template('{}.html'.format(project))

@app.route("/students/")
def show_students_call():
    return render_template('students.html')

@app.route("/advisors/")
def show_advisors_call():
    return render_template('students.html')




if __name__ == '__main__':
    app.run()
