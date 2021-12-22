""" Running the Xetra ETL application"""

import logging
import logging.config

import yaml 

def main():
    """
    entry point to run the ETL job
    """

    # Parsing YAML file
    config_path = "C:/Users/rzelj/OneDrive/Desktop/ETL_pipelines_in_Python_Pandas/xetra_project/xetra_4321/configs/xetra_report_config.yml"
    config = yaml.safe_load(open(config_path))
    # configure logging
    log_config = config['logging']
    logging.config.dictConfig(log_config)
    logger = logging.getLogger(__name__)
    logger.info("This is test")

if __name__ == '__main__':
    main()