from flask import Flask, render_template

import requests
response =requests.get("https://api.npoint.io/1967e694641da42398df")
data=response.json()
app = Flask(__name__)
post_obj=[]
print(type(data))
print(data)
@app.route('/')
def home():

    return render_template("index.html",posts=data)

@app.route('/post/<int:index>')
def get_all_post(index):
    for key in data:
        if key["id"]==index:
            requested_post=key
    return  render_template("post.html",post=requested_post)
if __name__ == "__main__":
    app.run(debug=True)
