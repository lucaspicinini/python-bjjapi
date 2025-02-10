from app.db import db

class Lineage(db.Model):
    __tablename__ = "linhagens"

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String)
    fighter_id: int = db.Column(db.Integer, db.ForeignKey("lutadores.id"), nullable=False)

    def dto(self):
        return {
            "id": self.id,
            "name": self.name,
            "fighter": self.fighter.slug,
        }