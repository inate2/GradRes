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
    return render_template('templates/page_1.html')

@app.route('/page_2')
def index():
    return render_template('templates/page_2.html')

@app.route('/page_3')
def index():
    return render_template('templates/page_3.html')

@app.route('/page_4')
def index():
    return render_template('templates/page_4.html')

@app.route('/page_5')
def index():
    return render_template('templates/page_5.html')

@app.route('/page_11')
def index():
    return render_template('templates/page_11.html')

@app.route('/page_12')
def index():
    return render_template('templates/page_12.html')

@app.route('/page_21')
def index():
    return render_template('templates/page_21.html')

@app.route('/page_22')
def index():
    return render_template('templates/page_22.html')

@app.route('/g1/page_1')
def index():
    return render_template('templates/g1/page_1.html')

@app.route('/g1/page_2')
def index():
    return render_template('templates/g1/page_2.html')

@app.route('/g1/page_3')
def index():
    return render_template('templates/g1/page_3.html')

@app.route('/g1/page_4')
def index():
    return render_template('templates/g1/page_4.html')

@app.route('/g1/page_5')
def index():
    return render_template('templates/g1/page_5.html')

@app.route('/g1/page_6')
def index():
    return render_template('templates/g1/page_6.html')

@app.route('/g1/page_7')
def index():
    return render_template('templates/g1/page_7.html')

@app.route('/g2/page_1')
def index():
    return render_template('templates/g2/page_1.html')

@app.route('/g2/page_2')
def index():
    return render_template('templates/g2/page_2.html')

@app.route('/g2/page_3')
def index():
    return render_template('templates/g2/page_3.html')

@app.route('/g2/page_4')
def index():
    return render_template('templates/g2/page_4.html')

@app.route('/g2/page_5')
def index():
    return render_template('templates/g2/page_5.html')

@app.route('/g2/page_6')
def index():
    return render_template('templates/g2/page_6.html')

@app.route('/g2/page_7')
def index():
    return render_template('templates/g2/page_7.html')

@app.route('/g3/page_1')
def index():
    return render_template('templates/g3/page_1.html')

@app.route('/g3/page_2')
def index():
    return render_template('templates/g3/page_2.html')

@app.route('/g3/page_3')
def index():
    return render_template('templates/g3/page_3.html')

@app.route('/g3/page_4')
def index():
    return render_template('templates/g3/page_4.html')

@app.route('/g3/page_5')
def index():
    return render_template('templates/g3/page_5.html')

@app.route('/g3/page_6')
def index():
    return render_template('templates/g3/page_6.html')

@app.route('/g3/page_7')
def index():
    return render_template('templates/g3/page_7.html')

@app.route('/g3/page_16')
def index():
    return render_template('templates/g3/page_16.html')

@app.route('/g3/page_17')
def index():
    return render_template('templates/g3/page_17.html')

@app.route('/g4/page_1')
def index():
    return render_template('templates/g4/page_1.html')

@app.route('/g4/page_2')
def index():
    return render_template('templates/g4/page_2.html')

@app.route('/g4/page_3')
def index():
    return render_template('templates/g4/page_3.html')

@app.route('/g4/page_4')
def index():
    return render_template('templates/g4/page_4.html')

@app.route('/g4/page_5')
def index():
    return render_template('templates/g4/page_5.html')

@app.route('/g4/page_6')
def index():
    return render_template('templates/g4/page_6.html')

@app.route('/g4/page_7')
def index():
    return render_template('templates/g4/page_7.html')

@app.route('/g4/page_16')
def index():
    return render_template('templates/g4/page_16.html')

@app.route('/g4/page_17')
def index():
    return render_template('templates/g4/page_17.html')


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

@app.route('/query_save', methods=['POST'])
def save_text():
    # フォームから送信された選択肢とテキストを取得
    theme = request.form.get('theme')
    username = request.form.get('username')
    search_query = request.form.get('search_query')

    # 両方のフィールドが入力されているかチェック
    if theme and username and search_query:
        # MySQLに接続してデータを保存
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # テーブルにデータを挿入するSQLクエリ
            sql = "INSERT INTO texts (theme_selected, user_name, search_query) VALUES (%s, %s, %s)"
            cursor.execute(sql, (theme, username, search_query))
            conn.commit()

            cursor.close()
            conn.close()

            # データ保存後、「同じページ」にリダイレクト
            if theme == 'theme1':
                return render_template('page_4.html')
            elif theme == 'theme2':
                return render_template('page_7.html')
        
        except mysql.connector.Error as err:
            return f"データベースエラー: {err}"
    else:
        # 両方のフィールドが入力されていない場合、エラーメッセージを表示
        return "エラー: 選択肢とテキストの両方を入力してください。"

if __name__ == '__main__':

    app.debug = True
    app.run(host='localhost', port=8888)