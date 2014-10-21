#!/usr/bin/python

from __future__ import print_function, unicode_literals

import json
import sqlite3

def create_db():
  conn = sqlite3.connect('scoreboard.db')
  c = conn.cursor()
  c.execute('DROP TABLE IF EXISTS tasks')
  c.execute('CREATE TABLE tasks (task text, flag text)')
  c.execute('DROP TABLE IF EXISTS users')
  c.execute('CREATE TABLE users (user text, state text)')
  conn.commit()
  conn.close()

def put_tasks(tasks):
  conn = sqlite3.connect('scoreboard.db')
  c = conn.cursor()
  for task, flag in tasks.items():
    c.execute('INSERT INTO tasks VALUES(?, ?)', (task, flag))
  conn.commit()
  conn.close()

def get_tasks():
  conn = sqlite3.connect('scoreboard.db')
  c = conn.cursor()
  c.execute('SELECT * from tasks')
  res = dict(c.fetchall())
  conn.close()
  return res

def get_task_flag(task):
  conn = sqlite3.connect('scoreboard.db')
  c = conn.cursor()
  c.execute('SELECT * from tasks WHERE task = ?', (task,))
  res = c.fetchone()
  conn.close()
  if res == None:
    return None
  return res[1]

def add_user(user):
  conn = sqlite3.connect('scoreboard.db')
  c = conn.cursor()
  tasks = get_tasks()
  for task in tasks.keys():
    tasks[task] = False
  state = json.dumps(tasks)
  c.execute('INSERT INTO users VALUES(?, ?)', (user, state))
  conn.commit()
  conn.close()
  return tasks

def get_users():
  conn = sqlite3.connect('scoreboard.db')
  c = conn.cursor()
  c.execute('SELECT * from users')
  res = dict(c.fetchall())
  for user in res.keys():
    res[user] = json.loads(res[user])
  conn.close()
  return res

def get_user_state(user):
  conn = sqlite3.connect('scoreboard.db')
  c = conn.cursor()
  c.execute('SELECT * FROM users WHERE user = ?', (user,))
  res = c.fetchone()
  conn.close()
  if res == None:
    return None
  res = json.loads(res[1])
  return res

def set_user_state(user, state):
  conn = sqlite3.connect('scoreboard.db')
  c = conn.cursor()
  state = json.dumps(state)
  c.execute('UPDATE users SET state = ? WHERE user = ?', (state, user))
  conn.commit()
  conn.close()

def try_solve_task(user, task, flag):
  correct_flag = get_task_flag(task)
  if correct_flag == None:
    return 'No such task!'
  if flag != correct_flag:
    return 'Bad flag!'
  state = get_user_state(user)
  if state == None:
    state = add_user(user)
  state[task] = True
  set_user_state(user, state)
  return 'Correct!'

if __name__ == '__main__':
  create_db()
  put_tasks({'a': '01', 'b': '02'})
  print(get_tasks())
  print(add_user('xairy'))
  print(get_task_flag('a'))
  print(get_user_state('xairy'))
  print(try_solve_task('xairy', 'a', '10'))
  print(try_solve_task('xairy', 'b', '02'))
  print(get_user_state('xairy'))
  print(get_users())
