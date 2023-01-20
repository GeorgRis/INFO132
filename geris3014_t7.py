import urllib.request
import json
def count_coauthors(author_id):
    names = []
    coauthors_dict = {}
    url = 'https://api.semanticscholar.org/graph/v1/author/'+author_id+'?fields=name,papers.authors'
    response = urllib.request.urlopen(url)
    text = response.read().decode()
    at = json.loads(text)

    for paper in at["papers"]:
        for name in paper["authors"]:
            names.append(name['name'])
    for coa in names:
        if coa not in coauthors_dict:
            coauthors_dict[coa] = 1
        else:
            coauthors_dict[coa] += 1
    coauthors_dict.pop(at["name"])
    return coauthors_dict


author_id = '47490276'
cc = count_coauthors(author_id)

top_coauthors = sorted(cc.items(), key=lambda item: item[1], reverse=True)

for co_author in top_coauthors[:10]:
    print(co_author)


