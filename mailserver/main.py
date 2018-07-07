from mailserver.inbox import Inbox
import email
from userstuff import do_stuff

inbox = Inbox()

@inbox.collate
def handle(to, sender, subject, body):
    b = email.message_from_string(body)
    do_stuff(b)
def main():
    inbox.dispatch()
if __name__ == '__main__':
    main()

