from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with  # rest api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)  # binding the app inside the api
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
db=SQLAlchemy(app)

class ViewModel(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100))
    views=db.Column(db.Integer)
    likes=db.Column(db.Integer)

# db.create_all()

video_put_args = reqparse.RequestParser()  # to parse the request we are sending
video_put_args.add_argument(
    'name', type=str, help="name of the video", location='form')
video_put_args.add_argument(
    'likes', type=int, help="Likes on the video", location='form')
video_put_args.add_argument(
    'views', type=int, help="view of the video", location='form')

resource_fields={
    'id':fields.Integer,
    'name':fields.String,
    'likes':fields.Integer,
    'views':fields.Integer
}

videos = {}
names = {'jess': {'age': 10, 'gender': 'female'},
         'bill': {'age': 56, 'gender': 'male'}}

# get,post,put,patch,delete


def abort_video_not_exists(video_id):
    if video_id not in videos:
        abort(404, message='Not found')


def abort_if_exists(video_id):
    if video_id in videos:
        abort(404, message='already added')


class HelloWorld(Resource):
    def get(self, name):  # get method from Resource class, here it is overriding
        # necessary to return dict or string, no other type
        return names[name]

    def post(self):  # post method
        return {'data': 'postrequest'}


class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        # abort_video_not_exists(video_id)
        result=ViewModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404,message='Not found')
        return result

    @marshal_with(resource_fields)
    def put(self, video_id):
        # abort_if_exists(video_id)
        args = video_put_args.parse_args()
        video= ViewModel(name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        # videos[video_id] = args
        return video

    def delete(self,video_id):
        abort_video_not_exists(video_id)
        del videos[video_id]
        return '',204

api.add_resource(Video, '/video/<int:video_id>')

# multiple endpoints
# api.add_resource(HelloWorld,'/helloworld', '/world') # making it accessible to others, helloworld is the endpoint
# passing data to the get request
api.add_resource(HelloWorld, '/helloworld/<string:name>')


# print(videos)
if __name__ == '__main__':
    app.run(debug=True)
