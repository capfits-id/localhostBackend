from app import db
from sqlalchemy.dialects.mysql import TEXT

class FotoOutfit(db.Model):
    id_foto = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    id_outfit = db.Column(db.BIGINT, db.ForeignKey("outfit.id_outfit"), nullable=False)
    foto = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return '<Foto {}>'.format(self.foto)
