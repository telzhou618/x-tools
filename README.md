# x-tools

X-tools is a collection of tools developed in Python

Commands:

```shell
  file      File download
  password  Password generate
  request   Http request tools
  data      Data processor
```
## Requirements
Python 3.9+

## Install

```shell
curl -fsSL https://raw.githubusercontent.com/telzhou618/x-tools/main/install.sh | bash
```

## Example:

### Data convert  processor

Usage: x-tools data [OPTIONS]

Options:

```shell
  -csv-to-sql,    --csv-to-sql TEXT         Convert csv to sql
  -csv-to-json,   --csv-to-json TEXT        Convert csv to json                           
  -csv-to-jsonl,  --csv-to-jsonlines TEXT   Convert csv to jsonlines    
  -csv-to-xls,    --csv-to-xls TEXT         Convert csv to xls,Deprecated
  -csv-to-xlsx,   --csv-to-xlsx TEXT        Convert csv to xlsx
  -d,             --divide-limit INTEGER    Limit number of batch sql generated
  -o,             --out-file TEXT           Output to file
  --help                                    Show this message and exit.
```

Example:

```shell
 # Convert CSV data into SQL statements, and separate every 1000 into batch statements
 x-tools data -csv-to-sql /home/user.csv -d 1000 -o ./tb_user.sql
```

### Download file

Usage: x-tools file [OPTIONS]
Options:

```shell
  -url, --url TEXT    file url  [required]
  -name, --name TEXT  Picture rename
  --help              Show this message and exit.
```

Example:

```shell
x-tools file -url https://vscode.cdn.azure.cn/stable/e5a624b788d92b8d34d1392e4c4d9789406efe8f/VSCodeUserSetup-x64-1.51.1.exe
```

### Password generate

Usage: x-tools password [OPTIONS]

```shell
Options:
  -c, --count INTEGER       Length of password, default is 16 chars
  -A, --upper-az BOOLEAN    Contain characters[A~Z]
  -a, --letter-az BOOLEAN   Contain characters[a~z]
  -n, --number BOOLEAN      Contain characters[0~9]
  -s, --special BOOLEAN     Contain characters[!@#$%^&*]
  -all, --all-char BOOLEAN  Contain all characters
  -o, --out-file TEXT       Output to file
  -his, --history BOOLEAN   History generated password
  --help                    Show this message and exit.
```

Example:

```shell
# generate password length is 16 chars and out to file
x-tools password -c 16 -o ./pw.txt 
> EPMhqHb#*ZtM0dHI

# view history
x-tools password -his

```

### Http request

Usage: x-tools request [OPTIONS] URL

Options:

```shell
  -m, --method [get|post]         Request method
  -h, --headers TEXT              Headers dict
  -p, --params TEXT               Params dict
  -j, --json-params TEXT          Json data dict
  -f, --files TEXT                Upload files
  -fr, --format-result [text|json] Format return data
  --help                          Show this message and exit.
```

Example:

```shell
# get
x-tools request https://www.httpbin.org/get
# post
x-tools request https://www.httpbin.org/post -m post -j {\"p1\":\"v1\"}
```
