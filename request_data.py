import requests as re

def request(url,params = None):
    cookies = {
        'select-state': 'AP',
        'select-city': 'S57',
        'renderid': 'rend02',
        '__cflb': '0H28uo2Z2Wgm3eS1vfqhXZwTTkt3ZjZTub19JtWiXjd',
        '__cf_bm': 'vqAOrJ6RM3oRbYUuMObNx95K3lKeCXu.CgZYxx0BhcQ-1776764652.53519-1.0.1.1-3Z..uvPFDnm__CD_E.UOuINj7cFm.7JmR2pU1ZZJ0b4MZHCP_PJDWtJlcFQ8vsC9eowtAlzL_xayfG6HNPkoPTTNwnW2EfVsEe_pj8Wl64VeiPnWojIdT2TCCCo4Ip5q',
        '_twpid': 'tw.1776764652565.766057751327398244',
        '_fbp': 'fb.1.1776764652626.91947085054929034',
        '_gid': 'GA1.2.1004716556.1776764653',
        'cookie-agree': 'true',
        '_ga': 'GA1.1.46079290.1776764653',
        'SCOUTER': 'x46nv7ajqdqo80',
        'JSESSIONID': 'node016jl35tvl8jad14v9hft55psvu1560544.node0',
        '_gcl_au': '1.1.1464931533.1776764653.1628099736.1776764730.1776764817',
        '_uetsid': 'abbafff03d6611f1a110b36412013044',
        '_uetvid': 'abbb1a603d6611f1a99ccf3ae940c63e',
        '_ga_9PSV9LG5D2': 'GS2.1.s1776764660$o1$g1$t1776764820$j48$l0$h0',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
        # 'cookie': 'select-state=AP; select-city=S57; renderid=rend02; __cflb=0H28uo2Z2Wgm3eS1vfqhXZwTTkt3ZjZTub19JtWiXjd; __cf_bm=vqAOrJ6RM3oRbYUuMObNx95K3lKeCXu.CgZYxx0BhcQ-1776764652.53519-1.0.1.1-3Z..uvPFDnm__CD_E.UOuINj7cFm.7JmR2pU1ZZJ0b4MZHCP_PJDWtJlcFQ8vsC9eowtAlzL_xayfG6HNPkoPTTNwnW2EfVsEe_pj8Wl64VeiPnWojIdT2TCCCo4Ip5q; _twpid=tw.1776764652565.766057751327398244; _fbp=fb.1.1776764652626.91947085054929034; _gid=GA1.2.1004716556.1776764653; cookie-agree=true; _ga=GA1.1.46079290.1776764653; SCOUTER=x46nv7ajqdqo80; JSESSIONID=node016jl35tvl8jad14v9hft55psvu1560544.node0; _gcl_au=1.1.1464931533.1776764653.1628099736.1776764730.1776764817; _uetsid=abbafff03d6611f1a110b36412013044; _uetvid=abbb1a603d6611f1a99ccf3ae940c63e; _ga_9PSV9LG5D2=GS2.1.s1776764660$o1$g1$t1776764820$j48$l0$h0',
    }

    

    response = re.get(url, params = params,cookies=cookies,headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(response.status_code)
        return None
    








