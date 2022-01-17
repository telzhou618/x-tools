# x-tools

x-tools is a collection of tools developed in Python

Options:

```shell
-h, --help  Show this message and exit
```

Commands:

```shell
  file      File download
  password  Password generate
  request   Http request tools
```

## Example:

### Download file
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
  --help                    Show this message and exit.
```
```shell
> x-tools password -c 16 # generate password length is 16 chars
> EPMhqHb#*ZtM0dHI
```

###  Http request