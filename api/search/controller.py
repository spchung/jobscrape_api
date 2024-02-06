from embedding.sentence_embedding import gen_embedding
from shared.connection import db
from shared.models import JobEmbedding, Job
from sqlalchemy import select

def search_title(title):
    search_emb = gen_embedding(title)
    db.session.execute(select(JobEmbedding))
    rows = db.session.execute(select(JobEmbedding.job_id).order_by(JobEmbedding.title_emb.l2_distance(search_emb)).limit(5))
    query = db.session.query(Job).filter(Job.job_id.in_([row[0] for row in rows]))
    return [job.to_dict() for job in query.all()]

def search_description(description):
    search_emb = gen_embedding(description)
    db.session.execute(select(JobEmbedding))
    rows = db.session.execute(select(JobEmbedding.job_id).order_by(JobEmbedding.description_emb.l2_distance(search_emb)).limit(5))
    query = db.session.query(Job).filter(Job.job_id.in_([row[0] for row in rows]))
    return [job.to_dict() for job in query.all()]

def search_title_and_description(title, description):
    title_emb = gen_embedding(title)
    description_emb = gen_embedding(description)
    db.session.execute(select(JobEmbedding))
    rows = db.session.execute(select(JobEmbedding.job_id).order_by(JobEmbedding.title_emb.l2_distance(title_emb)).limit(100))
    rows = db.session.execute(
        select(JobEmbedding.job_id).filter(
            JobEmbedding.job_id.in_([row[0] for row in rows])
        ).order_by(
            JobEmbedding.description_emb.l2_distance(description_emb)
        ).limit(10))
    
    query = db.session.query(Job).filter(Job.job_id.in_([row[0] for row in rows]))
    return [job.to_dict() for job in query.all()]