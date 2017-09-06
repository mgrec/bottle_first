<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="static/master.css">
    <title>Document</title>
</head>
<body>
%if name == 'default':
    <h1>Hello !</h1>
%else:
    <h1>Hello {{ name }} !</h1>
%end
</body>
</html>