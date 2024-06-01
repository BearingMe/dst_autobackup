from libs.PowerShellManager import PowerShellManager
from libs.JsonFileManager import JsonFileManager


def on_app_bootstrap():
    print("Bootstrapping...")

    ps = bootstrap_power_shell()
    config = bootstrap_json_config()

    return [ps, config]


def bootstrap_power_shell():
    ps = PowerShellManager()
    print("Loading PowerShellManager...")

    if not ps.is_installed:
        print("PowerShell is not installed. Exiting...")
        exit(1)

    return ps


def bootstrap_json_config():
    config = JsonFileManager(r"./config.json")
    print("Loading JsonFileManager...")

    if not config.exists:
        print("config.json not found. Exiting...")
        exit(1)

    return config
