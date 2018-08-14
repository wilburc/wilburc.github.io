import re
import urllib.parse

from wsgiref.simple_server import make_server

answers = {
  'Ping':'OK',
  'Resume':'wilburchen.com/files/wilbur_chen_resume.pdf',
  'Name':'Wilbur Chen',
  'Referrer':'LinkedIn',
  'Phone':'6508080573',
  'Email Address':'wilburchen1@gmail.com',
  'Puzzle':'a',
  'Degree':'B.S. in Informatics: Human-computer Interaction',
  'Position':'Data Scientist/Engineer',
  'Years':'3',
  'Source':'aws link',
  'Status':'Yes'
}

def application(environ, start_response):
    path    = environ['PATH_INFO']
    method  = environ['REQUEST_METHOD']
    msg_query = environ['QUERY_STRING']
    if msg_query:
      question = re.match('q=(.*?)&d',msg_query)
      question = question.group(1)
      question = re.sub('[^0-9a-zA-Z]+', ' ', question)
    if question in answers:
        if question == 'Puzzle':
          puzzle = urllib.parse.unquote(msg_query)
          puzzle = (puzzle.splitlines())[-4:]
          # response = solve_puzzle(puzzle)
          response = solve_puzzle(puzzle)
        else:
          response = answers[question]
    else:
        response = ''
    status = '200 OK'
    headers = [('Content-type', 'text/html')]

    start_response(status, headers)
    return [response]

def solve_puzzle(puzzle):
    letters = ['A','B','C','D']
    board = {}
    for p in puzzle:
        letter = p[0]
        rules = p[1:5]
        board[letter] = {letters[i]:rules[i] for i,j  in enumerate(letters)}
    results = {letter:i for i,letter in enumerate(letters)}
    for i,j in board.items():
        for k,l in j.items():
            if l == '>':
                v1 = results[i]
                v2 = results[k]
                if v1 < v2:
                    results[i] = v2+1
            elif l == '<':
                v1 = results[i]
                v2 = results[k]
                if v1 > v2:
                    results[i] = v2-1
    for i,j in board.items():
        v1 = results[i]
        for k,l in j.items():
            v2 = results[k]
            if v1 > v2:
                board[i][k] = '>'
            elif v1 < v2:
                board[i][k] = '<'
            else:
                board[i][k] = '='
    ans = ' ABCD\n'
    for i,j in board.items():
        ans += (i + ''.join([j for i,j in j.items()]) + '\n')
    return ans

if __name__ == '__main__':
    httpd = make_server('', 8000, application)
    print("Serving on port 8000...")
    httpd.serve_forever()
