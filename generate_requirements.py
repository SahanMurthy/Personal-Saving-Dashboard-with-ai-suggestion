import subprocess
import sys

def generate_requirements():
    try:
        # Run pip freeze command and capture the output
        result = subprocess.run([sys.executable, "-m", "pip", "freeze"], capture_output=True, text=True, check=True)
        
        # Write the output to requirements.txt
        with open("requirements.txt", "w") as f:
            f.write(result.stdout)
        
        print("requirements.txt file has been generated successfully.")
        print("Contents of requirements.txt:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while generating requirements.txt: {e}")
    except IOError as e:
        print(f"An error occurred while writing to requirements.txt: {e}")

generate_requirements()