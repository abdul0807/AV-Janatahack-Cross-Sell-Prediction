TYPE = "classification"

DATA_DIR = "./"
TRAIN_FILE = "train.csv"
TEST_FILE = "test.csv"
SUBMISSION_FILE = "sample_submission.csv"

TARGET = "Response"    

ID_COLS = ['id']
DATE_COLS = []
SUBMISSION_COLS = []

EVAL_METRIC = 'auc'
def scoring(*args, **kwargs):
    from sklearn.metrics import roc_auc_score
    return roc_auc_score(*args, **kwargs)

# Feature Engineering
OHE = False
