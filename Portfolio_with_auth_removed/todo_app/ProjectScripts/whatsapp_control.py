import os
from twilio.rest import Client
from django.contrib.sessions.backends.db import SessionStore

from_whatsapp_number = 'whatsapp:+14155238886'
def sessionkey():
    sessionstore = SessionStore
    print(sessionstore.session_key)
    return sessionstore
def to_whatsapp_number(number):
    print("number:",number)
    if number.startswith('07'):
        number = number.replace('0', 'whatsapp:+44', 1)
    return number


def twilio_auth():
    account_sid = 'AC8bcdbb25058b8907584f03589ae38f43'
    auth_token = '6f877febd28f2ddf321b7e2b7c15d236'
    client = Client(account_sid, auth_token)
    return client

def send_mssg(body, mobile_number):
    client = twilio_auth()
    client.messages.create(body=body,
                           from_=from_whatsapp_number,
                           to=mobile_number)

def is_in_session(request):
    if 'mobnum' in request.session.keys():
        mobile_number = request.session['mobnum']
        return mobile_number

class WACom():
    commands = ["Add:", "Remove:", "Update:", "Show:"]
    def __init__(self, sms_Json, todo_list, mobile_number):
        self.sms_Json = sms_Json
        self.todo_list = todo_list
        self.mobile_number = mobile_number

    def add_Com(self):
        sms_Json = self.sms_Json
        commands = self.commands
        todo_list = self.todo_list
        body = sms_Json["list_item"]
        mobile_number = self.mobile_number
        add_todo = body.replace(commands[0], '').strip()
        if not any(todo_dict['list_item'] == add_todo for todo_dict in todo_list):
            sms_Json["list_item"] = add_todo
            return sms_Json
        else:
            return send_mssg("Item already exists", mobile_number)

    def show_Com(self):
        sms_Json = self.sms_Json
        commands = self.commands
        todo_list = self.todo_list
        mobile_number = self.mobile_number
        if len(todo_list) > 0:
            spacer = '\n'
            list_maker = [tododict['list_item'] for tododict in todo_list]
            print(list_maker)
            sms_list = spacer.join(list_maker)
            send_mssg(f"Items for you todo:\n{sms_list}", mobile_number)
        else:
            send_mssg(f"There is nothing to do. Maybe add something? Type {commands[0]} followed by what you want to add", mobile_number)

    def remove_Com(self):
        sms_Json = self.sms_Json
        commands = self.commands
        todo_list = self.todo_list
        body = sms_Json["list_item"]
        mobile_number = self.mobile_number
        if len(todo_list) > 0:
            todo_item = body.replace(commands[1], '').strip()
            return (todo_item)
        else:
            send_mssg("There's nothing to delete.", mobile_number)

    def update_Com(self):
        sms_Json = self.sms_Json
        commands = self.commands
        todo_list = self.todo_list
        body = sms_Json["list_item"]
        mobile_number = self.mobile_number
        update_todo = body.replace(commands[2], '').strip().split("/")
        if any(todo_dict['list_item'] == update_todo[0] for todo_dict in todo_list):
            sms_Json['list_item'] = update_todo[1]
            return update_todo[0], sms_Json
        else:
            send_mssg("There are no matching items in your todo list. try adding some.", mobile_number)

