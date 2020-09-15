"""
File: fossil_fuel.py
--------------------
This program uses data downloaded from the EPA's Greenhouse Gas Inventory Data Explorer
(link: https://cfpub.epa.gov/ghgdata/inventoryexplorer/#electricitygeneration/allgas/source/all)
and creates an interactive graph using pandas and plotly.express. The graph displays each
emissions source as a line and shows the amount of emissions per year from 1990-2018.
When you hover over each line it will show you the year and amount of emissions for that data
point.
"""
import pandas as pd
import plotly.express as px


def main():
    ff = pd.read_csv('data.csv')
    ff_long = pd.melt(ff, id_vars=['Year'], value_vars=['Fossil fuel combustion: carbon dioxide',
                                                        'Fossil fuel combustion: other greenhouse gases',
                                                        'Incineration of waste',
                                                        'Other electricity generation categories',
                                                        'Total'])
    fig = px.line(ff_long, x='Year', y='value', color='variable',
                  title='US Greenhouse Gas Emissions from Electricity Generation')
    fig.update_layout(yaxis_title="Emissions (million metric tons)", legend_title="Emission source")
    fig.show()


if __name__ == '__main__':
    main()
