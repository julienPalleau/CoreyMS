# https://www.youtube.com/watch?v=N1GwQNatOwo&list=PLh3I780jNsiTXlWYiNWjq2rBgg3UsL1Ub&index=3
"""
How to create a bar chart
How to manipulate a bar chart
https://plotly.com/python-api-reference/generated/plotly.express.bar.html
"""
import pandas as pd
import plotly
import plotly.express as px
import plotly.io as pio

"""
excel sheet from https://www.kaggle.com/rajanand/prison-in-india/data
National Crime Records Bureau (NCRB), Govt of India has shared this dataset
"""
df = pd.read_csv("Caste.csv")
df = df[df['state_name'] == 'Maharashtra']
df = df.groupby(['year', 'gender', ], as_index=False)[['detenues', 'under_trial', 'convicts', 'others']].sum()
print(df[:5])

"""
fake margin of error, standard deviation, or 95% confidence interval
# df['err_plus'] =df['convicts']/100
# df['err_minus'] = df['convicts']/40
"""
barchart = px.bar(
    data_frame=df,
    x="year",
    y="convicts",
    color="gender",  # differentiate color of marks
    opacity=0.9,  # set opacity of markers (from 0 to 1)
    orientation="v",  # 'v', 'h': orientation of the marks
    barmode='relative',  # in 'overlay' mode, bars are on top of one another.
    # in 'group' mode, bars are placed beside each other.
    # in 'relative' mode, bars are stached above (+) or below (-) zero.
    # ------------------------------------------------------------------------------------------
    # facet_row='caste',    # assign marks to subplots in the vertical direction
    # facet_col='caste',    # assigns marks to subplots in the horizontal direction
    # facet_col_wrap=2      # maximum number of subplot columns. Do not set facet_row!
    # facet_col and facet_col_wrap can'be used with face_row!

    # color_discrete_sequence=["pink", "yellow"],           # set specific makrer colors. Color-column data anno
    # color_discrete_map={"Male": "gray", "Female":"red"},  # map you chosen colors

    # color_continuous_scale=px.colors.diverging.Picnic,  # set marker colors. When color column is numberic data
    # https://plotly.com/python/builtin-colorscales/

    # color_continuous_midpoint=3000,                         # set desired midpoint. When colors=deverging
    # range_color=[1, 10000],  # set your own continous color scale
    # -------------------------------------------------------------------------------------------
    # text='convicts',                                      # values appear in figure as text labels
    # hover_name='under_trial',                             # values appear in bold in the hover tooltip
    # hover_data=['detenues'],                              # values appear as extra data in the hover tooltip
    # custom_data=['others']                                # invisible values that are extra data to be used in Dash callback or widgets

    # log_x=True,                                           # x-axis is Log-scaled
    # Log_y=True,                                           # y-axis is log-scaled
    # error_y="err_plus",                                   # y-axis error bars are symmetrical or for positive direction
)
barchart.show()
