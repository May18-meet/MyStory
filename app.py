from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask import session as login_session
from flask_heroku import Heroku

#save
# story=Story(name='HP', cont='asdsf')
# db.session.add(story)
# story=Story(name='H1P', cont='as4tf4rdsf')
# db.session.add(story)

# db.session.commit()

#access
# result = db.session.query(Story).filter_by(name='HP').all()


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/pre-registration'
db = SQLAlchemy(app)


# Create our database model
class Story(db.Model):
    __tablename__ = "Story"
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String)
    Story= db.Column('content', db.String)
    #  name = Column(String)

    def __init__(self, name, content):
        self.name = name
        self.content = content



class User(db.Model):
    __tablename__="User"
    id=db.Column('id',db.Integer, primary_key=True)
    email=db.Column('email',db.String)
    name=db.Column('Name',db.String)
    password=db.Column('password',db.Integer)
    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password= password


class Review(db.Model):
    """docstring for ClassName"""
    __tablename__="Review"
    id=db.Column('id',db.Integer, primary_key=True)
    name=db.Column('name',db.String)
    review=db.Column('revirew',db.String)
    def __init__(self, name,revirew):
        self.name = name
        self.revirew = revirew







db.create_all()

# Set "homepage" to index.html
@app.route('/')
def main():
    return render_template('main.html')

@app.route('/all_stories/')
def all_stories():
    #stories = Story.query(Story).all()
    #Stor=Story()
    return render_template('all_stories.html')#, stories=stories#)

@app.route('/review/')
def Review():
   # if Review.query.all()!=None:
    #    review= Review.query.all()
     #   return render_template('review.html',review=review)
    return render_template('review.html')



    if request.method=='GET':    
        return render_template('postre.html')
    elif request.method=="POST":
        name=request.form['name']
        story=request.form['story']
        user=User(name=name,story=story)
        db.session.add(Story)
        db.session.commit()
        return redirect(url_for('all_stories'))    

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post')
def post_Story():
   # return render_template('post.html')   
    if request.method=='GET':    
        return render_template('post.html')
    elif request.method=="POST":
        name=request.form['name']
        story=request.form['story']
        user=User(name=name,story=story)
        db.session.add(Story)
        db.session.commit()
        return redirect(url_for('all_stories'))    

@app.route('/post_review', methods=["POST","GET"])
def post_review():
     if request.method=='GET':    
        return render_template('postre.html')
    #elif request.method=="POST":
        name=request.form['name']
        story=request.form['Review']
        user=User(name=name,review=Review)
        db.session.add(Review)
        db.session.commit()
        return redirect(url_for('Review'))  


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method=='GET':
        return render_template('login.html')
    user=db.session.query(User).filter_by(email=request.form['email']).one()
    if user.password==request.form['password'].one():
        login_session['name']=user.name
        return render_template('login.html')

@app.route('/sign_up', methods=["POST", "GET"])
def sign_up():
    if request.method=='GET':
        return render_template('signup.html')
    elif request.method=="POST":
        email=request.form['email']
        name=request.form['name']
        password=request.form['psw']
        password2=request.form['psw-repeat']
        if password!=password2:
            print('passwords are diffrent')
            return render_template('signup.html')
        user=User(email=email,name=name,password=password)
        db.session.add(user)
        db.session.commit() 
        return redirect(url_for('main'))
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