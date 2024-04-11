from flask import Flask,render_template,request
#to make our own web server
app = Flask('server1')
visited=0
@app.route('/counter')
def set():
    global visited
    visited +=1
    return render_template('practice.html',visited=visited)
app.run(port=8080)
