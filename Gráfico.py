import plotly.graph_objects as go
import plotly.io as pio

pio.renderers.default = 'png'

fig = go.Figure(
    data=[go.Bar(y=[2, 1, 3])],
    layout_title_text="A Figure Displayed with fig.show()"
)
fig.show()