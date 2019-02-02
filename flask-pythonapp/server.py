from flask import Flask


app = Flask(__name__)

#db = MySQLdb.connect(host="localhost",  # your host
#                     user="root",       # username
#                     passwd="Huawei@123",     # password
#                     db="mypolls")   # name of the database
 
# Create a Cursor object to execute queries.
#cur = db.cursor()


@app.route("/hello")
def hello():
    return "Hello, World!"


if __name__ == "__main__":
    app.run()


