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

Run database migrations.

```shell
# TODO: make sure this is correct
flask db init
flask db upgrade
```

Start the application.

```shell
python run.py
```