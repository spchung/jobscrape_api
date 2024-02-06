from shared.connection import db
from shared.models import Job

def get_job_by_id(job_id):
    row = db.session.query(Job).filter(Job.job_id == job_id).first()
    return row.to_dict() if not row is None else None

def query_jobs(
    job_id=None,
    company_id=None,
    title=None,
    job_type=None,
    location=None,
    salary=None,
    experience=None,
    education_restriction=None,
    subject_restriction=None,
    work_skills=None,
    technical_skills=None,
    addition_requirements=None,
    description=None,
    last_updated=None,
    source=None
):
    query = db.session.query(Job)
    if job_id:
        query = query.filter(Job.job_id == job_id)
    if company_id:
        query = query.filter(Job.company_id == company_id)
    if title:
        query = query.filter(Job.title.like(f'%{title}%'))
    if job_type:
        query = query.filter(Job.job_type.like(f'%{job_type}%'))
    if location:
        query = query.filter(Job.location.like(f'%{location}%'))
    if salary:
        query = query.filter(Job.salary.like(f'${salary}%'))
    if experience:
        query = query.filter(Job.experience.like(f'${experience}%'))
    if education_restriction:
        query = query.filter(Job.education_restriction.like(f'${education_restriction}%'))
    if subject_restriction:
        query = query.filter(Job.subject_restriction.like(f'${subject_restriction}%'))
    if work_skills:
        query = query.filter(Job.work_skills.like(f'${work_skills}%'))
    if technical_skills:
        query = query.filter(Job.technical_skills.like(f'${technical_skills}%'))
    if addition_requirements:
        query = query.filter(Job.addition_requirements.like(f'${addition_requirements}%'))
    if description:
        query = query.filter(Job.description.like(f'${description}%'))
    if last_updated:
        query = query.filter(Job.last_updated.like(f'${last_updated}%'))
    if source:
        query = query.filter(Job.source == source)
    
    query.order_by(Job.last_updated.desc())

    return [row.to_dict() for row in query.all()]