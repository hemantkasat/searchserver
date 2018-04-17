import os, os.path
from whoosh import index
from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED
from whoosh.analysis import StemmingAnalyzer
from whoosh.qparser import QueryParser, MultifieldParser
import whoosh.index as index

def create_schema():
    schema = Schema(docid=ID(stored=True),
                title=TEXT(stored=True, analyzer=StemmingAnalyzer()),
                abstract=TEXT(stored=True, analyzer=StemmingAnalyzer()))
    return schema

def add_pdf(docid, title, abstract):
    writer = ix.writer()
    writer.add_document(docid=docid, title=title, abstract=abstract)
    writer.commit()
def search(query, type1, type2):
    ix = index.open_dir("indexdir")
    try:
        searcher = ix.searcher()
    finally:
        searcher.close()
    qp = MultifieldParser([type1,type2], schema=ix.schema)
    q = qp.parse(query)

    s= ix.searcher()
    results = s.search(q)
    result_docids=[]
    if results:
        for hit in results:
            result_docids.append(hit['docid'])
        print(results)
        return result_docids
    else:
        return None






