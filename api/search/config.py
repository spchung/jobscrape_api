from embedding.sentence_embedding import gen_embedding, gen_l12_embedding
from shared.connection import db
from shared.models import JobEmbedding, JobEmbeddingL12

search_config = {
    'l6':{
        'emb_func': gen_embedding,
        'table': JobEmbedding,
    },
    'l12':{
        'emb_func': gen_l12_embedding,
        'table': JobEmbeddingL12
    }
}