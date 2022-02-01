import re
import sys
import traceback

from collections import namedtuple

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class PyProcessorCapture(object):
    def __init__(self, default_indent=0):
        self.default_indent = default_indent
        self.reset()

    def out(self, s, end='\n'):
        self._output.append(s + end)


    def indent(self, s, end='\n', indent=None):
        if indent is None:
            indent = self.default_indent


        for line in s.split('\n'):
            self.out(' ' * indent + line)

    def msg(self, m):
        print("Message: ", m)

    def reset(self):
        self._output = []

    def get(self):
        return ''.join(self._output)
Snippet = namedtuple("Snippet", ["position", "length", "code", "indentation"])


def process_repeat_statements(code, prefix='pyp', suffix='ypy'):
    lines = code.split('\n')

    NORMAL = 1
    REPEAT = 2

    output = []
    buff = None
    mode = NORMAL

    prefix = prefix + 'repeat'
    suffix = suffix + 'repeat'

    to_be_replaced = None
    replacement_values = None


    for line in lines:
        if line.startswith(prefix):
            assert mode == NORMAL
            splitted = [ t for t in line.split(' ') if t != '']
            assert splitted[0] == prefix
            to_be_replaced = splitted[1]
            assert splitted[2] == 'in'
            expression = ' '.join(splitted[3:])
            replacement_values = eval(expression)
            assert type(replacement_values) == list
            for val in replacement_values:
                assert type(val) == str
            buff = []
            mode = REPEAT
        elif line.startswith(suffix):
            assert mode == REPEAT

            for val in replacement_values:
                for line in buff:
                    output.append(line.replace(to_be_replaced, val))
            buff               = None
            to_be_replaced     = None
            replacement_values = None
            mode               = NORMAL
        else:
            if mode == NORMAL:
                output.append(line)
            elif mode == REPEAT:
                buff.append(line)
    assert mode == NORMAL, "Unfinished REPEAT statement business."

    return '\n'.join(output)



def process_snippet(code, prefix, suffix):
    lines = code.split('\n')
    indentation = lines[0].index(prefix)
    for i in range(len(lines)):
            lines[i] = lines[i][indentation:]

    return indentation, '\n'.join(lines[1:-1])

def process_inline_snippet(code, prefix, suffix):
    lines = code.split('\n')
    indentation = lines[0].index(prefix)
    function = lines[0][indentation + len(prefix) + len("inline") + 1:]
    if len(lines) > 2:
        lines = [line[indentation:] for line in lines[1:-1]]

        code = function + '"""' + '\n'.join(lines) + '""")'
        return indentation, code
    else:
        return indentation, function

def process_source(pyp_source, prefix="pyp", suffix = "ypy"):
    assert not prefix in suffix and not suffix in prefix

    pyp_source = process_repeat_statements(pyp_source)

    pyp_pattern = re.compile(r'(?!\n)\ *(?s)' + prefix + r'\s.*?' + suffix, re.MULTILINE)
    pyp_inline_pattern = re.compile(r'(^|(?!\n))\ *(?s)' + prefix + r'inline\s.*?' + suffix, re.MULTILINE)

    pyp_snippets = []
    for match in pyp_pattern.finditer(pyp_source):
        position = match.start()
        length = len(match.group())
        indentation, code = process_snippet(match.group(), prefix, suffix)
        pyp_snippets.append(Snippet(position, length, code, indentation))

    for match in pyp_inline_pattern.finditer(pyp_source):
        position = match.start()
        length = len(match.group())
        indentation, code = process_inline_snippet(match.group(), prefix, suffix)
        pyp_snippets.append(Snippet(position, length, code, indentation))

    # make sure the code snippets get executed in order
    pyp_snippets = sorted(pyp_snippets, key=lambda x: x.position)

    pyp_outputs = []

    pyp = PyProcessorCapture()
    variable_space = {'pyp': pyp}


    last_end = 0

    modified_source = ''

    encountered_error = False

    for i, snippet in enumerate(pyp_snippets):
        pyp.reset()
        pyp.default_indent = snippet.indentation
        try:
            exec(snippet.code, variable_space)
        except Exception as e:
            encountered_error = True
            print("Exception executing snippet: ", e)
            print(bcolors.FAIL)
            print(snippet.code)
            print(bcolors.ENDC)
            print('=== STACK TRACE ===')
            traceback.print_exc()
            print('===================')

        modified_source = modified_source + pyp_source[last_end:snippet.position]
        last_end = snippet.position + snippet.length

        modified_source = modified_source + pyp.get()

    modified_source = modified_source + pyp_source[last_end:]

    if encountered_error:
        raise Exception("Error while executing preprocessor")

    return modified_source


def process_file(pyp_filepath, prefix="pyp", suffix = "ypy"):
    with open(pyp_filepath) as pyp_f:
        pyp_source = pyp_f.read()
    return process_source(pyp_source, prefix=prefix, suffix=suffix)
