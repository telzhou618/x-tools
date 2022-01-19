from csv import reader
import json
import jsonlines

import click


@click.command()
@click.option("-csv-to-sql", "--csv-to-sql", help="Convert csv to sql")
@click.option("-csv-to-json", "--csv-to-json", help="Convert csv to json")
@click.option("-csv-to-jsonl", "--csv-to-jsonlines", help="Convert csv to jsonlines")
@click.option("-d", "--divide-limit", type=int, help="Limit number of batch sql generated")
@click.option("-o", "--out-file", help="Output to file")
def data(csv_to_sql, csv_to_json, csv_to_jsonlines, divide_limit, out_file):
    """Data convert  processor"""
    if csv_to_sql:
        m_csv_to_sql(csv_to_sql, divide_limit, out_file)
    if csv_to_json:
        m_csv_to_json(csv_to_json, out_file)
    if csv_to_jsonlines:
        m_csv_to_jsonlines(csv_to_jsonlines, out_file)


def m_csv_to_jsonlines(csv_file, out_file):
    """Convert  csv to jsonlines"""
    filename = csv_file.split("/")[-1].split('.')[0]
    if not out_file:
        out_file = filename + '.jsonl'
    lst = []
    with open(csv_file, 'r') as f:
        result = reader(f)
        header = next(result)  # column
        for d in result:
            new_d = []
            for x in d:
                if x.isdigit():
                    new_d.append(int(x))
                else:
                    new_d.append(x)
            dic = {}
            for i in range(len(header)):
                dic[header[i]] = new_d[i]
            lst.append(dic)
        with jsonlines.open(out_file, mode='w') as writer:
            writer.write_all(lst)


def m_csv_to_json(csv_file, out_file):
    """Convert  csv to json"""
    filename = csv_file.split("/")[-1].split('.')[0]
    if not out_file:
        out_file = filename + '.json'
    lst = []
    with open(csv_file, 'r') as f:
        result = reader(f)
        header = next(result)  # column
        for d in result:
            new_d = []
            for x in d:
                if x.isdigit():
                    new_d.append(int(x))
                else:
                    new_d.append(x)
            dic = {}
            for i in range(len(header)):
                dic[header[i]] = new_d[i]
            lst.append(dic)
        with open(out_file, 'w') as out:
            out.write(json.dumps(lst))


def m_csv_to_sql(csv_file, divide_limit, out_file):
    """Convert  csv to sql"""
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
            new_d = []
            for x in d:
                if x.isdigit():
                    new_d.append(x)
                else:
                    new_d.append(f"'{x}'")
            val = "(%s)" % (",".join(new_d))
            if not divide_limit:
                sql = insert_pre + val + ";"
                w.write(sql + "\n")
                pass
            else:
                # 每x条分隔
                limit = int(divide_limit)
                tmp_lst.append(val)
                if i > 0 and i % limit == 0:
                    batch_val = ','.join(tmp_lst)
                    sql = insert_pre + batch_val + ';'
                    w.write(sql + "\n")
                    tmp_lst.clear()
        else:
            batch_val = ','.join(tmp_lst)
            sql = insert_pre + batch_val + ';'
            w.write(sql + "\n")
            tmp_lst.clear()
    w.close()
    click.echo(out_file)
