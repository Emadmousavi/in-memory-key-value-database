# IN-MEMORY-KEY-VALUE-DATABASE


KEY-VALUE-DATABASE (KVDB) is a lightweight key-value store (think Redis, Couchbase on a much smaller scale) written in Python that leverages in-memory storage to minimize read/write times. KVDB also uses websocketing for client-server communication in order to minimize latency.

![KVDB Architecture](/assets/flow.png)

Full list of supported commands: [commands.md](/docs/commands.md)

## Setup

#### Cloning the repo

Make sure that you have the latest version of [Python](https://www.python.org/downloads/) installed on your machine. To download the source code, run:

```
git clone https://github.com/J-Obog/littlekv.git](https://github.com/Emadmousavi/in-memory-key-value-database.git
```

#### Virtualenv

first install virtual environment module:

```
pip install virtualenv
```

then create a virtual environment. in this case virtual environment name is 'venv'
```
python -m venv venv
```

The required packages are listed in the Pipfile. To install those dependencies, run:

```
pip install -r requirements.txt
```
## install kvdb module
after that enter the command below 
```
python setup.py install
```
## Running KVDB

#### Default configurations

The [KVDB.config](/KVDB.config) toml file holds informations regarding the project environment such the default host and port for the server to run on.
You can edit the content and provide your own custom default settings.

#### Running the server

To run the KVDB server with the default configurations, simply run:

```
KVDB-server
```

You can also pass in additional parameters through the command line:

```
usage: KVDB-server [-h HOST] [-p PORT] [-d KV_DIR] [-s KV_SRC] [-H]

KVDB Server

optional arguments:
  -h HOST, --host HOST  host server should run on
  -p PORT, --port PORT  port server should run on
  -d KV_DIR, --dir KV_DIR
                        directory of target kv file
  -s KV_SRC, --src KV_SRC
                        name of target kv file
  -H, --help            show this help message and exit
```

Example usage:

```
$ KVDB-server
Server listening @ 127.0.0.1 on port 9876
```

#### Running the CLI

LittleKV comes equipped with a command line interface that you can use to run commands.
To run the KVDB CLI with the default configurrations, simply run:

```
KVDB-cli
```

You can also pass in additional parameters through the command line:

```
usage: KVDB-cli [-h HOST] [-p PORT] [-H] command [command ...]

KVDB CLI

positional arguments:
  command               KVDB commands

optional arguments:
  -h HOST, --host HOST  host client should connect to
  -p PORT, --port PORT  port client should connect to
  -H, --help            show this help message and exit
```

Example usage:

```
$ KVDB-cli
# ping
ping
> PONG 

$ KVDB-cli
# set key value
set test foo
> OK
$ KVDB-cli
# get key
get test
> foo
$ KVDB-cli
# list
list
> ['default', 'other_db']

```
