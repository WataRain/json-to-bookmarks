import json

with open(r"data.json") as json_file:
    data = json.loads(json_file.read())

output = """<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Start</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <div>
            <h1>Hello!</h1>
            <nav>"""

for category, link_data in data.items():
    output += "\n\t\t\t\t<ul>"+category
    for display_name, link_url in link_data.items():
        output += f"\n\t\t\t\t\t<li><a href={link_url}>{display_name}</a></li>"
    output += "\n\t\t\t\t</ul>"

output += "\n\t\t\t</nav>\n\t\t</div>\n\t</body>\n</html>"

with open("start.html", "w") as out_file:
    out_file.write(output)
