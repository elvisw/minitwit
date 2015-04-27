from app import db


followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.Unicode, index = True, unique = True)
    email = db.Column(db.String, index = True, unique = True)
    pw_hash = db.Column(db.String)
    message = db.relationship('Message', backref='author', lazy='dynamic')
    followed = db.relationship('User',
        secondary = followers,
        primaryjoin = (followers.c.follower_id == id),
        secondaryjoin = (followers.c.followed_id == id),
        backref = db.backref('followers', lazy = 'dynamic'),
        lazy = 'dynamic')

    @staticmethod
    def make_unique_username(username):
        if User.query.filter_by(username = username).first() == None:
            return username
        version = 2
        while True:
            new_username = username + str(version)
            if User.query.filter_by(username = new_username).first() == None:
                break
            version += 1
        return new_username

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)
            return self

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)
            return self

    def is_following(self, user):
        return self.followed.filter(followers.c.followed_id == user.id).count() > 0

    def followed_posts(self):
        return Message.query.join(followers, (followers.c.followed_id == Message.author_id)).filter(
            followers.c.follower_id == self.id).order_by(Message.pub_date.desc())

    def __repr__(self):
        return '<User %r>' % (self.username)


class Message(db.Model):
    message_id = db.Column(db.Integer, primary_key = True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    text = db.Column(db.UnicodeText)
    pub_date = db.Column(db.DateTime)

    def __repr__(self):
        return '<Message %r>' % (self.text)
