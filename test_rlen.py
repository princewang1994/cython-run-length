from rlen import make_submission

if __name__ == '__main__':
    import pickle
    pkl_path = 'train.pkl'
    data = pickle.load(open(pkl_path, 'rb'))
    masks, name = data['masks'], data['names']
    make_submission(masks, name, fast=True, path='fast_submission.csv')
    make_submission(masks, name, fast=False, path='slow_submission.csv')
