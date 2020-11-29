import shutil
import sys

shutil.copyfile('person.json', 'test_dir/person.json')

shutil.rmtree('test_dir')

sys.stdin  # standard input
sys.stdout  # standard output
sys.stderr  # standard error output

sys.exit(5)
