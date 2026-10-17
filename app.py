from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# ==========================================
# INSTAGRAM USERS
# ==========================================

users = [
    {
        "id": 1,
        "username": "roja_creations",
        "name": "Roja",
        "avatar": "profile1.jpg",
        "bio": "Digital Creator | Photography Lover",
        "followers": "12.5K"
    },
    {
        "id": 2,
        "username": "telugu_traveller",
        "name": "Travel Diaries",
        "avatar": "profile2.jpg",
        "bio": "Exploring beautiful destinations",
        "followers": "25.8K"
    },
    {
        "id": 3,
        "username": "foodie_hyderabad",
        "name": "Hyderabad Foodie",
        "avatar": "profile3.jpg",
        "bio": "Food | Travel | Lifestyle",
        "followers": "18.2K"
    },
    {
        "id": 4,
        "username": "nature_lover",
        "name": "Nature Photography",
        "avatar": "profile4.jpg",
        "bio": "Nature and Wildlife Photography",
        "followers": "32.4K"
    },
    {
        "id": 5,
        "username": "fashion_diaries",
        "name": "Fashion Diaries",
        "avatar": "profile5.jpg",
        "bio": "Fashion | Beauty | Lifestyle",
        "followers": "19.6K"
    }
]


# ==========================================
# INSTAGRAM POSTS
# ==========================================

posts = [
    {
        "id": 1,
        "username": "roja_creations",
        "avatar": "profile1.jpg",
        "image": "post1.jpg",
        "location": "Hyderabad, India",
        "caption": "Beautiful moments deserve beautiful memories ❤️✨",
        "likes": 2450,
        "comments": 128,
        "time": "2 HOURS AGO"
    },
    {
        "id": 2,
        "username": "telugu_traveller",
        "avatar": "profile2.jpg",
        "image": "post2.jpg",
        "location": "Araku Valley, Andhra Pradesh",
        "caption": "Lost in the beauty of nature 🌿⛰️",
        "likes": 3820,
        "comments": 215,
        "time": "5 HOURS AGO"
    },
    {
        "id": 3,
        "username": "foodie_hyderabad",
        "avatar": "profile3.jpg",
        "image": "post3.jpg",
        "location": "Hyderabad, India",
        "caption": "Nothing beats delicious Hyderabadi biryani 😍🍛",
        "likes": 5640,
        "comments": 342,
        "time": "1 DAY AGO"
    },
    {
        "id": 4,
        "username": "roja_creations",
        "avatar": "profile1.jpg",
        "image": "post4.jpg",
        "location": "Visakhapatnam",
        "caption": "Sunsets and peaceful evenings 🌅❤️",
        "likes": 1980,
        "comments": 95,
        "time": "2 DAYS AGO"
    },
    {
        "id": 5,
        "username": "nature_lover",
        "avatar": "profile4.jpg",
        "image": "post5.jpg",
        "location": "Kerala, India",
        "caption": "Nature is the best therapy 🌿💚",
        "likes": 4250,
        "comments": 178,
        "time": "3 DAYS AGO"
    },
    {
        "id": 6,
        "username": "fashion_diaries",
        "avatar": "profile5.jpg",
        "image": "post6.jpg",
        "location": "Bangalore, India",
        "caption": "Confidence is the best outfit ✨❤️",
        "likes": 6850,
        "comments": 320,
        "time": "4 DAYS AGO"
    }
]


# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def home():
    return render_template(
        "index.html",
        users=users,
        posts=posts
    )


# ==========================================
# GET ALL USERS
# ==========================================

@app.route("/api/users", methods=["GET"])
def get_users():
    return jsonify(users)


# ==========================================
# GET ALL POSTS
# ==========================================

@app.route("/api/posts", methods=["GET"])
def get_posts():
    return jsonify(posts)


# ==========================================
# LIKE A POST
# ==========================================

@app.route("/api/like/<int:post_id>", methods=["POST"])
def like_post(post_id):

    for post in posts:

        if post["id"] == post_id:

            post["likes"] += 1

            return jsonify({
                "success": True,
                "message": "Post liked successfully",
                "likes": post["likes"]
            })

    return jsonify({
        "success": False,
        "error": "Post not found"
    }), 404


# ==========================================
# ADD COMMENT
# ==========================================

@app.route("/api/comment/<int:post_id>", methods=["POST"])
def add_comment(post_id):

    data = request.get_json(silent=True) or {}

    comment = data.get("comment", "")

    if not isinstance(comment, str) or not comment.strip():
        return jsonify({
            "success": False,
            "error": "Comment cannot be empty"
        }), 400

    if len(comment) > 500:
        return jsonify({
            "success": False,
            "error": "Comment is too long"
        }), 400

    for post in posts:

        if post["id"] == post_id:

            post["comments"] += 1

            return jsonify({
                "success": True,
                "message": "Comment added successfully",
                "comment": comment.strip(),
                "comments": post["comments"]
            })

    return jsonify({
        "success": False,
        "error": "Post not found"
    }), 404


# ==========================================
# HEALTH CHECK
# ==========================================

@app.route("/health", methods=["GET"])
def health():

    return jsonify({
        "status": "healthy",
        "application": "InstaVibe Instagram Clone"
    })


# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )
