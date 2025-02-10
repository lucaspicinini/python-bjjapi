from app.db import db

class Team(db.Model):
    __tablename__ = "equipes"

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String, nullable=False)
    fighters = db.relationship("Fighter", backref="team", lazy="dynamic")

    def dto(self):
        return {
            "id": self.id,
            "name": self.name,
            "fighters": [fighter.slug for fighter in self.fighters],
        }