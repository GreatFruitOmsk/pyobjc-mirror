from scanner import *
from textwrap import dedent


SUBPATTERNS = dict(
    AVAILABLE=r'(?:AVAILABLE_\w+)',
    KEYWORD=r'((?:double|float|int|unsigned|long|char|extern|volatile|void|inline|__(?:\w+?)__|const|typedef|static|const))',
    IDENTIFIER=r'([A-Za-z_]\w*)',
    SIZEOF=r'(?:sizeof\(([^)]+)\))',
    DECIMAL=r'(?:[+\-]?\d*(?:\.\d*)?(?:[eE]\d+)?[fF]?)',
    INTEGER=r'(?:[+\-]?\d*[uU]?[lL]?)',
    CHARS=r"(?:'(?:[^\\'\n]|\\')*')",
    STRING=r'(?:"(?:[^\\"\n]|\\")*")',
    CFSTRING=r'(?:CFSTR\("(?:[^\\"\n]|\\")*"\))',
    HEX=r'(?:0[xX][0-9a-fA-F]+[lL]?)',
    EXTERN=r'(?:(?:(?:[A-Z-a-z_]\w*?_)?EXTERN|extern))',
    EXPORT=r'(?:(?:(?:[A-Z-a-z_]\w*?_)?EXPORT|extern))',
    STATIC_INLINE=r'(?:(?:(?:[A-Z-a-z_]\w*?_)?INLINE|static inline|static __inline__))',
    INDIRECTION=r'(?:\s*\*)',
    BOL=r'(?:\s*^\s*)',
    EOL=r'(?:\s*$\n?)',
    SEMI=r';\s*',
)

def deadspace(string, begin, end):
    return 'NO MATCH FOR [%d:%d] %r' % (begin, end, string[begin:end])

def pattern(s):
    return dedent(s).strip() % SUBPATTERNS

def example(s):
    return dedent(s).strip()

class BlockComment(Token):
    pattern = pattern(r'''
    \s*
    \/\*
    (?P<comment>([^*]|\*(?!/))*)
    \*\/
    ''')
    example = example('''
    /*************\t\tThis is an annoying one\t\t**********/
    /* this is a block comment */
    ''')

class SingleLineComment(Token):
    pattern = pattern(r'\s*//(?P<comment>[^\n]*)(\n|$)')
    example = example(r'// this is a single line comment')

class InsignificantWhitespace(IgnoreToken):
    pattern = pattern(r'''\s+''')
    example = example('  \t\n\r   ')

class UninterestingTypedef(Token):
    pattern = pattern(r'''
    typedef
    \s*(?P<body>[^;]*)
    %(SEMI)s
    ''')
    example = example('''
    typedef baz wibble fun* SomethingGreat;
    ''')

class CompilerDirective(Token):
    pattern = pattern(r'''
    \s*
    \#(?P<name>undef|if|ifdef|ifndef|endif|else|elif|pragma|error|warn|define)
    \s*(?P<body>([^\\\n]|\\(\n|$))*)
    ''')
    example = example(r'''
    #if defined(foo)
    #if \
        insane
    #endif
    #else stuff
    #define NS_DURING { \
        GARBAGE!  blah blah {
    ''')

class Interface(Token):
    pattern = pattern(r'''
    @interface
        \s+(?P<name>%(IDENTIFIER)s)
        \s*(?:\((?P<category>%(IDENTIFIER)s)\))?
        \s*(?::\s*(?P<super>%(IDENTIFIER)s))?
        \s*(?:<(?P<protocols>[^>]*)>)?
        \s*(?:{(?P<ivars>[^}])})?
        \s*(?P<interface_body>.*?)
    @end
    %(EOL)s
    ''')
    example = example(r'''
    @interface Foo(Bar): Baz <protocols> {
    @private
        NSArray *crazy;
    }

    + (Foo *)newFoo;
    - init;
    @end
    ''')

class Protocol(Token):
    pattern = pattern(r'''
    @protocol
        \s+(?P<name>%(IDENTIFIER)s)
        \s*(?:<(?P<super>%(IDENTIFIER)s)>)?
        \s*(?P<protocol_body>.*?)
    @end
    %(EOL)s
    ''')
    example = example(r'''
    @protocol FooProtocol <Foo>
    + (Foo *)protoFoo;
    @end
    ''')

class AngleImport(Token):
    pattern = pattern(r'''
    \#\s*(?P<import_type>import|include)
        \s+<(?P<import_file>[^>]*)>
    %(EOL)s
    ''')
    example = example('#import <Foo/Bar.h>')

class StringImport(Token):
    pattern = pattern(r'''
    \#\s*(?P<import_type>import|include)
        \s+"(?P<import_file>[^"]*)"
    %(EOL)s
    ''')
    example = example('#import "Foo/Bar.h"')

class SimpleDefine(Token):
    # XXX foo << bar
    # XXX foo | bar | baz
    # XXX ((type)foo)
    pattern = pattern(r'''
    \#\s*define\s*
        (?P<name>%(IDENTIFIER)s)\s+
        \(?(?P<value>
            (?!%(KEYWORD)s)%(IDENTIFIER)s
            | %(HEX)s
            | %(INTEGER)s
            | %(DECIMAL)s
            | %(CHARS)s
            | %(STRING)s
            | %(CFSTRING)s
            | %(SIZEOF)s
        )\)?
    %(EOL)s
    ''')
    example = example(r'''
    #define foo bar
    #define foo 0x200
    #define foo 2.0
    #define foo 'foo!'
    #define foo "foo"
    #define foo CFSTR("foo")
    #define foo sizeof(bar)
    #define foo (8)
    ''')
    
class MacroDefine(Token):
    pattern = pattern(r'''
    \s*\#\s*define\s*
        (?P<name>%(IDENTIFIER)s)
        \s*\(
            (?P<args>
                (\s*%(IDENTIFIER)s\s*,)*
                (\s*%(IDENTIFIER)s\s*)?
            )
        \)
    \s*(?P<body>([^\\\n]|\\(\n|$))*)
    ''')
    example = example(r'''
    #define NSLocalizedString(key, comment) \
        [[NSBundle mainBundle] localizedStringForKey:(key) value:@"" table:nil]
    #define GetNSApp() [NSApplication sharedApplication]
    #define DoStuff(a, b, c) do { \
        blah blah blah \
        blah blah blah \
    } while (0);
    ''')

class GlobalThing(Token):
    pattern = pattern(r'''
    (?:%(EXTERN)s|%(EXPORT)s)\s+
    (const\s+)?
    (?P<type>%(IDENTIFIER)s%(INDIRECTION)s*)
    \s*(const\s+)?
    (?P<name>%(IDENTIFIER)s)(?:\s*\[\s*\]\s*|\b)
    (?:\s+%(AVAILABLE)s)?
    %(SEMI)s
    ''')
    example = example(r'''
    extern const double FooBar;
    extern const NSString *foo;
    extern NSString *foo;
    APPKIT_EXTERN NSString* const foo;
    FOUNDATION_EXPORT NSString * const Foo;
    extern CFStringRef cfFoo AVAILABLE_MAC_OSX_10_8;
    APPKIT_EXTERN const char foosball[] AVAILABLE_NEVER;
    ''')

class ForwardClassReference(Token):
    pattern = pattern(r'@class (?P<name>[^;]+)%(SEMI)s')
    example = example(r'@class Foo;')

class EnumBareMember(Token):
    pattern = pattern(r'''
    \s*(?P<name>%(IDENTIFIER)s)
    \s*,?
    ''')
    example = example(r'''
    Foo,
    Foo
    ''')

class EnumValueMember(Token):
    pattern = pattern(r'''
    \s*(?P<name>%(IDENTIFIER)s)
    \s*=
    \s*(?P<value>(
        %(INTEGER)s
        | %(HEX)s
        | %(CHARS)s
        | %(IDENTIFIER)s
        ))
    \s*,?
    ''')
    example = example(r'''
    Foo = 12,
    Foo = 2
    ''')

class NamedEnumEnd(Token):
    pattern = pattern(r'''
    \s*}
    \s*(?P<name>%(IDENTIFIER)s)
    \s*%(SEMI)s
    ''')
    example = example(r'''
    } FooBarBazWible;
    ''')

class NamedEnum(ScanningToken):
    pattern = pattern(r'''
    typedef
    \s+enum
    \s*(?P<name>%(IDENTIFIER)s)?
    \s*{\s*
    ''')
    endtoken = NamedEnumEnd
    lexicon = [
        InsignificantWhitespace,
        BlockComment,
        SingleLineComment,
        EnumValueMember,
        EnumBareMember,
    ]
    example = example(r'''
    typedef enum {
        FooBar = 1, // This is the best value for FooBar
        Baz = 2,
        Wibble
    } FooBarBazWibble;
    typedef enum {
        FooBar, /* But this FooBar has no value! */
        Baz,
        Wibble
    } FooBarBazWibble;
    ''')

class EnumEnd(Token):
    pattern = pattern(r'''
    \s*}
    \s*%(SEMI)s
    ''')
    example = example(r'''
    };
    ''')

class Struct(Token):
    # XXX handle comments? need its own internal parser?
    pattern = pattern(r'''
    struct
    \s*(?P<structname>%(IDENTIFIER)s)?
    \s*{
        (?P<content>[^}]*)
    \s*}
    \s*%(SEMI)s
    ''')
    example = example(r'''
    struct {
        signed foo name;
        int bar;
    };
    struct _FooBarStruct {
        signed foo name;
        int bar;
    };
    ''')

class NamedStruct(Token):
    # XXX handle comments? need its own internal parser?
    pattern = pattern(r'''
    typedef
    \s+struct
    \s*(?P<structname>%(IDENTIFIER)s)?
    \s*{
        (?P<content>[^}]*)
    \s*}
    \s*(?P<name>%(IDENTIFIER)s)
    \s*%(SEMI)s
    ''')
    example = example(r'''
    typedef struct {
        signed foo name;
        int bar;
    } FooBarStruct;
    typedef struct _FooBarStruct {
        signed foo name;
        int bar;
    } FooBarStruct;
    ''')
 
class Enum(ScanningToken):
    pattern = pattern(r'''
    \s*enum
    \s*(?P<name>%(IDENTIFIER)s)?
    \s*{\s*
    ''')
    endtoken = EnumEnd
    lexicon = [
        InsignificantWhitespace,
        BlockComment,
        SingleLineComment,
        EnumValueMember,
        EnumBareMember,
    ]
    example = example(r'''
    enum {
        FooBar = 1, // This is the best value for FooBar
        Baz = 2,
        Wibble
    };
    enum {
        FooBar, /* But this FooBar has no value! */
        Baz,
        Wibble
    };
    ''')

class FunctionEnd(Token):
    # XXX - UNUSED
    pattern = pattern(r'''
    \)
    \s*%(SEMI)s
    ''')
    example = example(r'''
    );
    )  ;
    ''')

class FunctionParameter(Token):
    # XXX - UNUSED
    pattern = pattern(r'''
    (%(IDENTIFIER)s\s*)+
    \s*%(INDIRECTION)s
    \s*%(IDENTIFIER)s?
    \s*,?\s*
    ''')
    example = example(r'''
    NSString *foo, NSString *bar
    ''')

#class ExportFunction(ScanningToken):
#    pattern = pattern(r'''
#    %(EXPORT)s
#    \s*(?P<returns>%(IDENTIFIER)s%(INDIRECTION)s*)
#    \s*%(IDENTIFIER)s
#    \s*\(
#    ''')
#    endtoken = FunctionEnd
#    lexicon = [
#        InsignificantWhitespace,
#        FunctionParameter,
#    ]
#    example = example(r'''
#    FOUNDATION_EXPORT SomeResult **SomeName(const Foo *, const Foo *Bar);
#    FOUNDATION_EXPORT SomeResult SomeName(int,float);
#    ''')

class ExportFunction(Token):
    # XXX handle comments? need its own internal parser?
    pattern = pattern(r'''
    %(EXPORT)s
    \s*(?P<returns>
        (%(KEYWORD)s\s*)*
        %(IDENTIFIER)s
        (%(INDIRECTION)s|\s+%(KEYWORD)s)*
    )
    \s*(?P<name>%(IDENTIFIER)s)
    \s*\(
        (?P<args>\s*[^)]*)
    \s*\)
    \s*%(SEMI)s\s*
    ''')
    example = example(r'''
    FOUNDATION_EXPORT SomeResult **SomeName(const Foo *, const Foo *Bar);
    FOUNDATION_EXPORT SomeResult SomeName(int,float);
    ''')

class StaticInlineFunction(Token):
    # XXX need to figure out how to find a close brace
    #     will probably need something stateful I guess
    pattern = pattern(r'''
    %(STATIC_INLINE)s
    \s*(?P<returns>
        (%(KEYWORD)s\s*)*
        %(IDENTIFIER)s
        (%(INDIRECTION)s|\s+%(KEYWORD)s)*
    )
    \s*(?P<name>%(IDENTIFIER)s)
    \s*\(
        (?P<args>\s*[^)]*)
    \s*\)
    (?P<body>
            \s*{[^}\n]*}(\n|$)
        |
            \s*{([^}\n]|[^\n]}|\n[^}])*\n}
    )\s*
    ''')
    example = example(r'''
    FOUNDATION_STATIC_INLINE BOOL NSDecimalIsNotANumber(const NSDecimal *dcm)
      { return ((dcm->_length == 0) && dcm->_isNegative); }
    FOUNDATION_STATIC_INLINE unsigned short NSSwapShort(unsigned short inv) {
        return CFSwapInt16(inv);
    }
    FOUNDATION_STATIC_INLINE NSSwappedFloat NSConvertHostFloatToSwapped(float x) {
        union fconv {
        float number;
        NSSwappedFloat sf;
        };
        return ((union fconv *)&x)->sf;
    }
    ''')


LEXICON = [
    InsignificantWhitespace,
    BlockComment,
    SingleLineComment,
    Interface,
    Protocol,
    AngleImport,
    SimpleDefine,
    GlobalThing,
    ForwardClassReference,
    NamedEnum,
    Enum,
    NamedStruct,
    Struct,
    ExportFunction,
    StaticInlineFunction,
    UninterestingTypedef,
    MacroDefine,
    CompilerDirective,
]

if __name__ == '__main__':
    from pdb import pm
    import re
    import sys
    #fn = '/System/Library/Frameworks/Foundation.framework/Headers/NSDecimal.h'
    fn = '/System/Library/Frameworks/Foundation.framework/Headers/NSBundle.h'
    files = sys.argv[1:] or [fn]
    def deadraise(string, i, j):
        print string[i:j]
        import pdb
        pdb.Pdb().set_trace()
    scan = Scanner(LEXICON)
    for fn in files:
        for token in scan.iterscan(file(fn).read(), dead=deadraise):
            if token is not None:
                print token
