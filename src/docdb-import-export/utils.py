
# Confirm yes or not to continue.
def confirm(prompt=None, resp=False):
  if prompt is None:
    prompt = "Are you sure you want to continue? [y/N]: "

  while True:
    ans = input(prompt).strip()
    if not ans:
      return resp
    if ans not in ['y', 'Y', 'n', 'N']:
      print('please enter y or n.' + '\n')
      continue
    if ans == 'y' or ans == 'Y':
      return True
    if ans == 'n' or ans == 'N':
      return False
