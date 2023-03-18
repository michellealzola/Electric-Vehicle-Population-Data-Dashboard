import pandas as pd
import plotly.express as px

data = pd.read_csv('Electric_Vehicle_Population_Data.csv')

def pop_ev_make():
    make_count = data.Make.value_counts(dropna=False)
    fig = px.scatter(make_count,
                     x='Make',
                     y=make_count.index,
                     color_discrete_sequence=px.colors.qualitative.Pastel1,
                     title='EV Population per Make',
                     hover_name='Make')
    return fig

def pop_per_state():
    make_evtype_pivot = data.pivot_table(values=['Make'], columns='State', aggfunc='count')
    make_evtype_pivot_T = make_evtype_pivot.T
    make_evtype_pivot_T.rename(columns={'Make': 'EV Population'}, inplace=True)
    fig = px.bar(make_evtype_pivot_T,
                 color_discrete_sequence=px.colors.qualitative.Pastel1,
                 title='EV Population per State',
                 hover_name=make_evtype_pivot_T.index)
    return fig

def pop_per_type():
    evtype_count = data['Electric Vehicle Type'].value_counts(dropna=False)
    fig = px.pie(evtype_count,
                 values='Electric Vehicle Type',
                 names=evtype_count.index,
                 color_discrete_sequence=px.colors.qualitative.Pastel1,
                 title='Population per EV Type',
                 hover_name='Electric Vehicle Type')
    return fig

def pop_per_e_utility():
    e_utility_count = data['Electric Utility'].value_counts(dropna=False)
    fig = px.scatter(e_utility_count,
                     x='Electric Utility',
                     y=e_utility_count.index,
                     color_discrete_sequence=px.colors.qualitative.Pastel1,
                     title='Electric Utility Count',
                     hover_name=e_utility_count.index)
    return fig

def pop_per_location():
    location = list(data['Vehicle Location'].dropna())
    location_list = []
    for item in location:
        v = str(item)
        location_list.append(v.replace('POINT (', '').replace(')', '').split(' '))
    location_point_x = []
    location_point_y = []
    for i in range(len(location_list)):
        location_point_x.append(location_list[i][0])
        location_point_y.append(location_list[i][1])
    fig = px.scatter(x=location_point_x, y=location_point_y, opacity=0.5, color_discrete_sequence=['red'])
    fig.add_densitymapbox(lat=location_point_y, lon=location_point_x, radius=5, zmax=8, colorscale='Greens')
    fig.update_layout(mapbox_style="carto-positron", mapbox_zoom=1.5,
                      mapbox_center={"lat": 47.10349, "lon": -119.01561})
    return fig
