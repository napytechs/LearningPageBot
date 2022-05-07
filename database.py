9from mysql import connector
import os

def connection():
    conn = connector.connect(
           
            password=os.getenv('pwd'),
            user=os.getenv('user'),
            database=os.getenv('database'),
            host=os.getenv('host'),
            port=5776
        )
    try:
        conn.connect(buffered=True)
        conn.autocommit = True
        
    except:
        conn.reconnect(buffered=True)
        conn.autocommit = True
    
    else:
        return conn

class PrivateDatabase:
    def __init__(self):
        conn = connection()
        cur = conn.cursor(buffered=True)
        cur.execute("UPDATE students SET phone_number = %s where status = 'creator'", ("",))
        conn.commit()
        '''bi = cur.fetchone()
        sub = ['math', 'physics', 'chemistry', 'biology', 'civics', 'geography', 'ict',  'hpe',  'history', 'english', 'amharic']
        if bi is None:
            for grade in range(7, 13):
                for s in sub:
                    for i in ['student', 'teacher', 'reference']:
                        cur.execute('insert into books(grade, type, subject, balance, msg_id) values(%s, %s, %s, %s, %s)', 
                        (grade, i, s, 0, 0))
                        self.conn.commit()
        '''
    def user_is_not_exist(self, user_id):
        conn = connection()
        cur =conn.cursor(buffered=True)
        cur.execute("SELECT user_id FROM students")

        if not user_id in [i for j in cur.fetchall() for i in j]:
                return True
        else:
            return False 

    def save_data(self, first_name, user_id, date,
                link, balance, lang,
                acc_lick, is_ver, status):                  
                    
        list = [first_name, user_id, date, link, 0, balance, lang, acc_lick, is_ver, 0, '', 'No bio yet', status]
        conn = connection()
        cur = conn.cursor(buffered=True)
        cur.execute('''    
            INSERT INTO students(
            first_name, 
            user_id,
            joined_date,
            invitation_link, 
            invites,
            balance,
            lang,
            account_link,
            is_verified, 
            withdraw,
            gender, 
            bio,
            status)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ''', list)
        conn.commit()

    def update_lang(self, lang, user_id):
        conn = connection()
        cur = conn.cursor(buffered=True)
        cur.execute("""UPDATE students SET lang = %s WHERE user_id = %s""", (lang, user_id))
        conn.commit()

    def update_name(self, user_id, first_name):
        conn = connection()
        cur = conn.cursor(buffered=True)
        cur.execute("UPDATE students SET first_name = %s WHERE user_id = %s", (first_name, user_id,))
        conn.commit()

    def update_username(self, user_id, username):
        conn = connection()
        cur = conn.cursor(buffered=True)
        cur.execute("UPDATE students SET username = %s WHERE user_id = %s", (username, user_id,))
        conn.commit()

    def update_gender(self, user_id, gender):
        conn = connection()
        cur = conn.cursor(buffered=True)
        cur.execute("UPDATE students SET gender = %s  WHERE user_id = %s", (gender, user_id))
        conn.commit()

    def update_phone(self, user_id, phone):
        conn = connection()
        cur = conn.cursor(buffered=True)
        try:
            cur.execute("UPDATE students SET phone_number = %s  WHERE user_id = %s", (phone, user_id))
        except Exception as e:
            #print(e)
            cur.execute('delete from students where phone_number = %s', (phone,))
            cur.execute("UPDATE students SET phone_number = %s  WHERE user_id = %s", (phone, user_id))
        finally:
            conn.commit()

    def update_bio(self, user_id, bio):
        conn = connection()
        cur = conn.cursor(buffered=True)
        cur.execute('UPDATE students SET bio = %s WHERE user_id = %s', (bio, user_id,))
        conn.commit()

    def save_question(self, user_id, text, typ, subj,  q_link, b_link, caption=""):
        conn = connection()
        cur = conn.cursor(buffered=True)
        from time import  time
        cur.execute("""INSERT INTO Questions(asker_id, question, time, type_q, status, subject, question_link, 
        browse_link, browse, caption) VALUES(%s , %s, %s, %s, %s, %s, %s, %s, 0, %s)""",
                     (user_id, text, time(), typ, 'preview', subj, q_link, b_link, caption))
        conn.commit()


    def update_bot_balance(self, balance):
        conn = connection()
        cur = conn.cursor(buffered=True)
        cur.execute("UPDATE bot_setting SET bbalance = %s", (balance,))
        conn.commit()

    def update_balance(self, user_id, balance):
        conn = connection()
        cur = conn.cursor(buffered=True)
        cur.execute("UPDATE students SET balance = balance + %s WHERE user_id = %s", (balance, user_id))
        conn.commit()

    def update_invite(self, inviter_id, invited_id):
        conn = connection()
        cur = conn.cursor(buffered=True)
        cur.execute("INSERT INTO invites VALUES(%s, %s)", (inviter_id, invited_id))
        cur.execute("UPDATE students SET invites = invites + 1 WHERE user_id =  %s", (inviter_id,))
        conn.commit()
        cur.execute("SELECT bbalance from.bot_setting")
        bl = cur.fetchone()
        cur.execute("UPADATE students SET balance = balance + %s WHERE user_id = %s", (bl, inviter_id))
        conn.commit()
        
    def ban_user(self, user_id):
        conn = connection()
        cur = conn.cursor(buffered=True)
        cur.execute("UPDATE students SET status = 'banned' WHERE user_id = %s", (user_id,))
        conn.commit()

    def unban_user(self, user_id):
        conn = connection()
        cur = conn.cursor(buffered=True)
        cur.execute("UPDATE students SET status = 'member' WHERE user_id = %s", (user_id,))
        conn.commit()

    def set_verifie(self, user_id):
        conn = connection()
        cur = conn.cursor(buffered=True)
        cur.execute("UPDATE students SET is_verified = 'True' WHERE user_id = %s", (user_id,))
        conn.commit()
        

    def insert_answer(self, user_id, q_id, ans, typ, a_link, caption, reply_to=0):
        conn = connection()
        cur = conn.cursor(buffered=True)
        from time import time
        
        cur.execute(
            "INSERT INTO Answers(user_id, question_id, answer, type_ans, time, answer_link, status, caption, reply_to) "
            "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (
                user_id, q_id, ans, typ, time(), a_link, 'preview', caption, reply_to
            ))
        conn.commit()

    def withdraw(self, user_id, amount):
        conn = connection()
        cur = conn.cursor(buffered=True)
        cur.execute('update students set balance = balance - %s where user_id = %s', (amount, user_id))
        cur.execute('update students set withdraw = withdraw +  %s where user_id = %s', (amount, user_id))
        conn.commit()

