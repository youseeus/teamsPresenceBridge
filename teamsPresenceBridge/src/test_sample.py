from util import loadConfFromVar
import os


def test_answer():
  os.environ["azureApplicationId"] = "azureApplicationId1"
  os.environ["azureClientKey"] = "azureClientKey1"
  os.environ["azureTenantId"] = "azureTenantId1"
  res= loadConfFromVar()
  assert res["azureApplicationId"] == "azureApplicationId1"
  assert res["azureClientKey"] == "azureClientKey1"
  assert res["azureTenantId"] == "azureTenantId1"
