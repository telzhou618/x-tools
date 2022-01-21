from csv import reader
import json
import jsonlines
import pandas as pd
import os

import click


@click.command()
@click.option("-csv-to-sql", "--csv-to-sql", help="Convert csv to sql")
@click.option("-csv-to-json", "--csv-to-json", help="Convert csv to json")
@click.option("-csv-to-jsonl", "--csv-to-jsonlines", help="Convert csv to jsonlines")
@click.option("-csv-to-xls", "--csv-to-xls", help="Convert csv to xls")
@click.option("-csv-to-xlsx", "--csv-to-xlsx", help="Convert csv to xlsx")
@click.option("-d", "--divide-limit", type=int, help="Limit number of batch sql generated")
@click.option("-o", "--out-file", help="Output to file")
def data(csv_to_sql, csv_to_json, csv_to_jsonlines, csv_to_xls, csv_to_xlsx, divide_limit, out_file):
    """Data processor"""
    if csv_to_sql:
        m_csv_to_sql(csv_to_sql, divide_limit, out_file)
    elif csv_to_json:
        m_csv_to_json(csv_to_json, out_file)
    elif csv_to_jsonlines:
        m_csv_to_jsonlines(csv_to_jsonlines, out_file)
    elif csv_to_xls:
        m_csv_to_xls(csv_to_xls, out_file)
    elif csv_to_xlsx:
        m_csv_to_xlsx(csv_to_xlsx, out_file)
    else:
        os.system('x-tools data --help')


def m_csv_to_xls(csv_file, out_file):
    """Convert csv to xl"""
    filename = csv_file.split("/")[-1].split('.')[0]
    if not out_file:
        out_file = filename + '.xls'
    csv = pd.read_csv(csv_file, encoding='utf-8')
    csv.to_excel(out_file)
    click.echo(out_file)


def m_csv_to_xlsx(csv_file, out_file):
    """Convert csv to xlsx"""
    filename = csv_file.split("/")[-1].split('.')[0]
    if not out_file:
        out_file = filename + '.xlsx'
    csv = pd.read_csv(csv_file, encoding='utf-8')
    csv.to_excel(out_file)
    click.echo(out_file)


def m_csv_to_jsonlines(csv_file, out_file=None):
    """Convert csv to jsonlines"""
    filename = csv_file.split("/")[-1].split('.')[0]
    if not out_file:
        out_file = filename + '.jsonl'
    lst = []
    with open(csv_file, 'r') as f:
        result = reader(f)
        header = next(result)  # column
        for d in result:
            new_d = [int(x) if x.isdigit() else x for x in d]
            dic = {}
            for i in range(len(header)):
                dic[header[i]] = new_d[i]
            lst.append(dic)
        with jsonlines.open(out_file, mode='w') as writer:
            writer.write_all(lst)
    click.echo(out_file)


def m_csv_to_json(csv_file, out_file=None):
    """Convert csv to json"""
    filename = csv_file.split("/")[-1].split('.')[0]
    if not out_file:
        out_file = filename + '.json'
    lst = []
    with open(csv_file, 'r') as f:
        result = reader(f)
        header = next(result)  # column
        for d in result:
            new_d = [int(x) if x.isdigit() else x for x in d]
            dic = {}
            for i in range(len(header)):
                dic[header[i]] = new_d[i]
            lst.append(dic)
        with open(out_file, 'w') as out:
            out.write(json.dumps(lst))
    click.echo(out_file)


def m_csv_to_sql(csv_file, divide_limit=1, out_file=None):
    """Convert csv to sql"""
    filename = csv_file.split("/")[-1].split('.')[0]
    if not out_file:
        out_file = filename + '.sql'
    w = open(out_file, 'w')
    with open(csv_file, 'r') as f:
        result = reader(f)
        header = next(result)  # column
        # 根据表头生成 INSERT 语句
        column = ",".join(header)
        insert_pre = "INSERT INTO %s (%s) VALUES " % (filename, column)
        tmp_lst = []
        for i, d in enumerate(result):
            new_d = [x if x.isdigit() else f"'{x}'" for x in d]
            val = "(%s)" % (",".join(new_d))
            # 默认生成单条SQL语句
            if not divide_limit:
                sql = insert_pre + val + ";"
                w.write(sql + "\n")
            else:
                limit = int(divide_limit)
                tmp_lst.append(val)
                # 每limit条分隔
                if (i + 1) % limit == 0:
                    sql = insert_pre + ','.join(tmp_lst) + ';'
                    w.write(sql + "\n")
                    tmp_lst.clear()
        else:
            if tmp_lst:
                sql = insert_pre + ','.join(tmp_lst) + ';'
                w.write(sql + "\n")
                tmp_lst.clear()
    w.close()
    click.echo(out_file)
