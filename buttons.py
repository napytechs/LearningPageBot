from database import connection
from telebot import types
conn = connection()
c = conn.cursor(buffered=True)
from system import creator_id

def language_btn():
    both_btn = types.InlineKeyboardMarkup()
    en_btn = types.InlineKeyboardButton(text="π¬π§ English",callback_data='en')
    am_btn = types.InlineKeyboardButton(text="πͺπΉ α αα­α",callback_data='am')
    #back=types.InlineKeyboardButton(text="π Back" if lang == 'am' else "π α°ααα΅",callback_data='backwithdr')
    both_btn.add(en_btn,am_btn)
    return both_btn

def am_phone():
    all= types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("π± α΅αα­ αα₯α­ αα­",request_contact=True)
    all.add(btn)
    return all

def en_phone():
    all= types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("π±Send Phone Number",request_contact=True)
    all.add(btn)
    return all

def remove_btns():
    both_btn = types.ReplyKeyboardRemove(selective=True)
    return both_btn

def user_gender(lang, gen):
    all_btns = types.InlineKeyboardMarkup(row_width=5)
    umale = types.InlineKeyboardButton(text="π¨ ααα΅"+" β" if gen == 'π¨' else "π¨ ααα΅", callback_data="male")
    ufamale = types.InlineKeyboardButton(text="π§ α΄α΅"+" β" if gen =='π§' else "π§ α΄α΅", callback_data="famale")
    male = types.InlineKeyboardButton(text='π¨ Male'+" β" if gen == 'π¨'  else 'π¨ Male', callback_data="male")
    famale = types.InlineKeyboardButton(text='π§ Famale'+" β" if gen == 'π§' else 'π§ Famale', callback_data="famale")
    back = types.InlineKeyboardButton(text="π Back" if lang == 'en' else "π α°ααα΅",callback_data='back_gender')
    menu = types.InlineKeyboardButton(text="π  Main Menu" if lang == 'en' else "π  αα αα½",callback_data='main_gender')
    all_btns.add(male if lang == 'en' else umale, famale if lang == 'en' else ufamale)
    all_btns.add(back,menu)
    return all_btns

def books_btn(lang, type_book, grade):
    all_btn = types.InlineKeyboardMarkup(row_width=3)
    en = types.InlineKeyboardButton("π¬π§ English",callback_data=f'book:english:{type_book}:{grade}')
    am = types.InlineKeyboardButton("πͺπΉ α αα­α",callback_data=f'book:amharic:{type_book}:{grade}')
    chem = types.InlineKeyboardButton("π§ͺ Chemistry",callback_data=f'book:chemistry:{type_book}:{grade}')
    math = types.InlineKeyboardButton("π§? Math",callback_data=f'book:math:{type_book}:{grade}')
    phy = types.InlineKeyboardButton("π­ Physics ",callback_data=f'book:physics:{type_book}:{grade}')
    geo = types.InlineKeyboardButton("π§­ Geography",callback_data=f'book:geography:{type_book}:{grade}')
    his = types.InlineKeyboardButton("π History",callback_data=f'book:history:{type_book}:{grade}')
    ict = types.InlineKeyboardButton("π» ICT",callback_data=f'book:ict:{type_book}:{grade}')
    bio = types.InlineKeyboardButton("π¬ Biology",callback_data=f'book:biology:{type_book}:{grade}')
    civ = types.InlineKeyboardButton("β Civics",callback_data=f'book:civics:{type_book}:{grade}')
    hep = types.InlineKeyboardButton("β½οΈ HPE",callback_data=f'book:hpe:{type_book}')
    back = types.InlineKeyboardButton(text="π Back" if lang == 'en' else "π α°ααα΅", callback_data=f'book:back:{type_book}')
    menu = types.InlineKeyboardButton(text="π  Main Menu" if lang == 'en' else "π  αα αα½", callback_data='book:main')
    all_btn.add(math, phy, chem, bio, civ, geo, ict, hep, his, en, am)
    all_btn.add(back, menu)
    return all_btn

def user_setting(lang):
    all_btn = types.InlineKeyboardMarkup(row_width=5)
    lan = types.InlineKeyboardButton(text="π Language" if lang == 'en' else "π ααα",callback_data='lang')
    edit_p = types.InlineKeyboardButton(text='π Edit Profile' if lang == 'en' else "π αααα« α α΅α΅",callback_data='editp')
    close = types.InlineKeyboardButton(text='β Close' if lang == 'en' else "β αα",callback_data='closeS')
    all_btn.add(lan,edit_p)
    all_btn.add(close)
    return all_btn

def on_user_question(status, q_id):
    btn = types.InlineKeyboardMarkup()
    c = types.InlineKeyboardButton("β Cancel", callback_data=f'q:cancel:{q_id}')
    rs = types.InlineKeyboardButton("β Resubmit", callback_data=f'q:resubmit:{q_id}')

    if status == 'pending':
        btn.add(c)
    else:
        btn.add(rs)
    return btn


def main_buttons(l, user_id, **kwargs):
    all_btn = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3, one_time_keyboard=True)
    #home = types.KeyboardButton()
    send_m = types.KeyboardButton("π Send Message")
    bot_s = types.KeyboardButton("π€ Bot Setting")
    statics = types.KeyboardButton("π Statics")
    que = types.KeyboardButton("π§© Questions")
    books = types.KeyboardButton("π Books" if l == 'en' else "παα½ααα΅")
    ask = types.KeyboardButton("π£ Ask Question" if l == 'en' else "π£ α₯α«α α α­α" )
    ques = types.KeyboardButton("πββMy Questions" if l == 'en'  else "πββ α¨α α₯α«ααα½")
    invite = types.KeyboardButton("π¨βπ©βπ¦βπ¦ Invite" if l == 'en' else "π¨βπ©βπ¦βπ¦ αα₯α")
    setting = types.KeyboardButton("βοΈ Settings" if l == 'en'  else "βοΈ ααα₯α?α½")
    feedback = types.KeyboardButton("π¬ Feedback" if l == 'en' else "π¬ α α΅α³α¨α΅")
    all_btn.add(send_m if user_id == creator_id() or kwargs.get(str(user_id), {}).get('send_message') else "",
                bot_s if user_id == creator_id() or kwargs.get(str(user_id), {}).get('manage_setting') else "",
                statics if user_id == creator_id() or kwargs.get(str(user_id), {}).get('can_see') else "",
                que if user_id == creator_id() or kwargs.get(str(user_id),{}).get('approve_questions') else "")
    all_btn.add(books, ask)
    all_btn.add(ques, invite)
    all_btn.add(setting, feedback)
    return all_btn

def on_book_click(id, exist=False):
    btn = types.InlineKeyboardMarkup()
    if exist:
        btn.add(types.InlineKeyboardButton("π³ Balance", callback_data=f'ubook:bl:{id}'),
        types.InlineKeyboardButton("π Delete", callback_data=f'ubook:dl:{id}'))
    else:
        btn.add(types.InlineKeyboardButton("β Add", callback_data=f'ubook:add:{id}'))
        
    btn.add(types.InlineKeyboardButton("π Back", callback_data=f'ubook:back:{id}'))   
    return btn 

def user_profile_info(user_id, banned = False, admin_id = None, **kwargs):
    all = types.InlineKeyboardMarkup(row_width = 2)
    btn = []
    chat = types.InlineKeyboardButton("π Send Message", callback_data=f'user:chat:{user_id}')
    ban = types.InlineKeyboardButton("π· Ban" if not banned else "β Unban" , callback_data=f'user:ban:{user_id}'
                    if not banned else f"user:unban:{user_id}")
    sp = types.InlineKeyboardButton("π€ Show Profile" , callback_data=f'user:show:{user_id}')
    all.add(chat)
    if admin_id == creator_id() or kwargs.get(str(admin_id), {}).get(
        'ban_user'):
        btn.append(ban)
    if admin_id == creator_id() or kwargs.get(str(admin_id), {}).get(
        'can_see'):btn.append(sp)
    all.add(*btn)
    return all

def on_user_(user_id, banned = False, admin_id = None, **kwargs):
    all = types.InlineKeyboardMarkup(row_width=2)
    chat = types.InlineKeyboardButton("π€ Reply", callback_data=f'user:reply:{user_id}' )
    ban = types.InlineKeyboardButton("π· Ban" if not banned else "β Unban", callback_data=f'user:ban:{user_id}'
    if not banned else f"user:unban:{user_id}")
    btn = []
    sp = types.InlineKeyboardButton("π€ Show Profile", callback_data=f'user:show:{user_id}')
    if admin_id == creator_id() or kwargs.get(str(admin_id), {}).get(
        'ban_member'):
        btn.append(ban)
    if admin_id == creator_id() or kwargs.get(str(admin_id), {}).get(
        'can_see'):
        btn.append(sp)
    all.add(chat, *btn)
    return all

def on_answer(user_id, q_id, ans_id):
    btn = types.InlineKeyboardMarkup()
    btn.add(
        types.InlineKeyboardButton("β© Reply", callback_data=f'areply:{user_id}:{q_id}:{ans_id}'),
        types.InlineKeyboardButton("β  Report", callback_data=f'report:{user_id}')
    )
    return btn

def types_book_am():
    all_btn = types.InlineKeyboardMarkup(row_width=2)
    edu = types.InlineKeyboardButton("π Student Book",callback_data='edus')
    edut = types.InlineKeyboardButton("π Teachers Guide",callback_data='edut')
    ref = types.InlineKeyboardButton("π Reference Book",callback_data='edutref')
    all_btn.add(edu, edut, ref)
    return all_btn

def edit_profile(id:int,lang):
    all_btn = types.InlineKeyboardMarkup(row_width=2)
    edit_fname = types.InlineKeyboardButton("πββοΈ Edit Name",callback_data='fname')
    edit_username = types.InlineKeyboardButton("π² Edit Username",callback_data='_username')
    edit_bio = types.InlineKeyboardButton("π Edit Bio",callback_data='bio')
    back = types.InlineKeyboardButton(text="π Back" if lang == 'en' else "π α°ααα΅",callback_data='back_edit')
    gender = types.InlineKeyboardButton(f"π» Edit Gender",callback_data='gender')
    all_btn.add(edit_fname, edit_username, edit_bio, gender, back)
    return all_btn

def question_btn(q_id):
    all_btn = types.InlineKeyboardMarkup(row_width=5)
    approve = types.InlineKeyboardButton(text="β« Approve",callback_data=f'uq_approve_{q_id}')
    disapp =types.InlineKeyboardButton(text="β¬ Decline",callback_data=f'uq_decline_{q_id}')
    all_btn.add(approve, disapp)
    return all_btn

def bot_setting_btn():
    btns = types.InlineKeyboardMarkup(row_width=2)
    btns.add(
        types.InlineKeyboardButton("π³ Balance", callback_data='bot:balance'),
        types.InlineKeyboardButton("π£ Channels", callback_data='bot:channels'),
        types.InlineKeyboardButton("π Manage Admins", callback_data='bot:admins')

    )
    return btns

def cancel(user_lang):
    btn = types.ReplyKeyboardMarkup(resize_keyboard=True)
    can = types.KeyboardButton("β Cancel" if user_lang=='en' else "β α°α­α")
    return btn.add(can)


def Panel(q_id):
    all_btn=types.InlineKeyboardMarkup(row_width=3)
    send = types.InlineKeyboardButton(text="β Submit",callback_data=f'send_{q_id}')
    edit=types.InlineKeyboardButton(text="β Edit",callback_data=f'edit_{q_id}')
    delete = types.InlineKeyboardButton(text="π Delete",callback_data=f'del_{q_id}')
    all_btn.add(send,edit,delete)
    return all_btn

def withdraw(lang,link):
    all_btn = types.InlineKeyboardMarkup(row_width=5)
    withdr =types.InlineKeyboardButton(text="π³ Withdraw" if lang == 'en' else "π³ ααͺ α α­α",callback_data='withdr')
    share = types.InlineKeyboardButton(text="β€΄ Share" if lang == 'en' else 'β€΄ α αα«',url=link)
    bonus = types.InlineKeyboardButton(text="π Bonus",callback_data='bonus')
    bt = types.InlineKeyboardButton(text="πΈ Transfer Birr" if lang == 'en' else "πΈ α₯α­ α α΅α°ααα",callback_data='bt')
    all_btn.add(withdr,bonus)
    all_btn.add(bt)
    all_btn.add(share)
    return all_btn

def grade(lang, type_book):
    all_btn = types.InlineKeyboardMarkup(row_width=3)
    #g6 = types.InlineKeyboardButton(text="6οΈβ£",callback_data='g6')
    g7 = types.InlineKeyboardButton(text="7",callback_data=f'grade_7_{type_book}')
    g8 = types.InlineKeyboardButton(text="8",callback_data=f'grade_8_{type_book}')
    g9 = types.InlineKeyboardButton(text="9",callback_data=f'grade_9_{type_book}')
    g10 = types.InlineKeyboardButton(text="10",callback_data=f'grade_10_{type_book}')
    g11 = types.InlineKeyboardButton(text="11",callback_data=f'grade_11_{type_book}')
    g12 = types.InlineKeyboardButton(text="12",callback_data=f'grade_12_{type_book}')
    back=types.InlineKeyboardButton(text="π Back" if lang == 'en' else "π α°ααα΅",callback_data='backgrade')
    all_btn.add(g7,g8,g9)
    all_btn.add(g10,g11,g12)
    all_btn.add(back)
    return all_btn

def subject_btn(lang):
    all_btn = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    en = types.KeyboardButton("π¬π§ English")
    am = types.KeyboardButton("πͺπΉ α αα­α")
    chem = types.KeyboardButton("π§ͺ Chemistry")
    math = types.KeyboardButton("π§? Math")
    phy = types.KeyboardButton("π­ Physics")
    geo = types.KeyboardButton("π§­ Geography")
    his = types.KeyboardButton("π History")
    ict = types.KeyboardButton("π» ICT")
    bio = types.KeyboardButton("π¬ Biology")
    civ = types.KeyboardButton("β Civics")
    hep = types.KeyboardButton("β½οΈ HPE")
    can = types.KeyboardButton("β Cancel" if lang=='en' else "β α°α­α")
    all_btn.add(math, phy, chem, bio, ict, geo, civ, his, hep, en, am, can)
    return all_btn

def amounts(lang):
    all_btn = types.InlineKeyboardMarkup(row_width=2)
    _5=types.InlineKeyboardButton(text="5 Birr",callback_data='5-birr')
    _10=types.InlineKeyboardButton(text="10 Birr",callback_data='10-birr')
    _15=types.InlineKeyboardButton(text="15 Birr",callback_data='15-birr')
    _20=types.InlineKeyboardButton(text="20 Birr",callback_data='20-birr')
    _25=types.InlineKeyboardButton(text="25 Birr",callback_data='25-birr')
    _50=types.InlineKeyboardButton(text="50 Birr",callback_data='50-birr')
    _75=types.InlineKeyboardButton(text="75 Birr",callback_data='75-birr')
    _100=types.InlineKeyboardButton(text="100 Birr",callback_data='100-birr')
    back=types.InlineKeyboardButton(text="π Back" if lang == 'en' else "π α°ααα΅",callback_data='backwithdr')
    all_btn.add(_15, _20, _25, _50, _75, _100)
    #all_btn.add(_20,_25,_50)
    #all_btn.add(_75,_100)
    all_btn.add(back)
    return all_btn

def answer_btn(q_id, ans_id):
    all_btn=types.InlineKeyboardMarkup(row_width=3)
    send = types.InlineKeyboardButton(text="β Submit",callback_data=f'SendAnswer_{q_id}_{ans_id}')
    edit=types.InlineKeyboardButton(text="β Edit",callback_data=f'EditAnswer_{q_id}_{ans_id}')
    delete = types.InlineKeyboardButton(text="π Delete",callback_data=f'DelAnswer_{q_id}_{ans_id}')
    all_btn.add(send,edit,delete)
    return all_btn

def bscancel():
    btn = types.InlineKeyboardMarkup()
    btn.add(types.InlineKeyboardButton("π« Cancel", callback_data='bscancel'))
    return btn

def admin_permision_btn(user_id, stat, **kwargs):
    btn = types.InlineKeyboardMarkup(row_width=2)
    btn.add(*[types.InlineKeyboardButton("π Message β" if kwargs.get(user_id, {}).get("send_message")
                                         else "π Message β", callback_data=f'admin:send_message:{user_id}'),
              types.InlineKeyboardButton("Approve  β" if kwargs.get(user_id, {}).get("approve_questions")
                                         else "Approve β", callback_data=f'admin:approve_questions:{user_id}'),
              types.InlineKeyboardButton("π­ Feedback β" if kwargs.get(user_id,{}).get("feedback") else "π­ Feedback β",
                                         callback_data=f'admin:feedback:{user_id}'),
              types.InlineKeyboardButton("π· Ban β" if kwargs.get(user_id,{}).get("ban_user") else "π· Ban β",
                                         callback_data=f'admin:ban_user:{user_id}'),
              types.InlineKeyboardButton("π  Manage β" if kwargs.get(user_id, {}).get("manage_setting") else "π  Manage β",
                                         callback_data=f'admin:manage_setting:{user_id}'),
              types.InlineKeyboardButton(
                  "π€ Profile β" if kwargs.get(user_id, {}).get("can_see") else "π€ Profile β",
                  callback_data=f'admin:can_see:{user_id}'),
              types.InlineKeyboardButton("β Remove", callback_data=f'admin:remove:{user_id}'),
              ]
            )

    info = []
    try:
        for key in kwargs.get(user_id):
            info.append(
    kwargs.get(user_id, {}).get(key))
    except:
        info.append(False)
    if not False in info:
              types.InlineKeyboardButton("π¨βπ» Ownership", callback_data=f'admin:owner:{user_id}')
    if not stat == 'admin':
        btn.add(types.InlineKeyboardButton("β Done", callback_data=f'admin:done:{user_id}'))
    else:
        btn.add(types.InlineKeyboardButton("π Back", callback_data=f'admin:back:{user_id}'))

    return btn

def channel_btn(channel_id, **kwargs):
    btn = types.InlineKeyboardMarkup(row_width=2)
    btn.add(
        types.InlineKeyboardButton("Message β" if kwargs.get(channel_id).get('send_message') else "Message β",
                                   callback_data=f"myc:{channel_id}:send_message"),
        types.InlineKeyboardButton("Approve β" if kwargs.get(channel_id).get('approve') else "Approve β",
                               callback_data=f"myc:{channel_id}:approve"),
        types.InlineKeyboardButton("Join β" if kwargs.get(channel_id).get('force_join') else "Join β",
                                   callback_data=f'myc:{channel_id}:force_join'),
    )
    btn.add(
        types.InlineKeyboardButton("β Remove", callback_data=f"myc:{channel_id}:remove"),
        types.InlineKeyboardButton("π Back", callback_data=f'myc:{channel_id}:back')
    )
    return btn
subj=["π¬π§ English", "πͺπΉ α αα­α", "π§ͺ Chemistry", "π§? Math", "π­ Physics", "β½οΈ HPE", "π¬ Biology", "π» ICT", "π History",
      "π§­ Geography", "πͺ Civics"]

am_btns = ["παα½ααα΅", "πββ α¨α α₯α«ααα½", "π¨βπ©βπ¦βπ¦ αα₯α","βοΈ ααα₯α?α½", "π£ α₯α«α α α­α", "π¬ α α΅α³α¨α΅"]

en_btns =["πββMy Questions", "π Books", "π¬ Feedback", "π¨βπ©βπ¦βπ¦ Invite", "βοΈ Settings", "π£ Ask Question"]
