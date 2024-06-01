import subprocess
import os


class PowerShellManager:
    @property
    def is_installed(self) -> bool:
        try:
            subprocess.run(
                ["powershell", "-Command", "Write-Host 'Hello, World!'"],
                check=True,
                stdout=subprocess.DEVNULL,
            )
            return True
        except subprocess.CalledProcessError:
            return False

    @staticmethod
    def run_exe(exe_path: str) -> None:
        command = f"powershell Start-Process '{exe_path}'"

        if not os.path.exists(exe_path):
            print(f"Path {exe_path} does not exist.")
            return

        try:
            subprocess.run(command, check=True, shell=True)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while trying to start the program: {e}")

    @staticmethod
    def run_command(command: str) -> None:
        try:
            subprocess.run(["powershell", "-Command", command], check=True)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while trying to run the command: {e}")
