class Site:

    def __init__(self):
        print('init')
        self.username = ''
        self.password = ''

    def log_in(self, username, password):
        print('logging in', username)
        self.username = username
        self.password = password


class Google(Site):

    gmail_url = 'http://mail.google.com'
    calendar_url = 'http://calendar.google.com'

    def query_gmail(self):
        print('querying gmail', self.gmail_url)

    def query_calendar(self):
        print('querying calendar', self.calendar_url)


class Yahoo(Site):

    yahoo_mail_url = 'http://mail.yahoo.com'

    def query_yahoo_mail(self):
        print('querying yahoo mail', self.yahoo_mail_url)


if __name__ == '__main__':

    mosky_g = Google()
    mosky_g.log_in('mosky', 'mypassword')
    mosky_g.query_gmail()
    print(mosky_g.username)
    print()

    andy_y = Yahoo()
    andy_y.log_in('andy', 'andypassword')
    andy_y.query_yahoo_mail()
    print(andy_y.username)
