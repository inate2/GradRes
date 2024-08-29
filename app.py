from flask import Flask, request, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

# データベース接続情報
db_config = {
    'user': 'root',
    'password': '4.sE/11R7*>v_p.',  # 適切なパスワードを設定
    'host': 'localhost',
    'database': 'grad_res'  # データベース名
}

@app.route('/')
def index():
    return render_template('page_1.html')

@app.route('/save', methods=['POST'])
def save_text():
    # フォームから送信された選択肢とテキストを取得
    group = request.form.get('group')
    username = request.form.get('username')

    # 両方のフィールドが入力されているかチェック
    if group and username:
        # MySQLに接続してデータを保存
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # テーブルにデータを挿入するSQLクエリ
            sql = "INSERT INTO texts (group_selected, user_name) VALUES (%s, %s)"
            cursor.execute(sql, (group, username))
            conn.commit()

            cursor.close()
            conn.close()

            # データ保存後、「page_5.html」にリダイレクト
            return render_template('page_5.html')
        
        except mysql.connector.Error as err:
            return f"データベースエラー: {err}"
    else:
        # 両方のフィールドが入力されていない場合、エラーメッセージを表示
        return "エラー: 選択肢とテキストの両方を入力してください。"

if __name__ == '__main__':

    app.debug = True
    app.run(host='localhost', port=8888)