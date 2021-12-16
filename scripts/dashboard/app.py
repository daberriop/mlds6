import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from sklearn.manifold import TSNE
from digitallistening.models.model import *
from digitallistening.database.data_manager import *

app = dash.Dash(__name__)

data = load_data_from_parquet()
clean_text = data["CONTENT_CLEAN"]
predictions = predict(clean_text)

tokenized_clean_text = get_tokenized_corpus(clean_text) 
w2v_model = get_w2v_model(tokenized_clean_text)
X_w2v = get_w2v_repr(tokenized_clean_text,w2v_model)

tsne = TSNE(
    n_components = 3,
    random_state = 0,
    n_iter = 1000,
    perplexity = 2,
    verbose = 1
)

T = tsne.fit_transform(X_w2v)

fig = px.scatter_3d(x=T[:,0],y=T[:,1],z=T[:,2],color=predictions, width=1200, height=600)
fig.update_traces(marker_size=2)
fig.show()

app.layout = html.Div(children=[
    html.H1(
        children='Mejora escucha digital de clientes'
    ),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
