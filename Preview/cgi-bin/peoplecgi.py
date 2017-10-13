#!/usr/bin/python
import cgi, shelve, sys, os, html
shelve_name = 'tmp/class-shelve'

field_names = ('name', 'age', 'job', 'pay')

form = cgi.FieldStorage()
print('Content-Type: text/html')
sys.path.insert(0, os.getcwd())

reply_html = """
<html>
<title>People Input Form</title>
<body>
<form method=POST action="peoplecgi.py">
    <table>
    <tr><th>key<td><input type=text name=key value="%(key)s">
    $ROWS$
    </table>
    <p>
    <input type=submit value="Fetch",  name=action>
    <input type=submit value="Update", name=action>
</form>
</body></html>
"""

row_html = '<tr><th>%s<td><input type=text name=%s value="%%(%s)s">\n'
rows_html = ''
for field_name in field_names:
    rows_html += (row_html % ((field_name,) * 3))
reply_html = reply_html.replace('$ROWS$', rows_html)


def htmlize(dict):
    new = dict.copy()
    for field in field_names:
        value = new[field]
        new[field] = html.escape(repr(value))
    return new


def fetch_record(db, form):
    try:
        key = form['key'].value
        record = db[key]
        fields = record.__dict__
        fields['key'] = key
    except:
        fields = dict.fromkeys(field_names, '?')
        fields['key'] = "Missing or invalid key!"
    return fields


def update_record(db, form):
    if 'key' not in form:
        fields = dict.fromkeys(field_names, '?')
        fields['key'] = 'Missing key input!'
    else:
        key = form['key'].value
        if key in db:
            record = db[key]                       # update existing record
        else:
            from Preview.person import Person              # make/store new one for key
            record = Person(name='?', age='?')     # eval: strings must be quoted
        for field in field_names:
            setattr(record, field, eval(form[field].value))
        db[key] = record
        fields = record.__dict__
        fields['key'] = key
    return fields


db = shelve.open(shelve_name)
action = form['action'].value if 'action' in form else None
if action == 'Fetch':
    fields = fetch_record(db, form)
elif action == 'Update':
    fields = update_record(db, form)
else:
    fields = dict.fromkeys(field_names, '?')        # bad submit button value
    fields['key'] = 'Missing or invalid action!'
db.close()
print(reply_html % htmlize(fields))                 # fill reply from dict
