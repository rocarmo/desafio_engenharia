from jira import JIRA


class DataCollect:

    def __init__(self, text1, text2):
        self.text1 = text1
        self.text2 = text2


    # def get_data(self):
    #     auth_jira = JIRA(options={'server': 'https://jiraps.atlassian.net/'},
    #                      basic_auth=('rocarmo@uolinc.com', 'whSXrKnCX64Iei3rH4DO7136'))
    #
    #     print(auth_jira)
    #
    #     issues_in_project = auth_jira.search_issues("project = 'PS - San Fierro' AND assignee = currentUser()")
    #
    #     for issue in issues_in_project:
    #         # print('-------------------------')
    #         # print("Card: ", issue)
    #         self.card_issue = issue
    #
    #         self.issue_coments = auth_jira.comments(issue)
    #
    #         # print('Comentários: ', len(issue_coments))
    #         self.comments_qty = len(self.issue_coments)
    #
    #         for issue_coment in self.issue_coments:
    #             # print('Autor do comentário: ', issue_coment.author.displayName)
    #             self.comments_author = issue_coment.author.displayName
    #
    #             # print('Data de criação: ', issue_coment.created)
    #             self.comments_date = issue_coment.created
    #
    #     # return self.comments_date, self.comments_author, self.comments_qty

