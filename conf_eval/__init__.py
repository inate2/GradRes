from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # 追加

app = Flask(__name__)
app.config.from_object('conf_eval.config')

db = SQLAlchemy(app)  # 追加
from .models import user_information  # 追加
from .models import query_saved  # 追加

import conf_eval.views