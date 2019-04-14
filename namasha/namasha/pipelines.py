from sqlalchemy.orm import sessionmaker
from namasha.models import NamashaDB, db_connect, create_table


class NamashaPipeline(object):

    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        namashadb = NamashaDB()
        namashadb.category = item['category']
        namashadb.title = item['title']
        namashadb.link = item['link']
        namashadb.date_added = item['date_added']
        namashadb.publisher = item['publisher']
        namashadb.publisher_logo = item['publisher_logo']
        namashadb.description = item['description']
        namashadb.view_count = item['view_count']

        try:
            session.add(namashadb)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
        return item