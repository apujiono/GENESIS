from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# Dummy data for dashboard
df = pd.DataFrame({
    'Time': ['2025-08-19 08:00', '2025-08-19 09:00', '2025-08-19 10:00'],
    'VIRAI Balance': [100, 120, 150],
    'Mining Reward': [5, 7, 10],
    'NFTs Generated': [1, 2, 3]
})

fig_balance = px.line(df, x='Time', y='VIRAI Balance', title='VIRAI Balance Over Time')
fig_mining = px.bar(df, x='Time', y='Mining Reward', title='Mining Rewards')
fig_nft = px.bar(df, x='Time', y='NFTs Generated', title='NFTs Generated')

app.layout = html.Div([
    html.H1('GENESIS v8.5 Dashboard'),
    html.H2('Yo, bro! Track your VIRAI cuan here! 🚀'),
    dcc.Graph(id='balance-graph', figure=fig_balance),
    dcc.Graph(id='mining-graph', figure=fig_mining),
    dcc.Graph(id='nft-graph', figure=fig_nft)
])

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
