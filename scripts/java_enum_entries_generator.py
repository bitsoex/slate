""" JAVA enum generator

This script prints in the console entries for the WebAPIErrorCodes enum.
"""
import re
# In case of the reason begins with a digit (The Jave enums can't begins with digits)
DIGITS_MAP = {
    '2': 'TWO'
}
with open('./source/index.html.md') as f:
    content = f.read()

errors_initial_position = content.find('## Error Codes')
errors_finish_position = content.find('## Client Libraries')
content = content[errors_initial_position:errors_finish_position].split('\n')
http_code = 500
categody = ''
error_list = []
for line in content:
    code = ''
    reason = ''
    name = ''
    if line[:3] == '###': # Get category and http_code from H3 texts
        header = line.split(':')
        category = header[0].split('###')[1].strip()
        http_code = header[1].split('(')[1]
        http_code = re.findall(r'[\d.]+', http_code)[0]
        print("")
        print("// {}".format(line[4:]))
        continue
    if line and line[0] == '*':
        splited_line = line.split(':')
        code = splited_line[0][2:]
        reason = splited_line[1].strip()
        reason = reason.replace("\"", "")
        name  = reason.replace(' ', '_')
        name = re.sub(r'\W+', '', name)
        name = DIGITS_MAP[name[0]] + name[1:] if name[0] in DIGITS_MAP else name
        error_list.append((code, name.upper()))
        print("{}(\"{}\", \"{}\", {}),".format(name.upper(), code, reason, http_code))
