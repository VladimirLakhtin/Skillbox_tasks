from main import db, Base
# from sqlalchemy_imageattach.entity import Image, image_attachment

class Kitties(Base):

    __tablename__ = "kitties"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    breed = db.Column(db.String(50))
    description = db.Column(db.Text)
    image_url = db.Column(db.Text)    



    