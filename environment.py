import os
import yaml


from helpers.constants import FOLDER_ALLURE_REPORT

environment = yaml.safe_load(open(f"{os.getcwd()[0:64]}/behave.yml"))
config_capabilities = yaml.safe_load(open(f"{os.getcwd()}/service/capabilities.yml"))

def before_all(context):
    if not context.config.log_capture:
        logging.basicConfig(level=logging.DEBUG)
    try:
        os.system(f"rm {FOLDER_ALLURE_REPORT}/*.*")
    except:
        pass    

def after_scenario(context, scenario):
    pass

def before_scenario(context, scenario):
    if "skip" in scenario.tags:
        scenario.skip("@skip")