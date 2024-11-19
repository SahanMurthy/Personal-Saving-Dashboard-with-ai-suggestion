import yaml
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Define your users and their credentials
credentials = {
    "usernames": {
        "sahan": {
            "email": "sahan@example.com",
            "name": "Sahan N Murthy",
            "password": hash_password("sahan123")
        }
    }
}

# Create the config dictionary
config = {
    "credentials": credentials,
    "cookie": {
        "expiry_days": 30,
        "key": "some_signature_key",  # Replace with a secure key for production
        "name": "personal_savings_dashboard_cookie"
    }
}

# Write the config to a YAML file
with open('config.yaml', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)

print("Configuration file created successfully.")