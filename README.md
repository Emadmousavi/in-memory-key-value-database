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

activate venv in windows
```
.\venv\Scripts\activate
```

activate venv in linux
```
source ./venv/bin/activate
```

The required packages are listed in the requirements.txt To install those dependencies, run:

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
kvdb-server
```

You can also pass in additional parameters through the command line:

```
usage: lkv-server [-h HOST] [-p PORT] [-d KV_DIR] [-s KV_SRC] [-H]

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
$ kvdb-server
Server listening @ 127.0.0.1 on port 9876
```

#### Running the CLI

LittleKV comes equipped with a command line interface that you can use to run commands.
To run the KVDB CLI with the default configurrations, simply run:

```
kvdb-cli
```

You can also pass in additional parameters through the command line:

```
usage: lkv-cli [-h HOST] [-p PORT] [-H] 

KVDB CLI

optional arguments:
  -h HOST, --host HOST  host client should connect to
  -p PORT, --port PORT  port client should connect to
  -H, --help            show this help message and exit
```
Example usage:

```
$ kvdb-cli
# ping
ping
> PONG 

$ kvdb-cli
# set key value
set test foo
> OK

$ kvdb-cli
# get key
get test
> foo

$ kvdb-cli
# list
list
> ['default', 'other_db']
```
#### dump / load command
for "dump" and "load" commands you can use absolute and relative path for filenames

for example relative path of new_data.txt which exist in this repo is ./new_data.txt

you can use .txt or .json files as you wish

```
# dump db_name path
dump default ./default.json
> OK
```

```
# load path db_name
load ./default.json default
> OK
```
