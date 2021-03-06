import os
import time
from subprocess import call, Popen
from flask import Flask, render_template
app = Flask(__name__)

PASSWORD = open('password.txt', 'r')
PASSWORD = PASSWORD.read()

if PASSWORD[-1:] == "\n":
    PASSWORD = PASSWORD[:-1]
 
ROOT_DIR = '.'
GIT_DIR = os.path.join(ROOT_DIR, 'sugar-irc')

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def commit():
    if not os.path.isdir('sugar-irc'):
        call(['git', 'clone', 'https://github.com/SAMdroid-apps/sugar-irc'],
             cwd=ROOT_DIR)

    call(['git', 'pull'], cwd=GIT_DIR)

    Popen(['python', 'sugar-irc-bot.py', PASSWORD],
          cwd=GIT_DIR)
    return 'I think it worked'

if __name__ == '__main__':
    if not os.path.isdir('sugar-irc'):
        call(['git', 'clone', 'https://github.com/SAMdroid-apps/sugar-irc'],
             cwd=ROOT_DIR)

    Popen(['python', 'sugar-irc-bot.py', PASSWORD], cwd=GIT_DIR)
    app.debug = True
    app.run(host="elsalvador.treehouse.su", port=5002)

