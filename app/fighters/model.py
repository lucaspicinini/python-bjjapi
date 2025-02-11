from app.db import db

class Fighter(db.Model):
    __tablename__ = 'lutadores'

    id: int = db.Column(db.Integer, primary_key=True)
    slug: str = db.Column(db.String, nullable=False, unique=True)
    full_name: str = db.Column(db.String(255))
    nickname: str = db.Column(db.String(4096))
    biography: str = db.Column(db.Text(255))
    weight_division: str = db.Column(db.String(255))
    image_url: str = db.Column(db.String(255))

    # Relationship
    achievements = db.relationship('Achievement', backref='fighter', lazy='dynamic')
    lineages = db.relationship('Lineage', backref='fighter', lazy='dynamic')
    team_id: int = db.Column(db.Integer, db.ForeignKey('equipes.id'), nullable=False)

    def dto(self):
        return {
            'slug': self.slug,
            'full_name': self.full_name,
            'nickname': self.nickname,
            'biography': self.biography,
            'weight_division': self.weight_division,
            'image_url': self.image_url,
            'team': self.team.name,
            'lineages': [lineage.name for lineage in self.lineages],
            'achievements': [achievement.name for achievement in self.achievements],
        }