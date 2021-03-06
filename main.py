import web
import json
from util import Board
import ast

urls = (
    "/test", "Test",
    "/json_api_template", "JsonApiDemo",
    "/get_random_iteration", "GetRandomIteration",
    "/get_custom_iteration", "GetCustomIteration"
)
app = web.application(urls, globals())


def customhook():
    web.header('Access-Control-Allow-Origin', '*')
    web.header('Access-Control-Allow-Headers','Content-Type, Access-Control-Allow-Origin,'
               'Access-Control-Allow-Headers, X-Requested-By, Access-Control-Allow-Methods')
    web.header('Access-Control-Allow-Methods', 'POST, GET, PUT, DELETE')


# Test whether the web server is running.
class Test:
    def GET(self):
        web.header('Content-Type', 'text')
        return 'The server is running now !'


class JsonApiDemo:
    def GET(self):
        result_dic = {'key_1': ['.', '.', 'O'], 'key_2': 2}
        web.header('Content-Type', 'application/json')
        return json.dumps(result_dic)


class GetRandomIteration:

    def POST(self):
        post_data = web.input()
        print(post_data)
        row_num, col_num = map(int, [post_data.row_num, post_data.col_num])
        try:
            iter_n = int(post_data.iter_n)
        except:
            iter_n = 50
        board = Board(row_num, col_num)
        board.iter_n(iter_n)
        result = {'data': board.history}
        web.header('Content-Type', 'application/json')
        return json.dumps(result)


class GetCustomIteration:
    def POST(self):
        post_data = web.input()
        print(post_data)
        initial_board = post_data.initial_board
        row_num, col_num = map(int, [post_data.row_num, post_data.col_num])
        try:
            iter_n = int(post_data.iter_n)
        except:
            iter_n = 50
        board = Board(row_num, col_num)
        board.status = ast.literal_eval(initial_board)
        board.iter_n(iter_n)
        result = {'data': board.history}
        web.header('Content-Type', 'application/json')
        return json.dumps(result)


if __name__ == "__main__":
    app.add_processor(web.loadhook(customhook))
    app.run()
