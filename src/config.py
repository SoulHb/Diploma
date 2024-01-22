import yaml
import sys
sys.path.append('src')
with open('./config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)
GPT_MATH_SOLVE = config["gpt_math_solve"]
GPT_CLASSIFICATION = config["gpt_classification"]
CLASSIFIER_GPT_MODEL = config["classifier_gpt_model"]
SOLVER_GPT_MODEL = config["solver_gpt_model"]
DATA_PATH = config["data_path"]
MAX_TOKEN_LIMIT = config["max_token_limit"]
CLASSIFIER_TEMPERATURE = config["classifier_temperature"]
SOLVER_TEMPERATURE = config["solver_temperature"]
