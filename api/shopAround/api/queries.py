from django.db import connection
from .models import PriceReport, Stores

def get_local_prices(product_id, lat, lon, rad):
    query ='''
    WITH latest_price_report AS (
        SELECT price_reports.*, 
            ROW_NUMBER() OVER(PARTITION BY store_id ORDER BY created_at DESC) AS rn
        FROM price_reports 
        WHERE product_id = %s)
    SELECT pr.price_id, pr.price, st.store_name, ST_Distance(
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
    print(results)
    for row in results:
        price_report = {
            'price_id': row[0],
            'price': row[1],
            'store_name': row[2],
            'distance': row[3]
        }
        price_reports.append(price_report)
    
    return price_reports







