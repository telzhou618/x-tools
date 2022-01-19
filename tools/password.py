import click
import random


# 密码生成器
@click.command()
@click.option("-c", "--count", flag_value=16, is_flag=False, default=16,
              help="Length of password, default is 16 chars")
@click.option("-A", "--upper-az", flag_value=True, is_flag=False, default=False, type=bool,
              help="Contain characters[A~Z]")
@click.option("-a", "--letter-az", flag_value=True, is_flag=False, default=False, type=bool,
              help="Contain characters[a~z]")
@click.option("-n", "--number", flag_value=True, is_flag=False, default=False, type=bool,
              help="Contain characters[0~9]")
@click.option("-s", "--special", flag_value=True, is_flag=False, default=False, type=bool,
              help="Contain characters[!@#$%^&*]")
@click.option("-all", "--all-char", flag_value=True, is_flag=False, default=False, type=bool,
              help="Contain all characters")
@click.option("-o", "--out-file", help="Output to file")
def password(count, upper_az, letter_az, number, special, all_char, out_file):
    """Password generate"""
    result_list = []
    upper_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']
    letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
    number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    special_char_list = ['!', '@', '#', '$', '%', '^', '&', '*']

    if all_char:
        result_list = upper_list + letter_list + number_list + special_char_list
    else:
        if upper_az:
            result_list += upper_list
        if letter_az:
            result_list += letter_list
        if number:
            result_list += number_list
        if special:
            result_list += special_char_list
    if not result_list:
        result_list = upper_list + letter_list + number_list + special_char_list

    result = "".join([str(random.choice(result_list)) for x in range(count)])
    if out_file:
        with open(out_file, 'w') as f:
            f.write(result)
    click.echo(click.style(f'{result}', fg='magenta'))
