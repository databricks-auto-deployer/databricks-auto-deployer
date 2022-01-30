"""Create Databricks infrastructure"""

from pyaz import group
from pyaz import databricks


def create_infrastructure():
    """function to create infrastructure in Azure"""
    location = "eastus"
    resource_group = "dad-dev-rg"
    managed_resource_group = resource_group + "-databricks"
    databricks_workspace = "daddev1workspace"

    group.create(location=location, name=resource_group)

    # test that group is created
    assert group.exists(name=resource_group), "resource group not created"

    databricks.workspace.create(
        location=location, 
        name=databricks_workspace, 
        resource_group=resource_group, sku="trial",
        managed_resource_group=managed_resource_group,
    )

    # test that the databricks workspace was created
    result = databricks.workspace.show(name=databricks_workspace, resource_group=resource_group)
    assert result['name'] == databricks_workspace, 'Databricks workspace not created'

if __name__ == "__main__":
    create_infrastructure()
