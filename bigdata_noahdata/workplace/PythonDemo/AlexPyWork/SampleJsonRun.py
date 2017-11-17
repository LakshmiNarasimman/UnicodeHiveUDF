'''
Created on 10-Nov-2017

@author: bigdata
'''
import json 
# json_list=[{u'list_price': 14.95, u'deal_id': None, u'objectID': u'B0727TZSS8', u'color': None, u'num_ratings': 5.0, u'collection_type': [u'bestseller'], u'category_breadcrumb': [u'Home & Kitchen', u'Kitchen & Dining', u'Kitchen Utensils & Gadgets', u'Fruit & Vegetable Tools', u'Corers & Pitters', u'Corers'], u'size': None, u'sku': u'B0727TZSS8', u'title': u'Pineapple Corer Slicer - Stainless Steel Kitchen Peeler with Blades for Diced Fruit Rings by La Maison TM', u'best_offer_url': None, u'is_best_seller': True, u'request_status': None, u'click_count': 0, u'best_offer_price': None, u'brand': None, u'store': u'amazon', u'ranking': 0, u'description': u'Pineapple Corer and and Fruit Slicer Tool - Stainless Steel Silver Peeler with Blades for Diced Fruit Rings - By La Maison TM\nLa Maison is\nVoted\n#1 best pineapple corer and fruit cutter on the USA market\nLa Maison brings you another high quality product to compliment your kitchenware. Slice away to your hearts content with no mess and no fuss.\nYour Pineapple slicer will peel, core, and slice a fresh pineapple in under 30 seconds.\nThis fruit de-corer peeler removes perfectly formed rings while leaving the core in the shell.\nMade with premium stainless steel making it strong sturdy and durable.\nThe Sharp, medium-sized, stainless steel blade is shaped for compact storage.\nThe serrated blades gently cut through the pineapple.\nThe handle is made with a superior quality plastic, offering you a comfortable non-slip grip.\nAll material are BPA free and Dishwasher safe.\nSuper Easy Clean-up! The Knob and slicer separate with the press of a button for easy cleaning.\nA simple yet beautiful design that makes it easy for anyone to just grip, turn, and slice!\nWe offer a 100% satisfactory guarantee! If for any reason whatsoever you are unhappy with your product, feel free to return it for a full refund no questions asked and no hard feelings.', u'image_url_array': [u'https://images-na.ssl-images-amazon.com/images/I/51NzeA4uJOL.jpg', u'https://images-na.ssl-images-amazon.com/images/I/61uP6iowHgL._SL1000_.jpg', u'https://images-na.ssl-images-amazon.com/images/I/81-vzGgq6vL._SL1500_.jpg', u'https://images-na.ssl-images-amazon.com/images/I/61uEVdME1eL._SL1074_.jpg', u'https://images-na.ssl-images-amazon.com/images/I/71gS38anC4L._SL1500_.jpg', u'https://images-na.ssl-images-amazon.com/images/I/71vNdsiC10L._SL1500_.jpg'], u'price_cat_id': 21624.0, u'prime_eligible': False, u'filter_label': None, u'product_url': u'https://www.amazon.com/dp/B0727TZSS8/?th=1&psc=1', u'num_reviews': 8, u'top_keywords': [], u'gender': None, u'age': None, u'offer_price': 5.95, u'upc': None, u'pdp_url': None, u'best_offer_affiliate_url': None, u'image_url': u'https://images-na.ssl-images-amazon.com/images/I/51NzeA4uJOL.jpg', u'fav_count': 0, u'request_id': None, u'price_category': u'Home & Kitchen > Kitchen & Dining > Kitchen Utensils & Gadgets', u'price_category_crumb': None},
# {u'list_price': None, u'deal_id': None, u'objectID': u'B071S59K6R', u'color': None, u'num_ratings': 5.0, u'collection_type': [u'bestseller'], u'category_breadcrumb': None, u'size': None, u'sku': u'B071S59K6R', u'title': u'Peter Pan (DVD, 2007, 2-Disc Set, Platinum Edition) Brand New', u'best_offer_url': None, u'is_best_seller': True, u'request_status': None, u'click_count': 0, u'best_offer_price': None, u'brand': None, u'store': u'amazon', u'ranking': 0, u'description': u"Detailed item info\n\nJoin mischievous Peter Pan, the young boy who refuses to grow up, his hot-tempered pixie pal, Tinker Bell and the Darling children as they soar away to the mysterious Never-Never land where childhood lasts forever in this magical, musical adventure. Based on J.M. Barrie's 1904 book.", u'image_url_array': [u'https://images-na.ssl-images-amazon.com/images/I/71TplDlOd0L._SL1000_.jpg'], u'price_cat_id': 18597.0, u'prime_eligible': False, u'filter_label': None, u'product_url': u'https://www.amazon.com/dp/B071S59K6R/?th=1&psc=1', u'num_reviews': 8, u'top_keywords': [], u'gender': None, u'age': None, u'offer_price': 11.59, u'upc': None, u'pdp_url': None, u'best_offer_affiliate_url': None, u'image_url': u'https://images-na.ssl-images-amazon.com/images/I/71TplDlOd0L._SL1000_.jpg', u'fav_count': 0, u'request_id': None, u'price_category_crumb': None},
# {u'list_price': 49.99, u'deal_id': None, u'objectID': u'B071HL77XS', u'color': None, u'num_ratings': 5.0, u'collection_type': [u'bestseller'], u'category_breadcrumb': [u'Home & Kitchen', u'Kitchen & Dining', u'Cutlery & Knife Accessories', u'Paring Knives'], u'size': None, u'sku': u'B071HL77XS', u'title': u'Paring Knife 4 Inch Fruit Knife Small Kitchen Knife Vegetable Cutlery Stainless Steel Forged Blade Ultra Sharp Ergonomic Handle Non Slip Cooks Knives', u'best_offer_url': None, u'is_best_seller': True, u'request_status': None, u'click_count': 0, u'best_offer_price': None, u'brand': None, u'store': u'amazon', u'ranking': 0, u'description': u'100% Satisfaction Guarantee, Lifetime Warranty, Just try it\n\nThis Classic 4 inch paring knife is perfect for your small subtly cutting tasks, it can help you peel, slice, cut, core and garnish your fruits and vegetables\n\nFeatures and Benefits\n1. Ideal for peeling, cutting or garnishing fruit and vegetables\n2. Premium German stainless steel\n3. Anti-corrosion and anti-stain\n4. Precisely forged and wear-resistant\n5. Ultra-sharp edge to make your slicing more easily and smoothly\n6. Protective finger guard\n7. Elaborately polished spine to ensure a comfortable pinch grip\n8. Triple riveted allowing more durability\n9. Specially designed bolster to protect your safety\n10. Easy to clean with low maintenance\n\nSpecifications\n1. Blade material: X50 CrMoV15\n2. Handle material: ABS + 430 Stanless Steel\n3. HRC(Rockwell Hardness): 58\n4. Knife total length: 8.8 inch\n5. Blade length: 4 inch\n6. Blade thickness: 0.08 inch\n7. Blade width:0.75 inch\n8. Knife weight: 0.27 lb\n9. Knife edge angle: 17 degrees\n\nCare and Use\n1. Please avoid the direct contact with the edge, do not test it by fingers and keep it away from children\n2. Keep the knife dry and clean with a soapy cloth after each use\n3. Safe for dishwasher, in order to keep knife\u2019s lifespan, hand washing is recommended\n4. Knives can be honed after several times uses with a honing steel, which can help keep knives sharp as always\n\nIncludes\n1* 4 Inch paring knife\n1* Protective tip guard\n1* Packaging box\n', u'image_url_array': [u'https://images-na.ssl-images-amazon.com/images/I/71Uav6P7q8L._SL1500_.jpg', u'https://images-na.ssl-images-amazon.com/images/I/71M-X4SjwlL._SL1500_.jpg', u'https://images-na.ssl-images-amazon.com/images/I/71dtmvKFw6L._SL1500_.jpg', u'https://images-na.ssl-images-amazon.com/images/I/81FRR%2Bous%2BL._SL1500_.jpg', u'https://images-na.ssl-images-amazon.com/images/I/71wkRmvdyzL._SL1500_.jpg', u'https://images-na.ssl-images-amazon.com/images/I/71qiYfDbknL._SL1500_.jpg', u'https://images-na.ssl-images-amazon.com/images/I/71xQchud8DL._SL1500_.jpg'], u'price_cat_id': 18549.0, u'prime_eligible': False, u'filter_label': None, u'product_url': u'https://www.amazon.com/dp/B071HL77XS/?th=1&psc=1', u'num_reviews': 8, u'top_keywords': [], u'gender': None, u'age': None, u'offer_price': 19.99, u'upc': None, u'pdp_url': None, u'best_offer_affiliate_url': None, u'image_url': u'https://images-na.ssl-images-amazon.com/images/I/71Uav6P7q8L._SL1500_.jpg', u'fav_count': 0, u'request_id': None, u'price_category': u'Home & Kitchen > Kitchen & Dining > Kitchen Knives & Cutlery Accessories', u'price_category_crumb': None}]
# json_data=json.loads(json.dumps(json_list))
# # for cb in json_data:
# #     #print "category_breadcrumb:", cb['category_breadcrumb']
# #     print "price_category:", cb['price_category']
# fil_list=[]
# for cb in json_data:    
#     if((cb["category_breadcrumb"]!=None) and (cb["category_breadcrumb"]!='')):
#         if(not cb.get('price_category')):
#             cb['price_category']=cb.get('category_breadcrumb')
#         cb['price_category']=cb.get('category_breadcrumb')
#         fil_list.append(cb)
# for x in fil_list:
#     print x        

# import pandas as pd
# import numpy as np
# 
# exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
#         'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
#         'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#         'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# 
# df = pd.DataFrame(exam_data , index=labels)
# print("Select specific columns and rows:")
# print(df.ix[[1, 3, 5, 6], ['name', 'score']])

print '{} {}'.format('Python', 'Format')
print '{1} {0}'.format('Python', 'Format')
print '{:>15}'.format('Python')
print '{:15}'.format('Python')

print '{:>{}}'.format('Pyhton',15)
print '{:^16}'.format('Python')
print '{:.10}'.format('Python Tutorial')
print '{:05.2f}'.format(5.12345678123)
from datetime import datetime
print '{:%Y-%m-%d %H:%M}'.format(datetime(2016, 7, 26, 3, 57))
