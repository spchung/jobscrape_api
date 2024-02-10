from shared.connection import db
from shared.models import Job
from sqlalchemy import select
from .config import search_config

def get_config(version):
    return search_config[version]['emb_func'], search_config[version]['table']

def search_title(title, version='l6'):
    emb_func, entity = get_config(version)
    search_emb = emb_func(title)
    db.session.execute(select(entity))
    rows = db.session.execute(select(entity.job_id).order_by(entity.title_emb.l2_distance(search_emb)).limit(5))
    query = db.session.query(Job).filter(Job.job_id.in_([row[0] for row in rows]))
    return [job.to_dict() for job in query.all()]

def search_description(description, version='l6'):
    emb_func, entity = get_config(version)
    search_emb = emb_func(description)
    db.session.execute(select(entity))
    rows = db.session.execute(select(entity.job_id).order_by(entity.description_emb.l2_distance(search_emb)).limit(5))
    query = db.session.query(Job).filter(Job.job_id.in_([row[0] for row in rows]))
    return [job.to_dict() for job in query.all()]

def search_title_and_description(title, description, version='l6'):
    emb_func, entity = get_config(version)
    title_emb = emb_func(title)
    description_emb = emb_func(description)
    db.session.execute(select(entity))
    rows = db.session.execute(select(entity.job_id).order_by(entity.title_emb.l2_distance(title_emb)).limit(100))
    rows = db.session.execute(
        select(entity.job_id).filter(
            entity.job_id.in_([row[0] for row in rows])
        ).order_by(
            entity.description_emb.l2_distance(description_emb)
        ).limit(10))
    
    query = db.session.query(Job).filter(Job.job_id.in_([row[0] for row in rows]))
    return [job.to_dict() for job in query.all()]