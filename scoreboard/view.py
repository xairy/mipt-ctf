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

    task_cmp = lambda task: sum([1 for user in users.keys() if users[user][task]])
    sorted_tasks = sorted(tasks.keys(), key=task_cmp, reverse=True)
    print sorted_tasks
    user_cmp = lambda user: sum([1 for task in tasks.keys() if users[user][task]])
    sorted_users = sorted(users.keys(), key=user_cmp, reverse=True)
    print sorted_users

    return render.index(tasks, sorted_tasks, users, sorted_users)

def start_app():
  app = web.application(urls, globals())
  app.run()

if __name__ == "__main__":
  start_app()
