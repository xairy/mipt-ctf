#!/usr/bin/python

import web

import db

urls = (
  '/', 'index'
)

render = web.template.render('templates')

class index:
  def GET(self):
    tasks = db.get_tasks()
    users = db.get_users()

    task_cmp = lambda task_name: tasks[task_name]['complexity']
    sorted_tasks = sorted(tasks.keys(), key=task_cmp, reverse=False)
    print sorted_tasks
    user_cmp = lambda user_name: sum([1 for task_name in tasks.keys() if users[user_name][task_name]])
    sorted_users = sorted(users.keys(), key=user_cmp, reverse=True)
    print sorted_users

    return render.index(tasks, sorted_tasks, users, sorted_users)

app = web.application(urls, globals())
wsgiapp = app.wsgifunc()

def start_app():
  app.run()

if __name__ == "__main__":
  start_app()
