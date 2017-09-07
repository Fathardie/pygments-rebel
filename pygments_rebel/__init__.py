"""
    Rebel lexer
    ~~~~~~~~~~~

    Pygments lexer for Ruby + RSpec.

    :copyright: Copyright 2012 Hugo Maia Vieira
    :license: BSD, see LICENSE for details.
"""

from pygments.lexer import RegexLexer, bygroups
from pygments.token import *

class RebelLexer(RegexLexer):
    name = 'Rebel'
    aliases = ['rebel']
    filenames = ['*.ebl']

    tokens = {
        'root':
            [ (r'module', Keyword.Reserved, 'module_spec')
            , (r'import', Keyword.Reserved, 'module_spec')
            , (r'specification', Keyword.Reserved)
            , (r'fields', Keyword.Reserved, 'fields')
            , (r'invariants?', Keyword.Reserved)
            , (r'lifeCycle', Keyword.Reserved)
            , (r'events', Keyword.Reserved)
            , (r'event', Keyword.Reserved)
            , (r'preconditions', Keyword.Reserved)
            , (r'postconditions', Keyword.Reserved)
            , (r'new', Keyword.Reserved)
            , (r'this.', Keyword.Reserved)
            , (r'function', Keyword.Reserved)
            , (r'initial\s', Keyword.Reserved)
            , (r'final\s', Keyword.Reserved)

            , (r'EUR', Number) # Currency

            , (r'@doc\s*\{[^\}]+\}', Comment.Multiline)

            , (r'@\w+', Name.Decorator) # Annotation

            , (r'(\s|\n)+', Whitespace) # Skip all whitespace

            , (r'[a-z][A-Za-z]*', Name.Variable)
            , (r'[A-Z][a-zA-Z]*', Keyword.Type)
            , (r'[0-9]+(,[0-9][0-9][0-9])*(\.[0-9]*)?%?', Number)

            , (r';', Text) # Statements ending with ;
            , (r'\{', Text)
            , (r'\}', Text)
            , (r'[-+*\^=<>]+', Operator)
            , (r'[\][]', Text)
            , (r'\(', Text)
            , (r'\)', Text)
            , (r'\->', Text)
            , (r',', Operator)
            , (r':', Operator)
            ],
        'module_spec':
            [ (r'\n', Whitespace, '#pop')
            , (r'\s+', Whitespace)
            , (r'(\w|.)+', Text)
            ],
        'fields':
            [ (r'\{', Text)
            , (r'([a-z][A-Za-z]*)(\s*)(:)(\s*)([A-Z][a-zA-Z]*)', bygroups(Name.Variable, Whitespace, Text, Whitespace, Keyword.Type))
            , (r'@\w+', Name.Decorator) # Annotation
            , (r'\}', Text, '#pop')
            , (r'(\s|\n)+', Whitespace)  # Skip all whitespace
            ]
    }