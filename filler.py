# encoding: utf-8
from base64 import b32decode as decode
from base64 import b32encode as encode
from getpass import getpass
from splinter.browser import Browser
import datetime

class Redmine(object):

    activities_codes = {'Funcionalidade': '36', 'Codificacao': '25'}
    type_codes = {'Funcionalidade': '2', 'Codificacao': '7', 'Refatoramento': '14'}
    participants_code = {'59':'Douglas Camata',
                        '65': 'Felipe Norato Lacerda',
                        '60': 'Fernando Carvalho',
                        '149': 'Fábio Ribeiro',
                        '68': 'Priscila Manhaes da Silva',
                        '32': 'Rogério Atem'}

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

    def visit_project(self, project_id):
        self.browser.visit('http://sgsetec.renapi.gov.br/kanban?project_id=%s' % project_id)

    def create_issue(self, project_id, type_name, title, description, begin, end, participants,
                        monitors):

        self.browser.visit('http://sgsetec.renapi.gov.br/projects/%s/issues/new' % project_id)
        self.browser.select('Tipo', self.type_codes[type_name])
        self.browser.fill('issue[subject]', title)
        self.browser.fill('issue[description]', description)
        self.browser.fill('issue[start_date]', begin)
        self.browser.fill('issue[due_date]', end)
        for participant in participants:
            self.browser.select('Participantes', self.participants_code[participant])
        for monitor in monitors:
            self.browser.select('Monitores', self.participants_code[monitor])
        self.browser.find_by_value('Criar').click()

    def update_issue(self, issue_id, activity, date,
                                    worked_hours=4, comment=None):
        self.browser.visit('http://sgsetec.renapi.gov.br/issues/%s/time_entries/new' % issue_id)
        self.browser.find_by_id('time_entry_hours').fill(worked_hours)
        self.browser.select('Atividade', self.activities_codes[activity.capitalize()])
        self.browser.find_by_value('Salvar').click()

    def finish_issue(self, issue_id, begin, total_days, activity):
        #do not need to plus um day into cause first day of work is 'begin'
        for day_worked in xrange(total_days):
            date = str(datetime.datetime.strptime(entrada, "%Y/%m/%d") + 
                        datetime.timedelta(day_worked))
            self.update_issue(issue_id=issue_id, date=date, activity=activity)
