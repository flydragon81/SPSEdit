"""
name
"""
x_file_pattern = '"XPS (*.xps, *.x, *.XPS, *.X )"'
s_file_pattern = '"SPS (*.sps, *.s, *.SPS, *.S )"'
r_file_pattern = '"RPS (*.rps, *.r, *.RPS, *.R )"'
db_file_pattern = '"SQLite (*.sqlite )"'

'''
table config
'''
point_table_content = '''(
                        line real NOT NULL,
                        point real NOT NULL,
                        idx int NOT NULL,
                        easting real NOT NULL,
                        northing real NOT NULL,
                        elevation real NOT NULL,
                        PRIMARY KEY(line, point, idx)'''

table_dict = {'R': point_table_content,
              'S': point_table_content
              }

# SQL_CREATE_TABLE = """ CREATE TABLE IF NOT EXISTS  {}{}
# ); """.format(list(table_dict.keys())[0], table_dict[list(table_dict.keys())[0]])
#
# print(SQL_CREATE_TABLE)
'''
filename：即日志输出的文件名，如果指定了这个信息之后，实际上会启用 FileHandler，而不再是 StreamHandler，这样日志信息便会输出到文件中了。
filemode：这个是指定日志文件的写入方式，有两种形式，一种是 w，一种是 a，分别代表清除后写入和追加写入。
format：指定日志信息的输出格式，即上文示例所示的参数，详细参数可以参考：docs.python.org/3/library/l…，部分参数如下所示：
%(levelno) s：打印日志级别的数值。
%(levelname) s：打印日志级别的名称。
%(pathname) s：打印当前执行程序的路径，其实就是 sys.argv [0]。
%(filename) s：打印当前执行程序名。
%(funcName) s：打印日志的当前函数。
%(lineno) d：打印日志的当前行号。
%(asctime) s：打印日志的时间。
%(thread) d：打印线程 ID。
%(threadName) s：打印线程名称。
%(process) d：打印进程 ID。
%(processName) s：打印线程名称。
%(module) s：打印模块名称。
%(message) s：打印日志信息。
datefmt：指定时间的输出格式。
style：如果 format 参数指定了，这个参数就可以指定格式化时的占位符风格，如 %、{、$ 等。
level：指定日志输出的类别，程序会输出大于等于此级别的信息。
stream：在没有指定 filename 的时候会默认使用 StreamHandler，这时 stream 可以指定初始化的文件流。
handlers：可以指定日志处理时所使用的 Handlers，必须是可迭代的。

Level
首先我们来了解一下输出日志的等级信息，logging 模块共提供了如下等级，每个等级其实都对应了一个数值，列表如下：
等级
数值
CRITICAL
50
FATAL
50
ERROR
40
WARNING
30
WARN
30
INFO
20
DEBUG
10
NOTSET
0
我们设置了输出 level，系统便只会输出 level 数值大于或等于该 level 的的日志结果。
'''