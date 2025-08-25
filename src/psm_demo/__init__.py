from importlib.metadata import version as get_version


__version__ = get_version("psm-demo")


def main() -> None:
    print(f"Hello from psm-demo {__version__}")
