
import web
import uuid
import dbconnector

urls = (
    '/getRaw', 'getRaw',
    '/postRaw', 'postRaw'
)
app = web.application(urls, globals())

class getRaw:
    def GET(self, ):
        key  = web.input(_method='get').get('key', '')
        if not key:
            return ''
        res = dbconnector.getKey(key)
        return res

class postRaw:
    def POST(self, ):
        rawdata = web.input(_method='post').get('rawdata', '')
        rawdata = str(rawdata)
        guid1 = str(uuid.uuid4())
        dbconnector.saveKey(guid1, rawdata)
        return guid1


if __name__ == "__main__":
    app.run()