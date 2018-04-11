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
    #ix = index.open_dir("indexdir")
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


schema = create_schema()
if not os.path.exists("indexdir"):
    os.mkdir("indexdir")
    #static_index()

ix = index.create_in("indexdir", schema)
add_pdf(u'1',u'COMPACT NEURAL NETWORKS BASED ON THE MULTISCALE ENTANGLEMENT RENORMALIZATION ANSATZ',u'This paper demonstrates a method for tensorizing neural networks')
add_pdf(u'2',u'Weakly Supervised Action Localization by Sparse Temporal Pooling Network',u'We propose a weakly supervised temporal action local- ization algorithm on untrimmed videos using convolutional neural networks')
add_pdf(u'3',u'A Robust Real-Time Automatic License Plate Recognition based on the YOLO Detector',u'Automatic License Plate Recognition (ALPR) has been a frequent topic of research due to many practical ap- plications. MULTISCALE')
while True:
    query= input()
    result = search(query,"title","abstract")
    print(result)





