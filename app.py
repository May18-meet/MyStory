#x  from model import *

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

from flask_heroku import Heroku


app = Flask(__name__)
db = SQLAlchemy(app)
#save
# story=Story(name='HP', cont='asdsf')
# db.session.add(story)
# story=Story(name='H1P', cont='as4tf4rdsf')
# db.session.add(story)

# db.session.commit()

#access
# result = db.session.query(Story).filter_by(name='HP').all()


# Set "homepage" to index.html
@app.route('/')
def main():
    return render_template('main.html')

@app.route('/all_stories/')
def all_stories():
    # stories = Story.query.all()
    return render_template('all_stories.html', stories=None)

@app.route('/review/')
def Review():
   # if Review.query.all()!=None:
    #    review= Review.query.all()
     #   return render_template('review.html',review=review)
    return render_template('review.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post')
def post_Story():
    return render_template('post.html')   


@app.route('/post_review')
def post_review():
    return render_template('postre.html')


@app.route('/login')
def login():
    return render_template('login.html')  

@app.route('/sign_up')
def sign_up():
    return render_template('signup.html')          

'''
@app.route('/post_Story')
def post_Story():
    new_story=Story()
    new_story.name=
    new_story.Story=
    db.session.add(new_story)
    db.session.commit()
        return render_template('post.html')    
'''
# Save e-mail to database and send to success page
@app.route('/prereg', methods=['POST'])
def prereg():
    email = None
    if request.method == 'POST':
        email = request.form['email']
        # Check that email does not already exist (not a great query, but works)
        if not db.session.query(User).filter(User.email == email).count():
            reg = User(email)
            db.session.add(reg)
            db.session.commit()
            return render_template('main.html')
    return render_template('main.html')

if __name__ == '__main__':
    #app.debug = True
    app.run(debug=True)