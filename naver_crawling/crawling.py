from bs4 import BeautifulSoup as bs
import requests
import gevent.pool

pool = gevent.pool.Pool(10)

HEADERS = {'User-Agent': 'Mozilla/5.0'}

def main():
    url = 'https://www.naver.com'
    total = get_keyword(url)
    print_json(total)
    return

def get_keyword(url):
    req = requests.get(url, headers = HEADERS)
    html = req.text
    soup = bs(html, 'html.parser')
    keywords = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul > li > .ah_a')
    answer = {'url':[], 'rank':[], 'word':[], 'related':[]}
    for keyword in keywords:
        answer['url'].append(keyword.get('href'))
        answer['rank'].append(keyword.select('.ah_r')[0].get_text())
        answer['word'].append(keyword.select('.ah_k')[0].get_text())

    answer['related'] = list(pool.map(get_relateds, keywords))

    return answer

def get_relateds(href):

    req = requests.get(href.get('href'), headers = HEADERS)
    html = req.text
    soup = bs(html, 'html.parser')
    keywords = soup.select('#nx_related_keywords > dl > dd.lst_relate._related_keyword_list > ul > li > a')

    return [keyword.get_text() for keyword in keywords]

def print_json(total):
    print(len(total))
    for i, v in enumerate(total['rank']):
        print(total['rank'][i], total['word'][i])
        print(total['related'][i])
    return

if __name__ == '__main__':
    main()
