from flask import Flask, request, render_template, redirect, url_for
import mysql.connector
#from conf_eval import db
#from conf_eval.models.query_saved import Query

app = Flask(__name__)

"""
# データベース接続情報
db_config = {
    'user': 'root',
    'password': '4.sE/11R7*>v_p.',  # 適切なパスワードを設定
    'host': 'localhost',
    'database': 'grad_res'  # データベース名
}
"""


@app.route('/add_query', methods=['GET', 'POST'])
def add_query():
    if request.method == 'GET':
        return render_template('que_dis/add_query.html')
    if request.method == 'POST':
        query = Query(
            theme_number=1,
            user_name="マロイタ",
            query_saved="スーパーフード  健康"
        )
        db.session.add(query)
        db.session.commit()
        return render_template('que_dis/add_query.html')


@app.route('/g1_save', methods=['GET', 'POST'])
def user_save():
    if request.method == 'GET':
        return render_template('g1/common_page_5.html')
    if request.method == 'POST':
        form_group = request.form.get('group')
        form_name = request.form.get('username')
        user = User(
            group_selected=form_group,
            user_name=form_name,
        )
        db.session.add(user)
        db.session.commit()
        return render_template('g1/common_page_5.html')
    

@app.route('/')
def index():
    return render_template('/g1/common_page_1.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)




#g1のルーティング
@app.route('/g1/common_page_1')
def g1_common1():
    return render_template('templates/g1/common_page_1.html')

@app.route('/g1/common_page_2')
def g1_common2():
    return render_template('templates/g1/common_page_2.html')

@app.route('/g1/common_page_3')
def g1_common3():
    return render_template('templates/g1/common_page_3.html')

@app.route('/g1/common_page_4')
def g1_common4():
    return render_template('templates/g1/common_page_4.html')

@app.route('/g1/common_page_5')
def g1_common5():
    return render_template('templates/g1/common_page_5.html')

@app.route('/g1/common_page_6')
def g1_common6():
    return render_template('templates/g1/common_page_6.html')

@app.route('/g1/common_page_7')
def g1_common7():
    return render_template('templates/g1/common_page_7.html')

@app.route('/g1/common_page_8')
def g1_common8():
    return render_template('templates/g1/common_page_8.html')

@app.route('/g1/common_page_9')
def g1_common9():
    return render_template('templates/g1/common_page_9.html')
    
@app.route('/g1/page_1')
def g1_1():
    return render_template('templates/g1/page_1.html')

@app.route('/g1/page_2')
def g1_2():
    return render_template('templates/g1/page_2.html')

@app.route('/g1/page_3')
def g1_3():
    return render_template('templates/g1/page_3.html')

@app.route('/g1/page_4')
def g1_4():
    return render_template('templates/g1/page_4.html')

@app.route('/g1/page_5')
def g1_5():
    return render_template('templates/g1/page_5.html')

@app.route('/g1/page_6')
def g1_6():
    return render_template('templates/g1/page_6.html')

@app.route('/g1/page_7')
def g1_7():
    return render_template('templates/g1/page_7.html')


#g2のルーティング
@app.route('/g2/common_page_1')
def g2_common1():
    return render_template('templates/g2/common_page_1.html')

@app.route('/g2/common_page_2')
def g2_common2():
    return render_template('templates/g2/common_page_2.html')

@app.route('/g2/common_page_3')
def g2_common3():
    return render_template('templates/g2/common_page_3.html')

@app.route('/g2/common_page_4')
def g2_common4():
    return render_template('templates/g2/common_page_4.html')

@app.route('/g2/common_page_5')
def g2_common5():
    return render_template('templates/g2/common_page_5.html')

@app.route('/g2/common_page_6')
def g2_common6():
    return render_template('templates/g2/common_page_6.html')

@app.route('/g2/common_page_7')
def g2_common7():
    return render_template('templates/g2/common_page_7.html')

@app.route('/g2/common_page_8')
def g2_common8():
    return render_template('templates/g2/common_page_8.html')

@app.route('/g2/common_page_9')
def g2_common9():
    return render_template('templates/g2/common_page_9.html')
    
@app.route('/g2/page_1')
def g2_1():
    return render_template('templates/g2/page_1.html')

@app.route('/g2/page_2')
def g2_2():
    return render_template('templates/g2/page_2.html')

@app.route('/g2/page_3')
def g2_3():
    return render_template('templates/g2/page_3.html')

@app.route('/g2/page_4')
def g2_4():
    return render_template('templates/g2/page_4.html')

@app.route('/g2/page_5')
def g2_5():
    return render_template('templates/g2/page_5.html')

@app.route('/g2/page_6')
def g2_6():
    return render_template('templates/g2/page_6.html')

@app.route('/g2/page_7')
def g2_7():
    return render_template('templates/g2/page_7.html')


#g3のルーティング
@app.route('/g3/common_page_1')
def g3_common1():
    return render_template('templates/g3/common_page_1.html')

@app.route('/g3/common_page_2')
def g3_common2():
    return render_template('templates/g3/common_page_2.html')

@app.route('/g3/common_page_3')
def g3_common3():
    return render_template('templates/g3/common_page_3.html')

@app.route('/g3/common_page_4')
def g3_common4():
    return render_template('templates/g3/common_page_4.html')

@app.route('/g3/common_page_5')
def g3_common5():
    return render_template('templates/g3/common_page_5.html')

@app.route('/g3/common_page_6')
def g3_common6():
    return render_template('templates/g3/common_page_6.html')

@app.route('/g3/common_page_7')
def g3_common7():
    return render_template('templates/g3/common_page_7.html')

@app.route('/g3/common_page_8')
def g3_common8():
    return render_template('templates/g3/common_page_8.html')

@app.route('/g3/common_page_9')
def g3_common9():
    return render_template('templates/g3/common_page_9.html')
    
@app.route('/g3/page_1')
def g3_1():
    return render_template('templates/g3/page_1.html')

@app.route('/g3/page_2')
def g3_2():
    return render_template('templates/g3/page_2.html')

@app.route('/g3/page_3')
def g3_3():
    return render_template('templates/g3/page_3.html')

@app.route('/g3/page_4')
def g3_4():
    return render_template('templates/g3/page_4.html')

@app.route('/g3/page_5')
def g3_5():
    return render_template('templates/g3/page_5.html')

@app.route('/g3/page_6')
def g3_6():
    return render_template('templates/g3/page_6.html')

@app.route('/g3/page_7')
def g3_7():
    return render_template('templates/g3/page_7.html')

@app.route('/g3/page_8')
def g3_8():
    return render_template('templates/g3/page_8.html')

@app.route('/g3/page_9')
def g3_9():
    return render_template('templates/g3/page_9.html')


#g4のルーティング
@app.route('/g4/common_page_1')
def g4_common1():
    return render_template('templates/g4/common_page_1.html')

@app.route('/g4/common_page_2')
def g4_common2():
    return render_template('templates/g4/common_page_2.html')

@app.route('/g4/common_page_3')
def g4_common3():
    return render_template('templates/g4/common_page_3.html')

@app.route('/g4/common_page_4')
def g4_common4():
    return render_template('templates/g4/common_page_4.html')

@app.route('/g4/common_page_5')
def g4_common5():
    return render_template('templates/g4/common_page_5.html')

@app.route('/g4/common_page_6')
def g4_common6():
    return render_template('templates/g4/common_page_6.html')

@app.route('/g4/common_page_7')
def g4_common7():
    return render_template('templates/g4/common_page_7.html')

@app.route('/g4/common_page_8')
def g4_common8():
    return render_template('templates/g4/common_page_8.html')

@app.route('/g4/common_page_9')
def g4_common9():
    return render_template('templates/g4/common_page_9.html')
    
@app.route('/g4/page_1')
def g4_1():
    return render_template('templates/g4/page_1.html')

@app.route('/g4/page_2')
def g4_2():
    return render_template('templates/g4/page_2.html')

@app.route('/g4/page_3')
def g4_3():
    return render_template('templates/g4/page_3.html')

@app.route('/g4/page_4')
def g4_4():
    return render_template('templates/g4/page_4.html')

@app.route('/g4/page_5')
def g4_5():
    return render_template('templates/g4/page_5.html')

@app.route('/g4/page_6')
def g4_6():
    return render_template('templates/g4/page_6.html')

@app.route('/g4/page_7')
def g4_7():
    return render_template('templates/g4/page_7.html')

@app.route('/g4/page_8')
def g4_8():
    return render_template('templates/g4/page_8.html')

@app.route('/g4/page_9')
def g4_9():
    return render_template('templates/g4/page_9.html')




"""
@app.route('/queryform_post', methods=['GET', 'POST'])
def queryform_post():
    if request.method == 'GET':
        return render_template('templates/g3/queryform_post.html')
    if request.method == 'POST':
        
        form_theme = request.form.get('theme', type=int)
        form_name = request.form.get('username')
        form_query = request.form.get('search_query')

        sea_que = search_query(
            theme_number=form_theme,
            user_name=form_name,
            query_saved=form_query,
        )
        db.session.add(sea_que)
        db.session.commit()
        
        if form_theme == 1:
            return render_template('page_4.html')
        elif form_theme == 2:
            return render_template('page_7.html')

@app.route('/page_17')
def employee_list():
    seaque_saved = search_query.query.all()
    return render_template('que_dis/query_list.html', seaque_saved=seaque_saved)

@app.route('/page_17/<user_name>')
def query_detail(user_name):
    seaque_saved = search_query.query.get(user_name)
    return render_template('que_dis/query_detail.html', seaque_saved=seaque_saved)


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



@app.route('/queryform_post', methods=['GET', 'POST'])
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
"""