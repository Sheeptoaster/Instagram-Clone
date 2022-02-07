from .db import db
from sqlalchemy.orm import relationship
from .user import likes

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    image = db.Column(db.Text, nullable=False)
    caption = db.Column(db.Text)

    user = relationship("User", foreign_keys=[user_id], overlaps="posts")
    comment = relationship("Comment", foreign_keys="Comment.post_id", overlaps="posts")

    post = relationship(
        "User",
        secondary=likes,
        back_populates="users"
    )
