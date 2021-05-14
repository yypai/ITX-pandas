import plotly.graph_objects as go
def plot_plotly(files, x, y, sep = ',', 
                plot_title = 'title', legend_tile = 'legend', 
                filename = 'export.html'):
    fig = go.Figure()
    for file in files:
        df = pd.read_csv(file, sep = sep)
        fig.add_trace(go.Scatter(x=df[x], y=df[y].rolling(1).mean(), name = file))
        
    fig.update_layout(template='plotly_white')
    fig.update_layout(
        title=plot_title,
        xaxis_title=x,
        yaxis_title=y,
        legend_title=legend_tile,
        font=dict(
            family="Sans-Serif",
            size=18,
            color="Black"
        ))
    fig.write_html(filename)
    fig.show()   
