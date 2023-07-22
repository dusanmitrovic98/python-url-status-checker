from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

template = """
