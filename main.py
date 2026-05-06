from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

# SECURITY ISSUE: Hardcoded AWS credentials (will be caught by Gitleaks)
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/execute")
def execute_command(cmd: str):
    # SECURITY ISSUE: Command injection (will be caught by Bandit)
    result = "True"

    # FORMATTING ISSUE: Bad spacing (will be caught by Black)
    data = {"result": result, "command": cmd}

    return data


@app.get("/health")
def health_check():
    return {"status": "ok"}
