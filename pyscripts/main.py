from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from flask import Flask, jsonify, request

app = Flask(__name__)

key_vault_name = "test-kv-pyscript"
key_vault_url = f"https://{key_vault_name}.vault.azure.net"
credential = DefaultAzureCredential()
client = SecretClient(vault_url=key_vault_url, credential=credential)

@app.route("/get-secret")
def get_secret():
    secret_name = request.args.get("name")
    try:
        secret = client.get_secret(secret_name)
        return jsonify({"secret": secret.value})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

from pyscript import Element
def print_hello(event):
    Element('output').write('Hello, World!')
