from shared.connection import db
from sqlalchemy import Column, String
from pgvector.sqlalchemy import Vector

class Job(db.Model):
    __tablename__ = 'jobs'
    job_id = Column(String, primary_key=True, index=True)
    company_id = Column(String)
    title = Column(String)
    job_type = Column(String)
    location = Column(String)
    salary = Column(String)
    experience = Column(String)
    education_restriction = Column(String)
    subject_restriction = Column(String)
    work_skills = Column(String)
    technical_skills = Column(String)
    addition_requirements = Column(String)
    raw_html = Column(String)
    description = Column(String)
    last_updated = Column(String)
    url = Column(String)
    source = Column(String)

    def __repr__(self):
        return '<Job %r>' % self.job_id
    
    def to_dict(self):
        return {
            'job_id': self.job_id,
            'company_id': self.company_id,
            'title': self.title,
            'job_type': self.job_type,
            'location': self.location,
            'salary': self.salary,
            'experience': self.experience,
            'education_restriction': self.education_restriction,
            'subject_restriction': self.subject_restriction,
            'work_skills': self.work_skills,
            'technical_skills': self.technical_skills,
            'addition_requirements': self.addition_requirements,
            'raw_html': self.raw_html,
            'description': self.description,
            'last_updated': self.last_updated,
            'url': self.url,
            'source': self.source
        }

class JobEmbedding(db.Model):
    __tablename__ = "job_embeddings"
    job_id = Column(String, primary_key=True, index=True)
    title_emb = Column(Vector(384))
    description_emb = Column(Vector(384))

    def to_dict(self):
        return {
            "job_id": self.job_id,
            "title_emb": self.title_emb,
            "description_emb": self.description_emb
        }
