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