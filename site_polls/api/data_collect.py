from jira import JIRA

auth_jira = JIRA(options={'server': 'https://jiraps.atlassian.net/'}, basic_auth=('rocarmo@uolinc.com', 'whSXrKnCX64Iei3rH4DO7136'))

print(auth_jira)

issues_in_project = auth_jira.search_issues("project = 'PS - San Fierro' AND assignee = currentUser()")

for issue in issues_in_project:
    # print('-------------------------')
    # print("Card: ", issue)
    card_issue = issue

    issue_coments = auth_jira.comments(issue)

    # print('Comentários: ', len(issue_coments))
    comments_qty = len(issue_coments)

    for issue_coment in issue_coments:
        # print('Autor do comentário: ', issue_coment.author.displayName)
        comments_author = issue_coment.author.displayName

        # print('Data de criação: ', issue_coment.created)
        comments_date = issue_coment.created


# comment = auth_jira.comment('FIER-251', '3128695')
#
# print(comment)
