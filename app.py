from flask import Flask,render_template
import requests


app =  Flask(__name__)
app.secret_key="secret key"

@app.route('/')
def index():
    #GET https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey=6b1eca38f2d846c2a839e81aa881d191
    url = "https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey=6b1eca38f2d846c2a839e81aa881d191"
    r = requests.get(url).json()
    case={
        'articles':r['articles']
    }
    return render_template('index.html',case = case)

@app.route('/sports')
def sports():
    surl = "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=6b1eca38f2d846c2a839e81aa881d191"
    sr = requests.get(surl).json()
    scase = {
        'articles':sr['articles']
    }
    return render_template('sports.html',scase = scase)

@app.route('/tech')
def tech():
    turl = "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=6b1eca38f2d846c2a839e81aa881d191"
    tr = requests.get(turl).json()
    tcase = {
        'articles':tr['articles']
    }
    return render_template('tech.html',tcase = tcase)


@app.route('/entertainment')
def entertainment():
    eurl = "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=6b1eca38f2d846c2a839e81aa881d191"
    # eurl = "https://newsapi.org/v2/everything?q=bitcoin&apiKey=6b1eca38f2d846c2a839e81aa881d191"
    ur=requests.get(eurl).json()
    ecase = {
       'articles':ur['articles']
    }
    return render_template('entertainment.html',ecase = ecase)

@app.route('/stocks')
def stocks():
    stockurl = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=6b1eca38f2d846c2a839e81aa881d191"
    stockur=requests.get(stockurl).json()
    stockcase={
        'articles':stockur['articles']
    }
    return render_template('stocks.html',stockcase=stockcase)
    

if __name__=='__main__':
    app.run(debug=True)