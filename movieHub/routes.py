from flask import Flask, redirect, render_template, request, url_for
from flask_login import LoginManager,login_user, current_user, login_required, logout_user
from login import loginUser
import sqlite3
from server import app
from sqlite3 import Error
from imdb import IMDb
from dbFunctions import *

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "searchText" in request.form:
            searchText = request.form["searchText"]
            return redirect(url_for('search', searchText=searchText))
    ia = IMDb()
    movies = movieQuery(None)
    return render_template("index.html", movies=movies)


# @app.route('/movie', methods=["GET" , "POST"])
# def movie():
#     ia = IMDb()
#     imdb_id = request.args.get("id")
    
#     movie = ia.get_movie(imdb_id)
#     ia.update(movie)
    
#     cinema_ids = playsQuery(imdb_id)
#     cinemaList = []
#     timesObj = []
#     for i in cinema_ids:
#         cinemaList.append(cinemaQuery(i.cinema_id))
#         timesObj.append(timeQuery(i.cinema_id, imdb_id))

#     times = []
#     for obj in timesObj:
#         for i in obj:
#             times.append(showtimesQuery(i.showtime_id))

#     return render_template("movie.html", movie=movie, cinemas=cinemaList, times=times)


@app.route('/login', methods=["GET" , "POST"])
def login():
    if request.method == "POST":
        username = str(request.form["username"])
        password = str(request.form["password"])

        if loginUser(username, password):
            return redirect(url_for("index"))

    return render_template("login.html")
'''
Created by : Rahil Agrawal
Created At : 11/5/18
Mock Functions for testing links
Can be modified by Backend Devs
'''
@app.route('/payment', methods=["GET" , "POST"])
def payment():
    return render_template("payment.html")

@app.route('/movielist', methods=["GET" , "POST"])
def movielist():
    return render_template("movielist.html")

@app.route('/moviedetail', methods=["GET" , "POST"])
def moviedetail():
    ia = IMDb()
    imdb_id = request.args.get("id")

    movie = ia.get_movie(imdb_id)
    ia.update(movie)
    
    cinema_ids = playsQuery(imdb_id)
    cinemaList = []
    timesObj = []
    for i in cinema_ids:
        cinemaList.append(cinemaQuery(i.cinema_id))
        timesObj.append(timeQuery(i.cinema_id, imdb_id))

    times = []
    for obj in timesObj:
        for i in obj:
            times.append(showtimesQuery(i.showtime_id))
    return render_template("moviedetail.html", movie=movie, cinemas=cinemaList, times=times)

@app.route('/signup', methods=["GET" , "POST"])
def signup():
    if request.method == "POST":
        username = str(request.form["username"])
        password = str(request.form["password"])

        if newUser(username, password):
            return redirect(url_for("index"))
    return render_template("signup.html")

@app.route('/search', methods=["GET", "POST"])
def search():
    searchText = request.args.get("searchText")
    movies = searchQuery(searchText)
    return render_template("search.html", searchText=searchText, movies=movies)
