# https://www.youtube.com/watch?v=PqUaDvbczbI
import pandas as pd
import plotly.express as px

AnnualTicketSales = pd.read_csv("AnnualTicketSales.csv")
df = pd.read_csv('AnnualTicketSales.csv')
# fig = px.box(df,
#              y='TOTAL BOX OFFICE',
#              title='Box & Whisker Plot of Total Box Office',
#              hover_data=['YEAR']
#              )

fig = px.scatter(df, x='YEAR', y='TICKETS SOLD', title='TICKETS SOLD vs YEAR')
fig.show()