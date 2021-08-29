# -----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
# -----------------------------------------------------------------------------------------

from flask import Flask,  render_template
import requests
import json
app = Flask(__name__)

config_file_path = "config"


@app.route("/")
def home():
    with open(config_file_path, "r") as config_file:
        template_sources = config_file.readlines()
    return render_template("index.html", template_sources=template_sources)


@app.route("/template.json")
def template_json():
    with open(config_file_path, "r") as config_file:
        template_sources = config_file.readlines()
        all_templates = []
        for template_source in template_sources:
            templates = requests.get(template_source.strip()).json()[
                'templates']
            all_templates = all_templates + templates
    result = {"version": "2", "templates": all_templates}
    return json.dumps(result)
