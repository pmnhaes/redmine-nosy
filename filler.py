# encoding: utf-8
from base64 import b32decode as decode
from base64 import b32encode as encode
from getpass import getpass
from splinter import Browser

class Redmine(object):

    activities_codes = {'Funcionalidade': '36'}

    def __init__(self):
        self.username = raw_input('Digite seu usuário: ')
        self.password = encode(getpass('Digite sua senha: '))
        self.prepare()

    def prepare(self):
        try:
          self.browser = Browser('chrome')
        except:
          self.browser = Browser()
        self.login()

    def login(self):
        self.browser.visit('http://sgsetec.renapi.gov.br/login')
        self.browser.fill('username', self.username)
        self.browser.fill('password', decode(self.password))
        self.browser.find_by_name('login').click()

    def visit_bd(self):
        self.browser.visit('http://sgsetec.renapi.gov.br/kanban?project_id=bd')

    def update_issue(self, issue_id, worked_hours=4, date=None,
                                    activity='Funcionalidade', comment=None):
        self.visit_bd()
        self.browser.visit('http://sgsetec.renapi.gov.br/issues/%s/time_entries/new' % issue_id)
        self.browser.find_by_id('time_entry_hours').fill(worked_hours)
        self.browser.select('Atividade', self.activities_codes[worked_hours])
        #self.browser.find_by_value('Salvar').click()
