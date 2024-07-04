from django.db import connection
from .models import PriceReport, Stores

def get_local_prices(product_id, lat, lon, rad):
    query ='''
    WITH latest_price_report AS (
        SELECT price_reports.*, 
            ROW_NUMBER() OVER(PARTITION BY store_id ORDER BY created_at DESC) AS rn
        FROM price_reports 
        WHERE product_id = %s)
    SELECT pr.price_id, pr.price, st.store_id, st.store_name, st.lat, st.lon, ST_Distance(
        ST_SetSRID(ST_MakePoint(%s, %s), 4326)::geography,
        ST_SetSRID(ST_MakePoint(st.lon, st.lat), 4326)::geography
    ) AS distance FROM latest_price_report pr
    INNER JOIN stores st ON pr.store_id = st.store_id
    WHERE pr.rn = 1 
    AND ST_DWithin(
    ST_SetSRID(ST_MakePoint(%s, %s), 4326)::geography, 
    ST_SetSRID(ST_MakePoint(st.lon, st.lat), 4326)::geography, 
    %s
    )
    ORDER BY distance;
    
    '''

    params = [product_id, lon, lat, lon, lat, rad]
    
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        results = cursor.fetchall()

    price_reports = []
    for row in results:
        price_report = {
            'price_id': row[0],
            'price': row[1],
            'store_id': row[2],
            'store_name': row[3],
            'latitude': row[4],
            'longitude': row[5],
            'distance': row[6]
        }
        price_reports.append(price_report)
    
    return price_reports

def get_local_stores(lat, lon, rad):
    query = '''
    SELECT stores.*, ST_Distance(
        ST_SetSRID(ST_MakePoint(%s, %s), 4326)::geography,
        ST_SetSRID(ST_MakePoint(stores.lon, stores.lat), 4326)::geography
    ) AS distance 
    FROM stores
    WHERE ST_DWithin(
        ST_SetSRID(ST_MakePoint(%s, %s), 4326)::geography, 
        ST_SetSRID(ST_MakePoint(stores.lon, stores.lat), 4326)::geography, 
        %s
    )
    ORDER BY distance;
    '''

    params = [lon, lat, lon, lat, rad]

    with connection.cursor() as cursor:
        cursor.execute(query, params)
        results = cursor.fetchall()

    local_stores = []
    for row in results:
        local_store = {
            "store_id" : row[0],
            "store_name" : row[1],
            "lat" : row[2],
            "lon" : row[3],
            "monday" : row[4],
            "tuesday" : row[5],
            "wednesday" : row[6],
            "thursday" : row[7],
            "friday" : row[8],
            "saturday" : row[9],
            "sunday" : row[10],
            "distance" : row[11],
        }
        local_stores.append(local_store)
        
    return local_stores
    




