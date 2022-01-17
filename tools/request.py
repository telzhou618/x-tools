import requests
import click

from fake_useragent import UserAgent

ua = UserAgent()


@click.command()
@click.option("-h", "--headers", help="设置请求头参数,多个\";\"分隔")
@click.option("-p", "--params", help="请求参数,如:a=b&c=d")
@click.option("-d", "--json", help="json格式的参数")
@click.option("-m", "--method", type=click.Choice(['get', 'post']), default='get', help="提交方式如:get,post等")
@click.option("-f", "--format", type=click.Choice(['text', 'json']), help="数据返回格式,如:text,json")
@click.help_option("-help", "--help", help="获得帮助文档")
@click.argument('url')
def request(url, headers, params, json, method, format):
    """
Http request tools

Example:

    x-tools request https://www.httpbin.org/get

    x-tools request https://www.httpbin.org/post -m post

    """
    _headers = {
        'User-Agent': ua.random
    }
    re = requests.request(str(method).upper(), url, headers=_headers)
    re.encoding = 'utf-8'
    if format == 'json':
        ret_str = re.json()
    else:
        ret_str = re.text
    click.echo(ret_str)


def main():
    x_request()


if __name__ == '__main__':
    main()
