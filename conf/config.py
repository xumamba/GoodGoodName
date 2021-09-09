# 强烈建议修改
LAST_NAME = '孙'  # 姓氏
SEX = '女'  # 孩子性别，男 或者 女
year = 2021  # 出生的时间：年
month = 9  # 出生的时间：月
date = 6  # 出生的时间：日
hour = 00  # 出生的时间：小时
minute = 3  # 出生的时间： 分钟

# 选择性修改
MIN_SINGLE_NUM = 2  # 单个字最少笔画过滤
MAX_SINGLE_NUM = 20  # 单个字最多笔画过滤
THRESHOLD_SCORE = 85  # 三才五格测试最低能接受的得分，结果记录在RESULT_FILE
SELECTED_XITONGSHEN = None  # 已知的喜用神，或者次喜用神。None表示没关系。这个喜用神自己在网站查查，选填，填了可能没有最佳匹配结果

# 尽量别改，除非你知道是什么意思
debug = False
my_write_num_list = [(7, 10)]  # 经过第一轮测试后笔画的结果， 自己记录下来
true_request = True  # 真实请求测试
# 名字固定要的字
fix_write_word = ''
SELECTED_SANCAI = ['大吉', '中吉']  # 三才中，如果为None就不特意选最好的

# 首先在http://www.qimingzi.net/ 网站提交基本信息，点击开始起名，F12查看请求信息把Cookie复制下来
headers = {"Cookie": "__51cke__=; Hm_lvt_1f1b125fd1b03fdb6cac5abdd0f5d306=1603866097,1603882167; ASP.NET_SessionId=typwis2xwc1cm5kd2iehtskw; __tins__20674741=%7B%22sid%22%3A%201603952255714%2C%20%22vd%22%3A%203%2C%20%22expires%22%3A%201603954232685%7D; 53gid2=10308951834010; visitor_type=new; 53gid0=10308951834010; 53gid1=10308951834010; 53revisit=1603952432864; 53kf_72241622_from_host=www.qimingzi.net; 53kf_72241622_keyword=; 53kf_72241622_land_page=http%253A%252F%252Fwww.qimingzi.net%252FnameReport.aspx%253Fsurname%253D%2525D3%2525DA%2526name%253D%2525D7%2525CE%2525E8%2525F2%2526sex%253D%2525C5%2525AE; kf_72241622_land_page_ok=1; 53uvid=1; onliner_zdfq72241622=0; __tins__5033285=%7B%22sid%22%3A%201603952125189%2C%20%22vd%22%3A%2013%2C%20%22expires%22%3A%201603955633053%7D; __51laig__=19; Hm_lpvt_1f1b125fd1b03fdb6cac5abdd0f5d306=1603953833",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0"}
