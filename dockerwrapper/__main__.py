from pyconfigmanager import get_config
import docker
import os


def main():
    schemafile = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "config", "schema.yaml")
    config = get_config(schema=schemafile)
    print(config)
    client = docker.from_env()
    print(client.containers.list(all=True))


if __name__ == "__main__":
    main()
