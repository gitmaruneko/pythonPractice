class Google:

    gmail_url = 'http://mail.google.com'
    calendar_url = 'http://calendar.google.com'

    def __init__(self):
        print('init')
        self.username = ''
        self.password = ''

    def log_in(self, username, password):
        print('logging in', username)
        self.username = username
        self.password = password

    def query_gmail(self):
        print('querying gmail', self.gmail_url)

    def query_calendar(self):
        print('querying calendar', self.calendar_url)


if __name__ == '__main__':

    print(Google.gmail_url)
    print(Google.calendar_url)
    print()

    mosky_g = Google()
    mosky_g.log_in('mosky', 'mypassword')
    mosky_g.query_gmail()
    print(mosky_g.username)
    print()

    andy_g = Google()
    andy_g.log_in('andy', 'andypassword')
    andy_g.query_gmail()
    print(andy_g.username)
