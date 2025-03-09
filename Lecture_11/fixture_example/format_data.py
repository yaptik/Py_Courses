def format_data_for_display(people: list[dict]):
    res_list = []
    for di in people:
        res_str = di.get('given_name') + ' '
        res_str += di.get('family_name')
        res_str += ': ' + di.get('title')
        res_list.append(res_str)
    return res_list


def format_data_for_excel(people: list[dict]):
    res_str = 'given,family,title\n'
    for di in people:
        res_str += di.get('given_name') + ','
        res_str += di.get('family_name') + ','
        res_str += di.get('title') + '\n'
    return res_str
