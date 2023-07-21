from app import app

if __name__ == "__main__":
    app.run(debug=True)



# In the app.py file, we import the db object from db.py and initialize the MongoDB connection using db.init_app(app).

# mongodb+srv://neha:phadtare@cluster0.rw33h7h.mongodb.net/entertainmentexpress?retryWrites=true&w=majority'