# %%
import pytest

from python_workflow_demo.interactive_map import make_interactive_map
from python_workflow_demo.project import Project

# def test_interactive_map():
#     p = Project(r"D:\github\wvangerwen\demo_data")
#     gdf = p.input.panden.load().head()
#     output_path = p.output.interactive_map.path
#     make_interactive_map(gdf, output_path)

#     assert output_path.exists()


def test_true():
    assert True


def test_hrt():
    import hhnk_research_tools


def test_htt():
    """This should fail as htt is not on the test env."""
    with pytest.raises(Exception):
        import hhnk_threedi_tools
