import requests
from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime
from datetime import date





articles = []
header = "<head> <!-- Required meta tags --> <meta charset=\"utf-8\"> <meta name=\"viewport\" content=\"width=device-width, initial-scale=1, shrink-to-fit=no\"> <link href=\"https://fonts.googleapis.com/css2?family=Comfortaa:wght@400;700&family=Staatliches&display=swap\" rel=\"stylesheet\"><link href=\"https://fonts.googleapis.com/css2?family=Noto+Sans&display=swap\" rel=\"stylesheet\">    <!-- Bootstrap CSS --> <link rel=\"stylesheet\" href=\"https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css\" integrity=\"sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk\" crossorigin=\"anonymous\"> <title>The Yemeni Crisis </title> </head>"
titlediv = "<div class=\"jumbotron text-light\" style=\"padding-left: 10%; padding-right: 10%; background: rgb(0,115,255); background: linear-gradient(90deg, rgba(0,115,255,1) 0%, rgba(210,230,255,1) 100%); border-radius: 0px;\"> <h1 class=\"display-3\" style=\"font-family: 'Staatliches', cursive;\"><a class=\"text-light\" style=\"text-decoration: none;\" href=\"/\">The Yemeni Crisis </a></h1> <p class=\"lead\" style=\"font-family: 'Comfortaa', cursive;\">“The first step toward change is awareness” –– Nathaniel Branden</p> </div>"
donate_titlediv = "<div class=\"jumbotron text-light\" style=\"padding-left: 10%; padding-right: 10%; background: rgb(0,115,255); background: linear-gradient(90deg, rgba(0,115,255,1) 0%, rgba(210,230,255,1) 100%); border-radius: 0px;\"> <h1 class=\"display-3\" style=\"font-family: 'Staatliches', cursive;\"><a class=\"text-light\" style=\"text-decoration: none;\" href=\"/\"><< Back</a></h1> <p class=\"lead\" style=\"font-family: 'Comfortaa', cursive;\">“The first step toward change is awareness” –– Nathaniel Branden</p> </div>"
footer = "<div class=\"card text-center bg-dark text-light\" style=\"padding: 20px; border-radius: 0px;\"> <p class=\"lead\" style=\"font-family: 'Comfortaa', cursive; font-weight: 500;margin-bottom: 0px;\">Powered by&nbsp;<a href=\"https://gnews.io\" >gnews.io</a></p> <p class=\"lead\" style=\"font-family: 'Comfortaa', cursive; font-weight: 600;\">Created by Gautam Bhaskar </p> </div>"
scripts = "<!-- Optional JavaScript --> <!-- jQuery first, then Popper.js, then Bootstrap JS --> <script src=\"https://code.jquery.com/jquery-3.5.1.slim.min.js\" integrity=\"sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj\" crossorigin=\"anonymous\"></script> <script src=\"https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js\" integrity=\"sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo\" crossorigin=\"anonymous\"></script> <script src=\"https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js\" integrity=\"sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI\" crossorigin=\"anonymous\"></script> <script> </script>"

today = date.today()
last_pull = ""
with open("date.json", "r") as json_file:
    last_pull = datetime.strptime(json.load(json_file), '%Y-%m-%d').date()
if today > last_pull:
    with open("date.json", "w") as json_file:
        json.dump(str(today), json_file)
    url = "https://gnews.io/api/v3/search?q=yemen&token=b7b22a92c40b559b5227a29ee61b8dd3"

    querystring = {"autoCorrect":"false","pageNumber":"1","pageSize":"20","q":"Yemen Crisis","safeSearch":"false"}

    headers = {
        'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
        'x-rapidapi-key': "b2880ab58dmshd1a39375dc76241p19a6e3jsnd824e08d2ded"
    }
    response = requests.request("GET", url).json()
    articles = response["articles"]
    with open('articles.json', 'w') as json_file:
        json.dump(articles, json_file)
else:
    with open('articles.json', 'r') as json_file:
        articles = json.load(json_file)
    








# articles = response["articles"]



used = []
html = "<!doctype html> <html lang=\"en\">" + header + " <body>" + titlediv + "<div class=\"container\"> <h1 style=\"font-family: 'Staatliches', cursive;\">Latest News</h1> <div class=\"row\">"
for article in articles:
    if article["title"][0:10] in used:
        pass
    else:
        image = ""
        used.append(article["title"][0:10])
        if article["image"] == None:
            # Add default image here
            image = '/static/default.png'
        else:
            image = article["image"]
        html += "<div class=\"col-lg-4 col-sm-6\"> <div class=\"card\" style=\"width: 100%; border-radius: 6px; margin-bottom: 25px;\"> <img src=" + image + " class=\"card-img-top\" alt=\"...\"> <div class=\"card-body\"> <h5 class=\"card-title\" style=\" font-family: 'Comfortaa', cursive; \">" + article["title"] + "</h5> <h6 class=\"card-subtitle mb-2 text-muted\" style=\" font-family: 'Comfortaa', cursive; \">" + article["source"]["name"] + "</h6> <p class=\"card-text\" style=\"font-family: 'Noto Sans', sans-serif;\">" + article["description"] + "<a href=" + article["url"] + " target = \"_blank\" class=\"card-link\"> Read More</a></p> <h6><span class=\"badge badge-dark\">" + article["publishedAt"][0:10] + "</span></h6> </div> </div> </div>" 

html += "</div> </div> <div class=\"jumbotron text-white\" style=\"padding-left: 10%; padding-right: 10%; border-radius: 0px; margin-bottom: 0px; background: rgb(0,115,255); background: linear-gradient(90deg, rgba(0,115,255,1) 0%, rgba(0,20,46,1) 100%);\"><h1 class=\"display-5\" style=\"font-family: 'Staatliches', cursive;\">What exactly is happening in Yemen?</h1> <blockquote class=\"blockquote\"> <p class=\"mb-0 text-white\" style=\"font-family: 'Comfortaa', cursive;\"><a class=\"text-light\" style=\"text-decoration: none;\" href=\"https://news.un.org/en/story/2019/02/1032811\"><i>“Since violence broke out in late March 2015, conditions in Yemen - already one of the poorest countries in the Middle East - have rapidly deteriorated. Extreme shortages of food, safe water, sanitation and healthcare, as well as deadly massive outbreaks of cholera and diphtheria have taken a heavy toll on civilian lives and deprived families of basic needs.  At least 70 percent majority of the population lack access to food, safe water and adequate healthcare and nearly one million suspected cholera cases have been registered since 2018.”</i></a></p>  <footer class=\"blockquote-footer text-white\" style=\"text-align: right; font-family: 'Comfortaa', cursive;\"><cite title=\"UN News\">The United Nations</cite></footer> </blockquote>  <p class=\"lead\" style=\"font-family: 'Comfortaa', cursive;\">Yemen is suffering from the world’s worst humanitarian crisis, yet the world is silent. Although we’re all in a critical situation with the pandemic, the BLM movement, and many other global events, right now, the people of Yemen need our help the most. The country has been devastated by civil war since 2011. The healthcare system has collapsed and disease is rampant. The children suffer the most as malnutrition leads to a poor immune system and an inability to fight even the slightest of infections. Countries like the US, the UK, UAE, Spain, and Canada are supporting Saudi Arabian airstrikes. We must act now.</p> </div>  <div class=\"jumbotron text-white\" style=\"padding-left: 10%; padding-right: 10%; border-radius: 0px; margin-bottom: 0px; background: rgb(0,115,255); background: linear-gradient(90deg, rgba(0,115,255,1) 0%, rgba(0,20,46,1) 100%);\"> <h1 class=\"display-5\" style=\"font-family: 'Staatliches', cursive;\">Why the website?</h1> <p class=\"lead\" style=\"font-family: 'Comfortaa', cursive;\"> The children of Yemen have suffered enough. It’s time for us to help. We must come together to stop this conflict and support relief organizations. The first step towards creating such change is awareness. We must all stay informed and educated in order to better contribute to this cause. This website compiles a list of news articles that discuss the Yemeni Crisis. Read the articles and share the information with your friends and relatives. Start the conversation.</p></div> <div class=\"jumbotron text-white\" style=\"padding-left: 10%; padding-right: 10%; border-radius: 0px; margin-bottom: 0px; background: rgb(0,115,255); background: linear-gradient(90deg, rgba(0,115,255,1) 0%, rgba(0,20,46,1) 100%);\"> <h1 class=\"display-5\" style=\"font-family: 'Staatliches', cursive;\">How can you help?</h1> <p class=\"lead\" style=\"font-family: 'Comfortaa', cursive;\">To help the people of Yemen, you can start by staying informed about the situation and raising awareness. This website compiles a list of news articles that discuss the Yemeni Crisis. Read the articles to better understand what is going on.</p> <p class=\"lead\" style=\"font-family: 'Comfortaa', cursive;\">Then, share this website with friends and family to help raise awareness. If you can, donate towards humanitarian relief programs. Relief organizations are running low on funds, and your support would help them significantly.</p><a class=\"btn btn-primary\" style=\"margin-right: 5vw; font-family: 'Comfortaa', cursive;\" href=\"https://www.hrw.org/world-report/2020/country-chapters/yemen\" role=\"button\">Learn more</a> <a class=\"btn btn-primary\" style=\"margin-right: 5vw; font-family: 'Comfortaa', cursive;\" href=\"/donate\" role=\"button\">Donate</a> </div>" + footer + scripts + " </body> </html>"

orgs = []
with open('orgs.json', 'r') as outfile:
    orgs = json.load(outfile)

donate_html = "<!doctype html> <html lang=\"en\">" + header + "<body>" + donate_titlediv + "<div class=\"container\"> <h1 style=\"font-family: 'Staatliches', cursive;\">Where to Donate</h1> <div class=\"row\">"
for org in orgs:
    donate_html += " <div class=\"col-lg-6 col-md-12\"> <div class=\"card\" style=\"width: 100%; margin-bottom: 25px;\"> <div class=\"card-body\"> <h5 class=\"card-title\" style=\"font-family: 'Comfortaa', cursive;\">" + org["name"] + "</h5> <p class=\"card-text\" style=\"font-family: 'Noto Sans', sans-serif;e;\">" + org["description"] + "</p>               <a href=" + org["url"] + " class=\"btn btn-primary\" style=\"font-family: 'Comfortaa', cursive;\">Donate</a> </div> </div> </div>"

donate_html += " </div></div>" + footer + scripts + "</body> </html>"




# Flask Routing
app = Flask(__name__)

@app.route("/")
def home():
    return html

@app.route("/donate")
def donate():
    return donate_html


if __name__ == "__main__":
    app.run()



# Write code to pull data from API once a day. Basically, in the main python file, check if the current date is greater than the last time the data was updated. When data is updated, store date in a variable for this comparison and write it to a file.



