import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
#print(ad_clicks.head())

views = ad_clicks.groupby('utm_source').user_id.count().reset_index()
#print(views)


### Why doesn't this work? ### ad_clicks['is_click']=ad_clicks.ad_click_timestamp.apply(lambda x: 'False' if x=='nan' else 'True') ######

ad_clicks['is_click'] = ~ad_clicks\
   .ad_click_timestamp.isnull()
print(ad_clicks)


clicks_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()
print(clicks_by_source)


clicks_pivot=clicks_by_source.pivot(columns='is_click',index='utm_source',values='user_id').reset_index()
print(clicks_pivot)


### Why doesn't this work? ### clicks_pivot['percent_clicked']=clicks_pivot['True']/(clicks_pivot['True'] + clicks_pivot['False']) ######
clicks_pivot['percent_clicked'] = \
   clicks_pivot[True] / \
   (clicks_pivot[True] + clicks_pivot[False])
print(clicks_pivot)


ab_num=ad_clicks.groupby('experimental_group').user_id.count().reset_index()
print(ab_num)


ab_click_num=ad_clicks.groupby(['experimental_group','is_click']).user_id.count().reset_index()
print(ab_click_num)


ab_pivot=ab_click_num.pivot(columns='is_click',index='experimental_group',values='user_id').reset_index()
print(ab_pivot)


ab_pivot['percent_clicked'] = \
   ab_pivot[True] / \
   (ab_pivot[True] + ab_pivot[False])
print(ab_pivot)


a_clicks = ad_clicks[ad_clicks.experimental_group=='A']
print(a_clicks)
a_by_day = a_clicks.groupby(['day','is_click']).user_id.count().reset_index()

a_pivot = a_by_day.pivot(columns='is_click',index='day',values='user_id').reset_index()

a_pivot['percent_clicked'] = \
   a_pivot[True] / \
   (a_pivot[True] + a_pivot[False])
print(a_pivot)



b_clicks = ad_clicks[ad_clicks.experimental_group=='B']
print(b_clicks)
b_by_day = b_clicks.groupby(['day','is_click']).user_id.count().reset_index()

b_pivot = b_by_day.pivot(columns='is_click',index='day',values='user_id').reset_index()

b_pivot['percent_clicked'] = \
   b_pivot[True] / \
   (b_pivot[True] + b_pivot[False])
print(b_pivot)

