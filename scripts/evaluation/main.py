# /bin/python3

from digitallistening.models.model import *
from digitallistening.database.data_manager import *
from digitallistening.preprocessing.text_preprocessing import *
import matplotlib.pyplot as plt

data = load_data_from_parquet()
clean_text = data["CONTENT_CLEAN"]
predictions = predict(clean_text)

tokenized_clean_text = get_tokenized_corpus(clean_text) 
w2v_model = get_w2v_model(tokenized_clean_text)
X_w2v = get_w2v_repr(tokenized_clean_text,w2v_model)

# +
from sklearn.manifold import TSNE

tsne = TSNE(
    n_components = 2,
    random_state = 0,
    n_iter = 1000,
    perplexity = 2,
    verbose = 1
)

T = tsne.fit_transform(X_w2v)
# -
plt.figure(figsize=(20, 15))
plt.scatter(T[:, 0], T[:, 1], c=predictions, alpha=0.4)


