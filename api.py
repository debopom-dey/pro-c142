from flask import Flask, jsonify, request
import csv
from storage import all_articles, liked_articles, not_liked_articles
from demographic_filtering import output
from content_filtering import get_recommendations

popular_articles=[]
recommended_articles= []

app = Flask(__name__)

@app.route("/get-article")
def get_article():
    return jsonify({
        "data": all_articles[0],
        "status": "success"
    })

@app.route("/liked-article", methods=["POST"])
def liked_article():
    article = all_articles[0]
    all_articles=all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/unliked-article", methods=["POST"])
def unliked_article():
    article = all_articles[0]
    all_articles=all_articles[1:]
    not_liked_articles.append(article)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/popular-article")
def unliked_article():
    article = all_articles[0]
    all_articles=all_articles[1:]
    popular_articles.append(article)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/recommended-article")
def recommended_articles():
 for liked_article in liked_articles:
        output = get_recommendations(liked_article[4])
        for data in output:
            recommended_articles.append(data)



if __name__ == "__main__":
    app.run()