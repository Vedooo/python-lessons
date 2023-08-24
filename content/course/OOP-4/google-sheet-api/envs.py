import os
import pprint


os.environ["NUTRITIONIX_APP_ID"] = 'xxxx'
os.environ["NUTRITIONIX_API_KEY"] = 'xxxx'
os.environ["SHEET_ENDPOINT"] = 'xxxx'
os.environ["BEARER"] = 'xxxx'


env_vars = os.environ
envs = pprint.pprint(dict(env_vars, width=1))
