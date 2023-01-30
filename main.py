#1 pip install requests
#2
import requests
import json

def get_data():


    cookies = {
        '__lhash_': '640b78f4bf38ddb2b0828c0351793663',
        'MVID_ACTOR_API_AVAILABILITY': 'true',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CART_AVAILABILITY': 'true',
        'MVID_CATALOG_STATE': '1',
        'MVID_CITY_ID': 'CityCZ_975',
        'MVID_CREDIT_AVAILABILITY': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GIFT_KIT': 'true',
        'MVID_GLC': 'true',
        'MVID_GLP': 'true',
        'MVID_GTM_ENABLED': '011',
        'MVID_IMG_RESIZE': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '7700000000000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MCLICK': 'true',
        'MVID_MCLICK_NEW': 'true',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_MINI_PDP': 'true',
        'MVID_MULTIOFFER': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_REGION_ID': '1',
        'MVID_REGION_SHOP': 'S002',
        'MVID_SERVICES': '111',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_WEBP_ENABLED': 'true',
        'MVID_WEB_SBP': 'true',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        '_gid': 'GA1.2.1337817062.1674901155',
        '_sp_ses.d61c': '*',
        '_ym_uid': '1674901155148031673',
        '_ym_d': '1674901155',
        '_ga': 'GA1.2.1768453920.1674901155',
        '_ym_isad': '2',
        '__SourceTracker': 'google__organic',
        'admitad_deduplication_cookie': 'google__organic',
        'SMSError': '',
        'authError': '',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': '246e257a-1b3a-40a9-847d-d297702d668a',
        'tmr_lvid': '61b4b78c575c6746283b15f3e5bbdc80',
        'tmr_lvidTS': '1674901157904',
        'advcake_track_id': 'd8f204e1-2554-c6b5-7bb5-837e7b56f799',
        'advcake_session_id': 'c2172a7e-d134-59df-84b6-901e26b3d318',
        'uxs_uid': '395f33b0-9ef5-11ed-9f6e-4d9b53e2e0b9',
        'afUserId': '4a86fd68-0a57-4124-9dba-5aad43f0e65d-c',
        'AF_SYNC': '1674901158753',
        'flocktory-uuid': 'b53ffc41-a288-4221-b8b8-1ad191bff1b5-1',
        'tmr_detect': '0%7C1674901161857',
        'flacktory': 'no',
        'BIGipServeratg-ps-prod_tcp80': '1812257802.20480.0000',
        'bIPs': '434929338',
        '_dc_gtm_UA-1873769-1': '1',
        '_dc_gtm_UA-1873769-37': '1',
        '_sp_id.d61c': '7589f5ad-d876-47dc-8f72-fcf2377910b0.1674901155.1.1674901266..8f95b561-472a-4745-85d3-1ea054822bee..643fc3a4-907f-49e1-a489-bcfea0b83bf8.1674901154740.22',
        '_ga_CFMZTSS5FM': 'GS1.1.1674901154.1.1.1674901274.0.0.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1674901155.1.1.1674901274.60.0.0',
        'MVID_ENVCLOUD': 'prod1',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'baggage': 'sentry-transaction=%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=6b47cadfe845472eb24265f208e1a6e4,sentry-sample_rate=0.5',
        # 'cookie': '__lhash_=640b78f4bf38ddb2b0828c0351793663; MVID_ACTOR_API_AVAILABILITY=true; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CART_AVAILABILITY=true; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_975; MVID_CREDIT_AVAILABILITY=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GIFT_KIT=true; MVID_GLC=true; MVID_GLP=true; MVID_GTM_ENABLED=011; MVID_IMG_RESIZE=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7700000000000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MCLICK_NEW=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_MULTIOFFER=true; MVID_NEW_ACCESSORY=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_TIMEZONE_OFFSET=3; MVID_WEBP_ENABLED=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; _gid=GA1.2.1337817062.1674901155; _sp_ses.d61c=*; _ym_uid=1674901155148031673; _ym_d=1674901155; _ga=GA1.2.1768453920.1674901155; _ym_isad=2; __SourceTracker=google__organic; admitad_deduplication_cookie=google__organic; SMSError=; authError=; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=246e257a-1b3a-40a9-847d-d297702d668a; tmr_lvid=61b4b78c575c6746283b15f3e5bbdc80; tmr_lvidTS=1674901157904; advcake_track_id=d8f204e1-2554-c6b5-7bb5-837e7b56f799; advcake_session_id=c2172a7e-d134-59df-84b6-901e26b3d318; uxs_uid=395f33b0-9ef5-11ed-9f6e-4d9b53e2e0b9; afUserId=4a86fd68-0a57-4124-9dba-5aad43f0e65d-c; AF_SYNC=1674901158753; flocktory-uuid=b53ffc41-a288-4221-b8b8-1ad191bff1b5-1; tmr_detect=0%7C1674901161857; flacktory=no; BIGipServeratg-ps-prod_tcp80=1812257802.20480.0000; bIPs=434929338; _dc_gtm_UA-1873769-1=1; _dc_gtm_UA-1873769-37=1; _sp_id.d61c=7589f5ad-d876-47dc-8f72-fcf2377910b0.1674901155.1.1674901266..8f95b561-472a-4745-85d3-1ea054822bee..643fc3a4-907f-49e1-a489-bcfea0b83bf8.1674901154740.22; _ga_CFMZTSS5FM=GS1.1.1674901154.1.1.1674901274.0.0.0; _ga_BNX5WPP3YK=GS1.1.1674901155.1.1.1674901274.60.0.0; MVID_ENVCLOUD=prod1',
        'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/planshety-195/f/skidka=da/tolko-v-nalichii=da',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': '6b47cadfe845472eb24265f208e1a6e4-b68eb027eaa18657-1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'x-set-application-id': '01973fcd-abca-42f8-8bd2-df3c683df8b1',
    }

    params = {
        'categoryId': '195',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyJza2lka2EiLCIiLCJkYSJd',
            'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        ],
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                            headers=headers).json()
    # print(response)

    products_ids = response.get('body').get('products')

    with open('1_products_ids.json', 'w') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)

    # print(products_ids)
    json_data = {
        'productIds': products_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': True,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                             json=json_data).json()
    with open('2_items.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    # print(len(response.get('body').get('products')))
    products_ids_str = ','.join(products_ids)

    params = {
        'productIds': products_ids_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
                            headers=headers).json()
    with open('3_prices.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    items_prices = {}
    material_prices = response.get('body').get('materialPrices')
    for item in material_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_sale_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')
        items_prices[item_id] = {'item_base_price': item_base_price,
                                 'item_sale_price': item_sale_price,
                                 'item_bonus': item_bonus}

    with open('4_items_prices.json', 'w') as file:
        json.dump(items_prices, file, indent=4, ensure_ascii=False)
def get_result():
    global prices
    with open('2_items.json') as file:
        products_data = json.load(file)
    with open('4_items_prices.json') as file:
        products_prices = json.load(file)
    products_data = products_data.get('body').get('products')

    for item in products_data:
        product_id = item.get('productId')
        if product_id in products_prices:
            prices = products_prices[product_id]

        item['item_base_price'] = prices.get('item_base_price')
        item['item_sale_price'] = prices.get('item_sale_price')
        item['item_bonus'] = prices.get('item_bonus')

    with open('5_result.json', 'w') as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)



def main():
    get_data()
    get_result()


if __name__ == '__main__':
    main()

