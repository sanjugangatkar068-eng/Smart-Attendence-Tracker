from flask import Flask, render_template_string, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "attendance_secret_key"

teachers = {
    "teacher1": "1234",
    "admin": "admin123"
}
login_page = """
<!DOCTYPE html>