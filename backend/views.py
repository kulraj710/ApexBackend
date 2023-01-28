from django.http import HttpResponse

def index(request):
    return HttpResponse('''
<!doctype html>
<html lang="en">
  <head>
    <title>Apex Children Hospital</title>
    <link rel="shortcut icon" href="data:image/x-icon;," type="image/x-icon">
  </head>
  <body>
    <h1>Homepage For Apex Children Hospital</h1>
    <h2>Server Page</h2>
  </body>
</html>
                        ''')