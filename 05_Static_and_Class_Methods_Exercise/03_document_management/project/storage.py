from project.category import Category
from project.topic import Topic
from project.document import Document
from typing import List

class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        c = next((c for c in self.categories if c.id == category_id), None)
        if c is not None:
            c.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        t = next((t for t in self.topics if t.id == topic_id), None)
        if t is not None:
            t.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        d = next((d for d in self.documents if d.id == document_id), None)
        if d is not None:
            d.edit(new_file_name)

    def delete_category(self, category_id):
        c = next((c for c in self.categories if c.id == category_id), None)
        if c is not None:
            self.categories.remove(c)

    def delete_topic(self, topic_id):
        t = next((t for t in self.topics if t.id == topic_id), None)
        if t is not None:
            self.topics.remove(t)

    def delete_document(self, document_id):
        d = next((d for d in self.documents if d.id == document_id), None)
        if d is not None:
            self.documents.remove(d)

    def get_document(self, document_id):
        d = next((d for d in self.documents if d.id == document_id), None)
        if d is not None:
            return d

    def __repr__(self):
        return "\n".join(str(d) for d in self.documents)

