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
