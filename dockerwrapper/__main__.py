from pyconfigmanager import get_config, logging_config, helper as config_helper
import docker
import os
import argparse
import logging


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="docker wrapper")
    schemafile = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "config", "schema.yaml")
    config = get_config(schema=[{
        key: value
        for key, value in config_helper.get_helpers().items()
        if key in ("config", "logging")
    }, schemafile])
    config.update_values_by_argument_parser(parser=parser)
    if config.config.dump:
        config.dump_config(config_name="config.dump", exit=True)
    logging_config.logger_config(
        name="dockerwrapper", level=config.logging.verbosity, propagate=False)
    logging.info([key for key in config])
    logging.info(config.build.values())
    client = docker.from_env()
    return
    image, logs = client.images.build(**config.build.values())
    for line in logs:
        print(line)


if __name__ == "__main__":
    main()
