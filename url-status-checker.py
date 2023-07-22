from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

template = """
<!DOCTYPE html>
<html>
<head>
    <title>URL Status Checker</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-fork-ribbon-css/0.2.3/gh-fork-ribbon.min.css" />
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            text-align: center;
            background-color: #6e6e80;
        }
        .container {
            max-width: 400px;
            margin: 0 auto;
        }
        .form-group {
            margin-bottom: 10px;
        }
        .btn {
            background-color: #2EA44F;
            color: white;
