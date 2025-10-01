import os
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime

# 加载MongoDB连接字符串
load_dotenv(os.path.join(os.path.dirname(__file__), 'token.env'))
MONGO_URI = os.getenv('MONGO_URI')

client = MongoClient(MONGO_URI)
db = client['note_app']
notes_collection = db['notes']

class Note:
    def __init__(self, title, content, created_at=None, updated_at=None, _id=None):
        self.id = str(_id) if _id else None
        self.title = title
        self.content = content
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    @staticmethod
    def from_dict(data):
        return Note(
            title=data.get('title'),
            content=data.get('content'),
            created_at=data.get('created_at', datetime.utcnow()),
            updated_at=data.get('updated_at', datetime.utcnow()),
            _id=data.get('_id')
        )
