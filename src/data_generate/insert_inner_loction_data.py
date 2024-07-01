import mysql.connector
from mysql.connector import Error

# 你的200组数据
data = [
("景点1", "景点", 39.9635, 116.3499,91),
("教学楼1", "教学楼", 39.9631, 116.3500,90),
("办公楼1", "办公楼", 39.9631, 116.3493,90),
("宿舍楼1", "宿舍楼",39.9628, 116.3500,90),
("商店1", "商店", 39.9628, 116.3493,90),
("饭店1", "饭店", 39.9625, 116.3492,90),
("洗手间1", "洗手间",39.9624, 116.3492,98),
("图书馆1", "图书馆", 39.9624, 116.3500,95),
("食堂1", "食堂", 39.9619, 116.3493,90),
("超市1", "超市", 39.9619, 116.3501,90),
("咖啡馆1", "咖啡馆", 39.9609, 116.3493,90),
("浴室1", "浴室", 39.9609, 116.3501,90),
("甜品店1", "甜品店", 39.9603, 116.3493,90),
("教学楼2", "教学楼", 39.9598, 116.3494,90),
("办公楼2", "办公楼", 39.9598, 116.3490,90),
("宿舍楼2", "宿舍楼",39.9593, 116.3494,90),
("文创店1", "文创店", 39.9593, 116.3511,90),
("饭店2", "饭店", 39.9603, 116.3511,90),
("洗手间2", "洗手间",39.9609, 116.3510,90),
("图书馆2", "图书馆", 39.9619, 116.3510,90),
("食堂2", "食堂", 39.9614, 116.3510,90),
("超市2", "超市", 39.9614, 116.3511,90),
("景点2", "景点", 39.9624, 116.3510,90),
("咖啡馆2", "咖啡馆", 39.9628, 116.3509,90),
("浴室2", "浴室", 39.9630, 116.3509,90),
("甜品店2", "甜品店", 39.9635, 116.3509,90),
("食堂3", "食堂", 39.9630, 116.3517,90),
("饭店3", "饭店", 39.9635, 116.3517,90),
("宿舍楼3", "宿舍楼",39.9630, 116.3519,90),
("图书馆3", "图书馆", 39.9628, 116.3519,90),
("洗手间3", "洗手间",39.9630, 116.3524,90),
("超市3", "超市", 39.9631, 116.3524,90),
("教学楼3", "教学楼", 39.9633, 116.3524,90),
("文创店2", "文创店", 39.9632, 116.3532,90),
("商店2", "商店", 39.9634, 116.3531,90),
("咖啡馆3", "咖啡馆", 39.9632, 116.3535,90),
("图书馆4", "图书馆", 39.9632, 116.3541,90),
("办公楼3", "办公楼", 39.9634, 116.3546,90),
("浴室3", "浴室", 39.9636, 116.3546,90),
("甜品店3", "甜品店", 39.9632, 116.3546,90),
("饭店4", "饭店", 39.9628, 116.3546,90),
("文创店3", "文创店", 39.9628, 116.3541,90),
("searc","彩蛋",39.9624, 116.3541,90),
("商店3", "商店", 39.9624, 116.3546,90),
("教学楼4", "教学楼", 39.9621, 116.3541,90),
("图书馆5", "图书馆", 39.9621, 116.3546,90),
("洗手间4", "洗手间",39.9623, 116.3535,90),
("食堂4", "食堂", 39.9616, 116.3536,90),
("宿舍楼4", "宿舍楼",39.9616, 116.3542,90),
("超市4", "超市", 39.9617, 116.3547,90),
("办公楼4", "办公楼", 39.9610, 116.3542,90),
("景点3", "景点", 39.9610, 116.3547,90),
("咖啡馆4", "咖啡馆", 39.9616, 116.3525,90),
("浴室4", "浴室", 39.9620, 116.3525,90),
("图书馆6", "图书馆", 39.9610, 116.3525,90),
("饭店5", "饭店", 39.9610, 116.3531,90),
("文创店4", "文创店", 39.9624, 116.3524,90),
("商店4", "商店", 39.9623, 116.3525,90),
("宿舍楼5", "宿舍楼",39.9601, 116.3547,90),
("景点4", "景点", 39.9601, 116.3543,90),
("文创店5", "文创店", 39.9603, 116.3543,90),
("食堂5", "食堂", 39.9603, 116.3531,90),
("洗手间5", "洗手间",39.9604, 116.3531,90),
("浴室5", "浴室", 39.9604, 116.3525,90),
("教学楼5", "教学楼", 39.9594, 116.3525,90),
("咖啡馆5", "咖啡馆", 39.9594, 116.3532,90),
("超市5", "超市", 39.9588, 116.3532,90),
("图书馆7", "图书馆", 39.9588, 116.3525,90),
("景点5", "景点", 39.9588, 116.3511,90),
("甜品店4", "甜品店", 39.9584, 116.3512,90),
("文创店6", "文创店", 39.9587, 116.3494,90),
("饭店6", "饭店", 39.9584, 116.3502,90),
("商店5", "商店", 39.9584, 116.3494,90),
("办公楼5", "办公楼", 39.9581, 116.3494,90),
("浴室6", "浴室", 39.9581, 116.3502,90),
("超市6", "超市", 39.9578, 116.3502,90),
("洗手间6", "洗手间",39.9578, 116.3494,90),
("咖啡馆6", "咖啡馆", 39.9573, 116.3494,90),
("文创店7", "文创店", 39.9570, 116.3494,90),
("甜品店5", "甜品店", 39.9573, 116.3503,90),
("食堂6", "食堂", 39.9571, 116.3503,90),
("饭店7", "饭店", 39.9571, 116.3512,90),
("商店6", "商店", 39.9575, 116.3512,90),
("教学楼6", "教学楼", 39.9571, 116.3518,90),
("文创店8", "文创店", 39.9570, 116.3518,90),
("浴室7", "浴室", 39.9568, 116.3518,90),
("甜品店8", "甜品店", 39.9570, 116.3527,94),
("洗手间7", "洗手间",39.9571, 116.3527,90),
("宿舍楼6", "宿舍楼",39.9571, 116.3525,90),
("咖啡馆7", "咖啡馆", 39.9571, 116.3531,92),
("甜品店6", "甜品店", 39.9575, 116.3525,100),
("超市7", "超市", 39.9576, 116.3536,90),
("图书馆8", "图书馆", 39.9573, 116.3531,80),
("景点6", "景点", 39.9573, 116.3537,90),
("食堂7", "食堂", 39.9571, 116.3537,90),
("甜品店7", "甜品店", 39.9579, 116.3525,70),
("饭店8", "饭店", 39.9579, 116.3533,90),
("浴室8", "浴室", 39.9580, 116.3525,90),
("咖啡馆8", "咖啡馆", 39.9580, 116.3512,90),
("商店7", "商店", 39.9584, 116.3525,90),
("办公楼6", "办公楼", 39.9584, 116.3534,90),
("超市8", "超市", 39.9581, 116.3534,91),
("洗手间8", "洗手间",39.9584, 116.3548,92),
("食堂8", "食堂", 39.9581, 116.3546,93),
("商店8", "商店", 39.9573, 116.3546,94),
]

try:
    # 连接到数据库
    connection = mysql.connector.connect(
        host='localhost',          # 替换为你的主机地址
        database='tour_system',    # 替换为你的数据库名称
        user='root',                # 替换为你的数据库用户名
        password='123456'         # 替换为你的数据库密码
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # 插入数据的SQL语句
        sql_insert_query = """INSERT IGNORE INTO innerlocations (name, type, latitude, longitude, popularity)
                              VALUES (%s, %s, %s, %s, %s)"""
        
        # 批量插入数据
        cursor.executemany(sql_insert_query, data)
        connection.commit()
        print(cursor.rowcount, "rows were inserted successfully.")

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")