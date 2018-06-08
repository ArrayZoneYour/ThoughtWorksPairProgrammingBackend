import web
import json

urls = (
    "/test", "Test",
    "/json_api_template", "JsonApiDemo"
)
app = web.application(urls, globals())


# Test whether the web server is running.
class Test:
    def GET(self):
        return 'The server is running now !'


class JsonApiDemo:
    def GET(self):
        result_dic = {'key_1': ['.', '.', 'O'], 'key_2': 2}
        web.header('Content-Type', 'application/json')
        return json.dumps(result_dic)


if __name__ == "__main__":
    app.run()
