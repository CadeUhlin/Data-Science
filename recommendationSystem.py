import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

data = fetch_movielens(min_rating=4.0)

# Weighted Approximate-Rank Pairwise - uses gradient descent
# Is both a Content and Collaborative method that takes the users rating of their
# movies another others rantings on the same and different movies
model = LightFM(loss='warp')

# epochs = runs & num_threads = parallel computations
model.fit(data['train'], epochs=30, num_threads=2)


def sample_recommendations(model, data, user_ids):
    num_users, num_items = data['train'].shape
    for user_id in user_ids:

        known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]
        scores = model.predict(user_id, np.arange(num_items))
        top_items = data['item_labels'][np.argsort(-scores)]

        print('Users %s' % user_id)

        print('Known positions :')
        for pos in known_positives[:5]:
            print('    %s' % pos)

        print('Recommendation:')
        for top in top_items[:5]:
            print('     %s' % top)


sample_recommendations(model, data, [3, 25, 450])
