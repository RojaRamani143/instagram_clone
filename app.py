from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

users = [
    {'username':'roja_creations','name':'Roja Creations','initials':'RC','color':'#e85d75'},
    {'username':'telugu_traveller','name':'Travel Diaries','initials':'TT','color':'#4f86c6'},
    {'username':'foodie_hyderabad','name':'Hyderabad Foodie','initials':'FH','color':'#e5a044'},
    {'username':'nature_frames','name':'Nature Frames','initials':'NF','color':'#3f9b80'},
    {'username':'city_lights','name':'City Lights','initials':'CL','color':'#9461b5'}
]
posts = [
    {'id':1,'username':'roja_creations','location':'Hyderabad, India','caption':'Collecting little moments, making big memories ✨','likes':2450,'time':'2 hours ago','theme':'sunset','emoji':'🌇','label':'Golden Hour'},
    {'id':2,'username':'telugu_traveller','location':'Araku Valley, Andhra Pradesh','caption':'A breath of fresh mountain air 🌿','likes':3820,'time':'5 hours ago','theme':'forest','emoji':'🌿','label':'Mountain Escape'},
    {'id':3,'username':'foodie_hyderabad','location':'Hyderabad, India','caption':'Good food, great company, best days 🍛','likes':5640,'time':'1 day ago','theme':'food','emoji':'🍲','label':'Food Stories'},
    {'id':4,'username':'nature_frames','location':'Visakhapatnam, India','caption':'Where the ocean meets the sky 🌊','likes':1980,'time':'2 days ago','theme':'ocean','emoji':'🌊','label':'Coastal Dreams'}
]

@app.get('/')
def home():
    return render_template('index.html', users=users, posts=posts)

@app.get('/api/posts')
def get_posts():
    return jsonify(posts)

@app.get('/health')
def health():
    return jsonify(status='healthy', app='InstaVibe')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
