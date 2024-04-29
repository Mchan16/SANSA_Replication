import random

def RANDOM_REC(df, k):
    """
    Takes a data frame that looks like this
    	            user_id	    item_id	    feedback	timestamp
        703224	    11980	    33446	    1.0	        1970-01-01
        2171749	    46468	    60418	    1.0	        1970-01-01
        1911328	    39358	    14564	    1.0	        1970-01-01
        222180	    2976	    7978	    1.0	        1970-01-01
        943203	    16832	    71092	    1.0	        1970-01-01
        ...         ...         ...         ...         ...
        110268	    1012	    5618	    1.0         1970-01-01
        1692743	    33736	    68914	    1.0	        1970-01-01
        2356330	    51757	    33239	    1.0	        1970-01-01
        2229084	    48035	    50699	    1.0	        1970-01-01
        2219110	    47775	    89569	    1.0	        1970-01-01
    and returns a 2-d array of random predictions
    """
    random_recs = []
    item_ids = df['item_id'].unique().tolist()
    user_ids = df['user_id'].unique().tolist()
    for _ in user_ids:
        pred = random.sample(item_ids, k)
        random_recs.append(pred)
    
    return random_recs