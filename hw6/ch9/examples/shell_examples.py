>>> pwd
'/Users/haleyharris/Desktop/belhavencsc/csc221/hw6/ch9/examples'
>>> from pathlib import Path
>>> Path('spam', 'bacon', 'eggs')
PosixPath('spam/bacon/eggs')
>>> ls
>>> my_files = ['accounts.txt']
>>> for filename in my_files:
...     print(Path(r'/Users/haleyharris/Desktop/belhavencsc/csc221/hw6/ch9/examples', filename))
...
>>> my_files = ['accounts.txt', 'details.csv', 'invite.docx']
>>> for filename in my_files:
...     print(Path(r'/Users/haleyharris/Desktop/belhavencsc/csc221/hw6/ch9/examples', filename))
...
>>> Path('spam')/Path('bacon'/'eggs')
>>> Path('spam') / Path('bacon'/'eggs')
>>> Path('spam') / Path('bacon' / 'eggs')
>>> str(Path('spam') / Path('bacon' / 'eggs'))
>>> parent_folder = '~/Desktop/belhavencsc/csc221'
>>> sub_folder = 'spam'
>>> parent_folder + '/' + sub_folder
'~/Desktop/belhavencsc/csc221/spam'
>>> '/'.join([parent_folder, sub_folder])
'~/Desktop/belhavencsc/csc221/spam'
>>> parent_folder / sub_folder
>>> str(parent_folder / sub_folder)
>>> parent_folder = Path('~/Desktop/belhavencsc/csc221/hw6/')
>>> sub_folder = Path('spam')
>>> str(parent_folder / sub_folder)
'~/Desktop/belhavencsc/csc221/hw6/spam'
>>> Path.cwd()
PosixPath('/Users/haleyharris/Desktop/belhavencsc/csc221/hw6/ch9/examples')
>>> Path.home()
PosixPath('/Users/haleyharris')
>>> os.makedirs('~/Desktop/belhavencsc/csc221/hw6/ch9/examples/delicious/walnut/waffles')
>>> import os
>>> os.makedirs('~/Desktop/belhavencsc/csc221/hw6/ch9/examples/delicious/walnut/waffles')
>>> ls
>>> Path.cwd()
PosixPath('/Users/haleyharris/Desktop/belhavencsc/csc221/hw6/ch9/examples')
>>> Path.cwd().is_absolute()
True
>>> Path('spam/bacon/eggs').is_absolute()
False
>>> Path('my/relative/path')
PosixPath('my/relative/path')
>>> Path.cwd
<bound method Path.cwd of <class 'pathlib.Path'>>
>>> Path.cwd()
PosixPath('/Users/haleyharris/Desktop/belhavencsc/csc221/hw6/ch9/examples')
>>> Path.cwd()/Path('my/relative/path')
PosixPath('/Users/haleyharris/Desktop/belhavencsc/csc221/hw6/ch9/examples/my/relative/path')
>>> os.path.abspath('.')
'/Users/haleyharris/Desktop/belhavencsc/csc221/hw6/ch9/examples'
>>> os.path.abspath('./Scripts')
'/Users/haleyharris/Desktop/belhavencsc/csc221/hw6/ch9/examples/Scripts'
>>> os.path.isabs('.')
False
>>> os.path.isabs(os.path.abspath('.'))
True
>>> os.path.relpath('/Users/haleyharris', '/Users')
'haleyharris'
>>> os.path.relpath('/Users/haleyharris', '/Users/spam/eggs')
'../../haleyharris'
>>> p = Path('/Users/haleyharris/spam.txt')
>>> p.anchor
'/'
>>> p.parent
PosixPath('/Users/haleyharris')
>>> p.name
'spam.txt'
>>> p.stem
'spam'
>>> p.suffix
'.txt'
>>> p.drive
''
>>> Path.cwd()
PosixPath('/Users/haleyharris/Desktop/belhavencsc/csc221/hw6/ch9/examples')
>>> Path.cwd().parents[0]
PosixPath('/Users/haleyharris/Desktop/belhavencsc/csc221/hw6/ch9')
>>> Path.cwd().parents[1]
PosixPath('/Users/haleyharris/Desktop/belhavencsc/csc221/hw6')
>>> Path.cwd().parents[2]
PosixPath('/Users/haleyharris/Desktop/belhavencsc/csc221')
>>> Path.cwd().parents[3]
PosixPath('/Users/haleyharris/Desktop/belhavencsc')
>>> Path.cwd().parents[4]
PosixPath('/Users/haleyharris/Desktop')
>>> Path.cwd().parents[5]
PosixPath('/Users/haleyharris')
>>> Path.cwd().parents[6]
PosixPath('/Users')
>>> Path.cwd().parents[7]
PosixPath('/')
>>> calc_filepath = '/Users/haleyharris/Documents/calc.exe'
>>> os.path.basename(calc_filepath)
'calc.exe'
>>> os.path.dirname(calc_filepath)
'/Users/haleyharris/Documents'
>>> os.path.split(calc_filepath)
('/Users/haleyharris/Documents', 'calc.exe')
>>> os.path.dirname(calc_filepath), os.path.basename(calc_filepath)
('/Users/haleyharris/Documents', 'calc.exe')
>>> calc_filepath.split(os.sep)
['', 'Users', 'haleyharris', 'Documents', 'calc.exe']
>>> os.path.getsize('/Users/haleyharris/Documents/calc.exe')
>>> os.path.getsize('/Users/haleyharris/Documents/belhavencs')
384
>>> os.listdir('/Users/haleyharris/Documents/belhavencs')
['csc121',
 'csc111',
 '.DS_Store',
 'csc211',
 'README.md',
 '.gitignore',
 'csc311',
 'csc411',
 '.git',
 'csc421']
>>> total_size = 0
>>> for filename in os.listdir('/Users/haleyharris/Documents/belhavencs'):
...     total_size = total_size + os.path.getsize(os.path.join('/Users/haleyharris/Documents/belhavencs', filename))
...
>>> print(total_size)
>>> p = Path('/Users/haleyharris/Documents/belhavencs')
>>> p.glob(*)
>>> p.glob('*')
<generator object Path.glob at 0x10a87de58>
>>> list(p.glob('*'))
[PosixPath('/Users/haleyharris/Documents/belhavencs/csc121'),
 PosixPath('/Users/haleyharris/Documents/belhavencs/csc111'),
 PosixPath('/Users/haleyharris/Documents/belhavencs/.DS_Store'),
 PosixPath('/Users/haleyharris/Documents/belhavencs/csc211'),
 PosixPath('/Users/haleyharris/Documents/belhavencs/README.md'),
 PosixPath('/Users/haleyharris/Documents/belhavencs/.gitignore'),
 PosixPath('/Users/haleyharris/Documents/belhavencs/csc311'),
 PosixPath('/Users/haleyharris/Documents/belhavencs/csc411'),
 PosixPath('/Users/haleyharris/Documents/belhavencs/.git'),
 PosixPath('/Users/haleyharris/Documents/belhavencs/csc421')]
>>> list(p.glob('*.md'))
[PosixPath('/Users/haleyharris/Documents/belhavencs/README.md')]
>>> list(p.glob('READM?.md'))
[PosixPath('/Users/haleyharris/Documents/belhavencs/README.md')]
>>> p = Path('/Users/haleyharris/Documents/belhavencs/csc311')
>>> list(p.glob('*.py'))
[]
>>> os.listdir('/Users/haleyharris/Documents/belhavencs/csc311')
['lab8',
 'lab1',
 'lab6',
 'lab7',
 'lab0',
 '.DS_Store',
 'final_project',
 'lab5',
 'lab2',
 'lab3',
 'lab4',
 'test_project',
 'haleyharris',
 'haleyharris.zip',
 'completed_features']
>>> p = Path('/Users/haleyharris/Documents/belhavencs/csc311/lab5')
>>> os.listdir(p)
['lab5-pandas-part2.ipynb',
 '.recipeitems-latest.json.icloud',
 'FremontBridge.csv',
 '.names.csv.icloud',
 'lab5-pandas-part2-problem-3.ipynb',
 '.ipynb_checkpoints',
 'lab5-pandas-part2-problem-2.ipynb']
>>> list(p.glob('*.csv'))
[PosixPath('/Users/haleyharris/Documents/belhavencs/csc311/lab5/FremontBridge.csv')]
>>> list(p.glob('*.ipynb'))
[PosixPath('/Users/haleyharris/Documents/belhavencs/csc311/lab5/lab5-pandas-part2.ipynb'),
 PosixPath('/Users/haleyharris/Documents/belhavencs/csc311/lab5/lab5-pandas-part2-problem-3.ipynb'),
 PosixPath('/Users/haleyharris/Documents/belhavencs/csc311/lab5/lab5-pandas-part2-problem-2.ipynb')]
>>> for text_filepath_obj in p.glob('*.ipynb'):
...     print(text_filepath_obj)
...
>>> p.exists()
True
>>> home_dir = Path('/Users/haleyharris')
>>> not_exist_dir = Path('/Users/This/Folder/Does/Not/Exist')
>>> readme_file = Path('Users/haleyharris/Documents/download.png')
>>> home_dir.exists()
True
>>> home_dir.is_dir()
True
>>> not_exist_dir.exists()
False
>>> readme_file.is_file()
False
>>> readme_file = Path('Users/haleyharris/Documents/README.md')
>>> readme_file.is_file()
False
>>> readme_file.is_dir()
False
>>> p = Path('spam.txt')
>>> p.write_text('Hello, world!')
13
>>> p.read_text()
'Hello, world!'
>>> hello_file = open(Path.home()/'hello.txt')
>>> pwd
'/Users/haleyharris/Desktop/belhavencsc/csc221/hw6/ch9/examples'
>>> hello_file = open(Path.home()/'hello.txt')
>>> hello_file = open('hello.txt')
>>> hello_content = hello_file.read()
>>> hello_content = hello_file.read()
>>> hello_file = open('hello.txt')
>>> hello_content = hello_file.read()
>>> hello_file.close()
>>> clear
>>> pwd
'/Users/haleyharris/Desktop/belhavencsc/csc221/hw6/ch9/examples'
>>> hello_file = open('/Users/haleyharris/Desktop/belhavencsc/csc221/hw6/ch9/examples/hello.txt')
>>> hello_content = hello_file.read()
>>> hello_content
'Hello, world!\n'
>>> hello_content
'Hello, world!\n'
>>> hello_file.close()
>>> hello_content
'Hello, world!\n'
>>> hello_file = open('/Users/haleyharris/Desktop/belhavencsc/csc221/hw6/ch9/examples/hello.txt')
>>> hello_file.readlines()
['Hello, world!\n', 'Hello, again\n']
>>> hello_file.write('Hi\n')
>>> hello_file.close()
>>> spam_file = open('spam.txt', 'w')
>>> spam_file.write('Hello, world!\n')
14
>>> spam_file.close()
>>> spam_file = open('spam.txt', 'a')
>>> spam_file.write('Bacon is not a vegetable.')
25
>>> spam_file.close()
>>> spam_file.open('spam.txt')
>>> spam_file = open('spam.txt')
>>> content = spam_file.read()
>>> spam_file.close()
>>> print(content)
>>> import shelve
>>> shelf_file = shelve.open('mydata')
>>> cats = ['Zophie', 'Pooka', 'Simon']
>>> shelf_file['cats'] = cats
>>> shelf_file.close()
>>> shelf_file = shelve.open('mydata')
>>> type(shelf_file)
shelve.DbfilenameShelf
>>> shelf_file['cats']
['Zophie', 'Pooka', 'Simon']
>>> shelf_file.close()
>>> shelf_file = shelve.open('mydata')
>>> list(shelf_file.keys())
['cats']
>>> list(shelf_file.values())
[['Zophie', 'Pooka', 'Simon']]
>>> shelf_file.close()
>>> import pprint
>>> cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
>>> pprint.pformat(cats)
"[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]"
>>> file_obj = open('my_cats.py', 'w')
>>> file_obj.write('cats =' + pprint.pformat(cats) + '\n')
82
>>> file_obj.close()
>>> import my_cats
>>> my_cats.cats
[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]
>>> my_cats.cats[0]
{'desc': 'chubby', 'name': 'Zophie'}
>>> my_cats.cats[0]['name']
'Zophie'
>>> %history -o -p -f shell_examples.py
