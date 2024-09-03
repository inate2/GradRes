from conf_eval import db

class Query(db.Model):
    __tablename__ = 'query_registered'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # システムで使う番号
    theme_number = db.Column(db.Integer)  # テーマ番号
    user_name = db.Column(db.String(255))  # ユーザ名
    query_saved = db.Column(db.String(255))  # 保存されたクエリ