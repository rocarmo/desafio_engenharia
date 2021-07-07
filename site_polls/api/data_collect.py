from jira import JIRA


class DataImport:
    def __init__(self):
        # self.comments_qty = DataCollect.get_comments_qty
        # self.comments_author = DataCollect.get_comments_author
        # self.comments_date = DataCollect.get_comments_date
        pass

class DataCollect:
    def __init__(self):
        self.auth_jira = JIRA(options={'server': 'https://jiraps.atlassian.net/'},
                              basic_auth=('rocarmo@uolinc.com', 'whSXrKnCX64Iei3rH4DO7136'))
        self.issues_in_project = self.auth_jira.search_issues("project = 'PS - San Fierro' AND assignee = currentUser()")


    def get_data(self):

        for issue in self.issues_in_project:
            self.issue_comments = self.auth_jira.comments(issue)

    def get_comments_qty(self):
        comments_qty = 12121212
        # comments_qty = len(self.issue_comments)
        return comments_qty

    def get_comments_author(self):
        # for issue_comment in self.issue_comments:
        #     comments_author = issue_comment.author.displayName

        comments_author = 'RODRIGOIDE PICA DAS GALAXIAS MANE'

        return comments_author

    def get_comments_date(self):

        # for issue_comment_date in self.issue_comments:
        #     comments_date = issue_comment_date.created

        comments_date = '19/08/1997'
        return comments_date
