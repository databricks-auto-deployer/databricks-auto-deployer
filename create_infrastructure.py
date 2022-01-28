"""Create Databricks infrastructure"""

from pyaz import group
from pyaz import databricks


def create_infrastructure():
    """function to create infrastructure in Azure"""
    location = "eastus"
    resource_group = "dad-dev-rg"
    databricks_workspace = "daddev1workspace"

    group.create(location=location, name=resource_group)

    databricks.workspace.create(
        location=location, name=databricks_workspace, resource_group=resource_group, sku="trial"
    )

if __name__ == "__main__":
    create_infrastructure()
