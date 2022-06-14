## LittleKV Commands

These are the following commands that are currently supported:
notice: before any command you should enter the corresponding template and after that enter the command

### GET - `get <key>`

**Template:** "# get key"

**Params:** key = Key to be retrieved

**Returns:** Value of key if it exists, otherwise "\<None>\"

### SET - `set <key> <value>`

**Template:** "# set key value"

**Params:** key = Key to be set (or updated if exists) | value = Value of key

**Returns:** "OK" if key was successfully set

### DEL - `del <key>`

**Template:** "# del key"

**Params:** key = Key to be deleted (if exists)

**Returns:** "OK" if key was successfully deleted

### KEYS - `keys <pattern>`

**Template:** "# keys regex"

**Params:** pattern = Regex pattern used to match keys

**Returns:** List of keys that fit criteria

### USE - `use <db_name>`

**Template:** "# use db_name"

**Params:** db_name = name of db to switch (if db does not exist it will be created automatically)

**Returns:** List of keys that fit criteria

### LOAD - `load <path> <db_name>`

**Template:** "# load path db_name"

**Params:** path = path of file which its data must be transefered to db | db_name = name of db

**Returns:** "OK" if key was successfully set

### DUMP - `dump <db_name> <path>`

**Template:** "# dump db_name path"

**Params:** path = path of file which db's data must be transefered to it | db_name = name of db

**Returns:** "OK" if key was successfully set

### LIST - `list`

**Template:** "# list"

**Params:** None

**Returns:** list of available dbs

### EXIT - `exit`

**Template:** "# exit"

**Params:** None

**Returns:** exit from cli 

### COUNT - `count`

**Template:** "# count"

**Params:** None

**Returns:** Number of key-value pair in db

### CLEAR - `clear`

**Template:** "# clear"

**Params:** None

**Returns:** "OK" if all keys were removed successfully

### PING - `ping`

**Template:** "# ping"

**Params:** None

**Returns:** "PONG" if client was able to connect to server
