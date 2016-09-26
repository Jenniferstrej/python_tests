from session import Session

class ExpandArticle:

    def do_activity(self, data=None):

        try:

            session = Session(self.settings)

            #do something with session

            article_id = 001

            session.store_value(self.get_workflowId(), 'article_id', article_id)

            return True

        except:

            return False



