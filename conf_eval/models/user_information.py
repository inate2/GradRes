from conf_eval import db

class User(db.Model):
    __tablename__ = 'user_registered'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # システムで使う番号
    group_selected = db.Column(db.String(255))  # グループ名
    user_name = db.Column(db.String(255))  # ユーザ名