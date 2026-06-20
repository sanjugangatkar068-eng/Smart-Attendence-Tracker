from flask import Flask, render_template_string, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "attendance_secret_key"

# Dummy teacher data
teachers = {
    "teacher1": "1234",
    "admin": "admin123"
}

# Login Page HTML
login_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Teacher Login</title>
    <style>
        body{
            font-family: Arial;
            background-color: #f0f2f5;
        }

        .login-box{
            width: 350px;  
            margin: 100px auto;
            padding: 30px;
            background: white;
            border-radius: 10px;
            box-shadow: 0px 0px 10px gray;
         
          h2{
              text-align: center;
        }