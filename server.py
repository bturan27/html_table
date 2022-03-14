from flask import Flask, render_template
app=Flask(__name__)




@app.route('/')
def render_table():
    users = [
        {'first_name' : 'Michael', 'Last_name' : 'Choi'},
        {'first_name' : 'John', 'Last_name' : 'Supsupin' },
        {'first_name' : 'Mark', 'Last_name' : 'Guillen'},
        {'first_name' : 'KB', 'Last_name' : 'Tonel'}


    ]
    return render_template("index.html", new_variable=users  )






if __name__ == "__main__":
    app.run(debug=True)