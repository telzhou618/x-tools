import requests
import click
import json

from fake_useragent import UserAgent

ua = UserAgent()


@click.command()
@click.option("-m", "--method", type=click.Choice(['get', 'post']), default='get', help="Request method")
@click.option("-h", "--headers", help="Headers dict")
@click.option("-p", "--params", help="Params dict")
@click.option("-j", "--json-params", help="Json data dict")
@click.option("-f", "--files", help="Upload files")
@click.option("-fr", "--format-result", type=click.Choice(['text', 'json']), help="Format return data")
@click.argument('url')
def request(url, headers, params, json_params, method, files, format_result):
    """
Http request tools

Example:

    x-tools request https://www.httpbin.org/get

    x-tools request https://www.httpbin.org/post -m post -j {\\"p1\\":\\"v1\\"}

    """
    data = {}
    method = str(method).upper()
    _headers = {'User-Agent': ua.random}
    if headers:
        for k, v in json.loads(headers).items():
            _headers[k] = v
    data['headers'] = _headers
    if params:
        data['params'] = json.loads(params)
    if json_params:
        data['json'] = json.loads(json_params)
    if files:
        data['files'] = json.loads(files)

    re = requests.request(method, url, **data)
    re.encoding = 'utf-8'
    if format_result == 'json':
        ret_str = re.json()
    else:
        ret_str = re.text
    click.echo(ret_str)
