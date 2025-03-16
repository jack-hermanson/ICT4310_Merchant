# ICT4310_Merchant

ICT 4310 project

## Setup

All commands assume a Unix-like operating system, but there are equivalents on Windows.

Clone the repository to a fresh directory and `cd` into it.

Create a virtual environment.

```sh
python3 -m venv venv  
```

Activate the virtual environment.

```shell
source venv/bin/activate  
```

Install the requirements.

```shell
pip install -r requirements.txt
```

Create your local `.env` file.

```shell
cp .env.template.txt .env
```

Generate a random hexadecimal number to use as a secret key.
This is one way to do it, but if you google "generate secret key"
online, there are other options.

```shell
node -e "console.log(require('crypto').randomBytes(48).toString('hex'))"
```

Copy the output and paste it into the `SECRET_KEY` value.

Fill in the rest of the `.env` file with valid environment variables.

```dotenv
FLASK_APP=application
ENVIRONMENT=dev
FLASK_ENV=development
SECRET_KEY=c1d137879ac5ba035d1495e85da0c914fe709868a94cb5aa2e657566acea08516c4667591f56deeacb534e7a24aaad3d
PORT=5035
```

Run database initialization and migrations.
```shell
python -m flask --app application db upgrade  
```

In the comments next to each command, I have a version 
that explicitly specifies the Flask app; you shouldn't 
need this if you properly activated the virtual environment
and set up your `.env` correctly.

Start the application.

```shell
python run.py
```