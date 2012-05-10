Redmine Nosy
========
 It's an automatic tool for filling redmine issues

Python dependencies
~~~~~~~~~~~~~~~~~~~
Run::

    pip install splinter


Using it
~~~~~~~~

Informing day worked::

# worked_hours is 4 for default
# update_issue(issue_id, activity, date, worked_hours=4, comment=None)
>>> redmine = Redmine()
>>> Digite seu usuário: fulano
>>> Digite sua senha:
>>> redmine.update_issue(4563, 'Funcionalidade', '2012-05-10')


Closing issue informing how long it tooks::

# finish_issue(issue_id, begin, total_days, activity):
>>> redmine = Redmine()
>>> Digite seu usuário: fulano
>>> Digite sua senha:
>>> redmine.finish_issue(4563,'2012-05-07', 4, 'Funcionalidade')


Only closing issue::
# close_issue(issue_id)
>>> redmine = Redmine()
>>> Digite seu usuário: fulano
>>> Digite sua senha:
>>> redmine.close_issue(4563)


create_issue still in tests

