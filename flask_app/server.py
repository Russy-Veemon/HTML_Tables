from flask import Flask, render_template
app = Flask(__name__)

# @app.route('/')
# def test():
#     return render_template("data.html")
#test route to see what the problem was for jinga error and no url found

@app.route('/test')
def create_table():
    jedis = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
    return render_template("data.html", jedis=jedis)	



if __name__=="__main__":
    app.run(debug=True)