import dash
import dash_table
import pandas as pd

data = pd.read_csv('Electric_Vehicle_Population_Data.csv')

def table_make():
    make_count = data.Make.value_counts(dropna=False)
    return make_count


# app = dash.Dash(__name__)
#
# # Load some data
# df = pd.read_csv('my_data.csv')
#
# app.layout = dash_table.DataTable(
#     id='my-table',
#     columns=[{"name": i, "id": i} for i in df.columns],
#     data=df.to_dict('records')
# )
#
# if __name__ == '__main__':
#     app.run_server(debug=True)
