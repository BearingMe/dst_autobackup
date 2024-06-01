from utils import on_app_bootstrap

# get instances of powershell and config
powershell, config = on_app_bootstrap()

# run powershell commands
powershell.run_exe(config.get("exe_absolute_path"))
powershell.run_command(config.get("ps_command"))
