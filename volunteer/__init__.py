from flask import Flask, render_template
import psycopg2

def create_app():
    app=Flask("volunteer")

    app.config.from_mapping(
        DATABASE="volunteer"
    )

    @app.route("/")
    def index():
        dbconn=psycopg2.connect("dbname=volunteer")
        cursor=dbconn.cursor()
        cursor.execute("select * from users")
        details=cursor.fetchall()
        return render_template("index.html", details=details)

    return app  