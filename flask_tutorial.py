from flask import Flask,render_template,request
#to make our own web server
app = Flask('server1')
visited=0
@app.route('/hi')
def index():
    return render_template('search.html')

@app.route('/shree')
def aa():
    print('i visited')
    return 
@app.route('/counter')
def sex():
    global visited
    visited +=1
    return render_template('practice.html',visited=visited)
app.run(port=8080)
