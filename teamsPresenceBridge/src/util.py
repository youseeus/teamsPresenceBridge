import os, yaml, json

def loadConfFromYaml (fileName):
    with open(fileName, "r") as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
    return cfg
def loadConfFromJson (fileName):
    with open(fileName, "r") as jsonFile:
        cfg = json.load(jsonFile)
    return cfg

def loadConfFromVar():
    applicationId = os.environ.get('azureApplicationId')
    clientKey = os.environ.get('azureClientKey')
    tenantId = os.environ.get('azureTenantId')

    if (not applicationId or not clientKey or not tenantId):
        print("Missing some settings. Please set the following envs: azureApplicationId, azureClientKey, azureTenantId")
        exit()

    tmpCfg = {'azureApplicationId': applicationId, 'azureClientKey': clientKey, 'azureTenantId': tenantId}

    jsonStr = json.dumps(tmpCfg)
    jsonCfg = json.loads(jsonStr)

    return jsonCfg