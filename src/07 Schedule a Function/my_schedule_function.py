import time

def schedule_function(t, f, *args):
  print(f'{f}() scheduled to run at {t}')
  return


schedule_function(time.time() + 1, print, 'Howdy!')

