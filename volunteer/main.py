import psycopg2
from flask import Flask, render_template, g, request, redirect, url_for
from flask import Blueprint
from . import db

bp=Blueprint("volunteer", "volunteer", url_prefix="/volunteer")


if __name__=="__main__":
    app.run()