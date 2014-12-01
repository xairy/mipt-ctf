#!/usr/bin/python

from __future__ import print_function, unicode_literals

import json
import sqlite3

def create_db():
  conn = sqlite3.connect('scoreboard.db')
  c = conn.cursor()
  c.execute('DROP TABLE IF EXISTS tasks')
  c.execute('CREATE TABLE tasks (name TEXT, flag TEXT, complexity INTEGER)')
  c.execute('DROP TABLE IF EXISTS users')
  c.execute('CREATE TABLE users (name TEXT, state TEXT)')
  conn.commit()
  conn.close()

def put_tasks(tasks):
  conn = sqlite3.connect('scoreboard.db')
  c = conn.cursor()
  for name in tasks.keys():
    c.execute('INSERT INTO tasks VALUES(?, ?, ?)',
        (name, tasks[name]['flag'], tasks[name]['complexity']))
  conn.commit()
  conn.close()

def get_tasks():
  conn = sqlite3.connect('scoreboard.db')
  c = conn.cursor()
  c.execute('SELECT * from tasks')
  raw_tasks = c.fetchall()
  tasks = {}
  for raw_task in raw_tasks:
    tasks[raw_task[0]] = {'flag': raw_task[1], 'complexity': raw_task[2]}
  conn.close()
  return tasks

def get_task_flag(name):
  conn = sqlite3.connect('scoreboard.db')
  c = conn.cursor()
  c.execute('SELECT * from tasks WHERE name = ?', (name,))
  res = c.fetchone()
  conn.close()
  if res == None:
    return None
  return res[1]

def add_user(name):
  conn = sqlite3.connect('scoreboard.db')
  c = conn.cursor()
  tasks = get_tasks()
  user_tasks = {}
  for task_name in tasks.keys():
    user_tasks[task_name] = False
  state = json.dumps(user_tasks)
  c.execute('INSERT INTO users VALUES(?, ?)', (name, state))
  conn.commit()
  conn.close()
  return user_tasks

def get_users():
  conn = sqlite3.connect('scoreboard.db')
  c = conn.cursor()
  c.execute('SELECT * from users')
  raw_users = c.fetchmany(100)
  users = {}
  for raw_user in raw_users:
    users[raw_user[0]] = json.loads(raw_user[1])
  conn.close()
  return users

def get_user_state(name):
  conn = sqlite3.connect('scoreboard.db')
  c = conn.cursor()
  c.execute('SELECT * FROM users WHERE name = ?', (name,))
  raw_user = c.fetchone()
  conn.close()
  if raw_user == None:
    return None
  state = json.loads(raw_user[1])
  return state

def set_user_state(name, state):
  conn = sqlite3.connect('scoreboard.db')
  c = conn.cursor()
  state = json.dumps(state)
  c.execute('UPDATE users SET state = ? WHERE name = ?', (state, name))
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
  put_tasks({'a': {'flag': '01', 'complexity': 1}, 'b': {'flag': '02', 'complexity': 2}})
  print(get_tasks())
  print(get_task_flag('a'))
  print(add_user('xairy'))
  print(get_users())
  print(get_user_state('xairy'))
  print(try_solve_task('xairy', 'a', '10'))
  print(try_solve_task('xairy', 'b', '02'))
  print(get_user_state('xairy'))
