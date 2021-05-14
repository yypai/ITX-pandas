import plotly.graph_objects as go

def plot_plotly(files, x, y, sep = ','):
    fig = go.Figure()
    for file in files:
        df = pd.read_csv(file, sep = sep)
        fig.add_trace(go.Scatter(x=df[x], y=df[y], name = file))
        
    fig.update_layout(template='plotly_white')
    
    fig.update_layout(
    title="Plot Title",
    xaxis_title=x,
    yaxis_title=y,
    legend_title="Legend Title",
    font=dict(
        family="Sans-Serif",
        size=18,
        color="Black"
    ))
 
    fig.show()   
