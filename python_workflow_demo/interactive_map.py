# %% Code test

from pathlib import Path

import geopandas as gpd
import hhnk_research_tools as hrt

from python_workflow_demo.project import Project


def make_interactive_map(gdf: gpd.GeoDataFrame, output_path: Path):
    """
    Maak een HTML met een folium map en een shapebestand.

    Parameters
    ----------
    gdf : gpd.GeoDataFrame
        gdf met shapes om op kaart te tekenen
    output_path : Path
        output html bestand
    """
    datacolumn = "bouwjaar"
    colormap_name = "viridis"
    colormap_steps = None

    title = "Interactive map test"
    legend_label = "Testlabels"
    tooltip_columns = ["gid", "bouwjaar"]
    tooltip_aliases = ["gid", "bouwjaar"]
    quantiles = [0, 0.1, 0.5, 0.8, 1]

    # quantiles = np.arange(0, 1.1, 0.1)

    v = hrt.create_interactive_map(
        gdf=gdf,
        datacolumn=datacolumn,
        output_path=output_path,
        title=title,
        legend_label=legend_label,
        tooltip_columns=tooltip_columns,
        tooltip_aliases=tooltip_aliases,
        colormap_name=colormap_name,
        colormap_steps=colormap_steps,
        quantiles=quantiles,
    )


# %%
if __name__ == "__main__":
    p = Project(r"D:\github\wvangerwen\demo_data")
    gdf = p.input.panden.load()
    output_path = p.output.interactive_map.path
    make_interactive_map(gdf, output_path)

    # Open in browser
    import webbrowser

    webbrowser.open(output_path)
