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
<form action="" method="post">
    <input type="text" name="btl_username">
    <input type="password" name="btl_pass">
    <button type="submit">Connection</button>
</form>
%if login == 'true':
<p>You're now connected</p>
%elif login == 'error':
<p>Login error</p>
%end
</body>
</html>