import subprocess

def run_powershell_in_directory(powershell_path, commands, working_directory):
    try:
        # Join the commands with semicolons
        command_string = ";".join(commands)

        # Execute the PowerShell commands with the specified working directory
        result = subprocess.run(
            [powershell_path, "-Command", command_string],
            capture_output=True,
            text=True,
            shell=True,
            cwd=working_directory
        )

        # Output the result
        print("Output:")
        print(result.stdout)

        print("Errors:")
        print(result.stderr)

    except Exception as e:
        print(f"An error occurred: {e}")

# Path to a specific PowerShell executable (correct path)
powershell_path = r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"

# Example PowerShell commands
powershell_commands = [
    r'YOUR COMMANDS HERE,
    r'YOUR COMMANDS HERE'
]

# Working directory (set to the root of a folder on drive C)
working_directory = r"ADDRESS"

# Run the commands
run_powershell_in_directory(powershell_path, powershell_commands, working_directory)
