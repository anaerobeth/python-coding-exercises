from Bio import Entrez
import json

DB = 'pubmed'
EMAIL = 'email@example.com'
RETMODE = 'xml'
SEARCH_TERM = 'mollusk'

def search(query):
    Entrez.email = EMAIL
    handle = Entrez.esearch(db=DB,
                            sort='relevance',
                            retmax='55000',
                            retmode=RETMODE,
                            term=query)
    results = Entrez.read(handle)

    return results


def fetch_details(id_list):
    ids = ','.join(id_list)
    Entrez.email = EMAIL
    handle = Entrez.efetch(db='pubmed',
                           retmode=RETMODE,
                           id=ids)
    results = Entrez.read(handle)

    return results


if __name__ == '__main__':
    results = search(SEARCH_TERM)
    id_list = results['IdList']
    papers = fetch_details(id_list)
    f = open('mollusk.txt', 'w')

    for i, paper in enumerate(papers['PubmedArticle']):
        citation = paper['MedlineCitation']
        article = citation['Article']

        article = {
            'pmid': citation.get('PMID'),
            'article': article.get('Abstract'),
            'date': article.get('ArticleDate'),
            'authors': article.get('AuthorList'),
            'title': article.get('ArticleTitle'),
            'journal': article.get('Journal'),
        }

        f.write(json.dumps(article, indent=2, separators=(',', ':')))

    f.close()

