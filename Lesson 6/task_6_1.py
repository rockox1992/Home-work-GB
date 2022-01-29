def parsing_no(logs='task_6_1.txt'):
    with open(logs, 'r', encoding='utf-8') as f:
        for line in f:
            remote_addr = line.split(' ')[0]
            request_type = line.split(' ')[5][1:4]
            requested_resource = line.split(' ')[6]
            yield f"({remote_addr}, {request_type}, {requested_resource}), \n"


print(*parsing_no())
