# https://www.youtube.com/watch?v=_b2KXL0wHQg
"""
1. How to create any chart you want using plotly documentation: 3 steps that I use for creating powerful graphs & charts with Plotly:
    a. Initiate your graph with Plotly sample code, and adapt it to your data
        (https://plotly.com/python)
    b. Enhance your graph with Plotly Express High-level interface
        (https://plotly.com/python-api-reference/plotly.express.html)
    c. Customize your graphs with Plotly Graph_Objects, using fig.Updates
        (https://plotly.com/python/reference/index/)
            i. Layout represents the chart (frames, title, color, tick, hover, legend)
            ii. Traces are representing the data (inside the layout)

    d.
            i. update_traces
            ii. update_layout
            iii. update_annotations
            iv. update_yaxes
            v. update_xaxes

2. Get stuck:
    a. Use Plotly Fundamentals documentation (https://plotly.com/python/plotly-fundamentals/)
    b. Use Plotly Forum (https://community.plotly.com/)

3. How to share your charts with others
    a. Dash and deploy to web using Heroku
    b. Kaleido(https://plotly.com/python/static-image-export/)
"""
#########################################################################################
# Step numer 1 - Initiate your graph with Plotly sample code, and adapt it to your data #
# (https://plotly.com/python)                                                           #
#########################################################################################
import pandas as pd
import plotly.express as px
dfb = pd.read_csv("bird-window-collision-death.csv")

df = px.data.tips()
fig = px.pie(dfb, values='Deaths', names='Bldg #')
fig.write_image("images/fig1.png")
#fig.show()


#################################################################
# Enhance your graph with Plotly Express High-level interface   #
# (https://plotly.com/python-api-reference/plotly.express.html) #
#################################################################
dfb = pd.read_csv("bird-window-collision-death.csv")

# df = px.data.tips()
# fig = px.pie(dfb, values='Deaths', names='Bldg #', color="Side", hole=0.3)
# fig.show()


######################################################################
# Customize your graphs with Plotly Graph_Objects, using fig.Updates #
# (https://plotly.com/python/reference/index/)                       #
######################################################################
"""
To further customize your graph using graph objects you'll have to do fig.update_ (mostly used will be traces and layout) the difference between the two is layout represents as you
can see here 
    + layout represents the attributes or the charts so it represents the color the tick the hover the legend, really how to different ways that you can change the chart
      so i embellishes it and looks prettier and more user-friendly for your user and yourself. 
    + Traces represtents the data very important to remember, traces represents the data that goes inside the layout 
"""
fig = px.pie(dfb, values='Deaths', names='Bldg #', color="Side", hole=0.3)
fig.update_traces(textinfo="label+percent", insidetextfont=dict(color="white"))
#fig.update_layout(legend={"itemclick": True})
fig.show()