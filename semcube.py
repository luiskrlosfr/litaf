class semcube:
  def __init__(self):
    self.cube = {
                    #TIPO INT
                    'int':{
                        '+':{
                            'int' : 'int',
                            'flo' : 'flo',
                            'cha' : 'error type mismatch',
                            'str' : 'error type mismathc',
                            'boo' : 'error type mismatch',
                            'void' : 'error type mismatch'
                            },
                        '-':{
                            'int' : 'int',
                            'flo' : 'flo',
                            'cha' : 'error type mismatch',
                            'str' : 'error type mismathc',
                            'boo' : 'error type mismatch',
                            'void' : 'error type mismatch'
                            },
                        '*':{
                            'int' : 'int',
                            'flo' : 'flo',
                            'cha' : 'error type mismatch',
                            'str' : 'error type mismathc',
                            'boo' : 'error type mismatch',
                            'void' : 'error type mismatch'
                        },
                        '/':{
                            'int' : 'int',
                            'flo' : 'flo',
                            'cha' : 'error type mismatch',
                            'str' : 'error type mismathc',
                            'boo' : 'error type mismatch',
                            'void' : 'error type mismatch'
                        },
                        '=':{
                            'int' : 'int',
                            'flo' : 'error type mysmatch',
                            'cha' : 'error type mismatch',
                            'str' : 'error type mismathc',
                            'boo' : 'error type mismatch',
                            'void' : 'error type mismatch'
                        },
                        '==':{
                            'int' : 'boo',
                            'flo' : 'boo',
                            'cha' : 'boo',
                            'str' : 'boo',
                            'boo' : 'boo',
                            'void' : 'boo'
                        },
                        '<':{
                            'int' : 'boo',
                            'flo' : 'boo',
                            'cha' : 'error type mismatch',
                            'boo' : 'error type mismatch',
                            'str' : 'error type mismatch',
                            'void' : 'error type mismatch'

                        },
                        '>':{
                            'int' : 'boo',
                            'flo' : 'boo',
                            'cha' : 'error type mismatch',
                            'str' : 'error type mismatch',
                            'boo' : 'error type mismatch',
                            'void' : 'error type mismatch'
                        },
                        '<=':{
                            'int' : 'boo',
                            'flo' : 'boo',
                            'cha' : 'error type mismatch',
                            'boo' : 'error type mismatch',
                            'str' : 'error type mismatch',
                            'void' : 'error type mismatch'

                        },
                        '>=':{
                            'int' : 'boo',
                            'flo' : 'boo',
                            'cha' : 'error type mismatch',
                            'str' : 'error type mismatch',
                            'boo' : 'error type mismatch',
                            'void' : 'error type mismatch'
                        },
                        '!=':{
                            'int' : 'boo',
                            'flo' : 'boo',
                            'cha' : 'error type mismatch',
                            'str' : 'error type mismatch',
                            'boo' : 'error type mismatch',
                            'void' : 'error type mismatch'
                        },
                        '||':{
                            'int' : 'operator error',
                            'flo' : 'operator error',
                            'cha' : 'operator error',
                            'str' : 'operator error',
                            'boo' : 'error type mismatch',
                            'void' : 'operator error'
                        },
                        '&&':{
                            'int' : 'operator error',
                            'flo' : 'operator error',
                            'cha' : 'operator error',
                            'str' : 'operator error',
                            'boo' : 'error type mismatch',
                            'void' : 'operator error'
                        }
                    },
                    ## TIPO FLOAT
                    'flo':{
                        '+':{
                            'int' : 'flo',
                            'flo' : 'flo',
                            'cha' : 'error type mismatch',
                            'str' : 'error type mismathc',
                            'boo' : 'error type mismatch',
                            'void' : 'error type mismatch'
                            },
                        '-':{
                            'int' : 'flo',
                            'flo' : 'flo',
                            'cha' : 'error type mismatch',
                            'str' : 'error type mismathc',
                            'boo' : 'error type mismatch',
                            'void' : 'error type mismatch'
                            },
                        '*':{
                            'int' : 'flo',
                            'flo' : 'flo',
                            'cha' : 'error type mismatch',
                            'str' : 'error type mismathc',
                            'boo' : 'error type mismatch',
                            'void' : 'error type mismatch'
                        },
                        '/':{
                            'int' : 'error type mismatch',
                            'flo' : 'flo',
                            'cha' : 'error type mismatch',
                            'str' : 'error type mismathc',
                            'boo' : 'error type mismatch',
                            'void' : 'error type mismatch'
                        },
                        '=':{
                            'int' : 'flo',
                            'flo' : 'flo',
                            'cha' : 'error type mismatch',
                            'str' : 'error type mismathc',
                            'boo' : 'error type mismatch',
                            'void' : 'error type mismatch'
                        },
                        '==':{
                            'int' : 'boo'
                            'flo' : 'boo'
                            'int' : 'boo',
                            'flo' : 'boo',
                            'cha' : 'boo',
                            'str' : 'boo',
                            'boo' : 'boo',
                            'void' : 'boo'
                        },
                        '<':{
                            'int' : 'boo',
                            'flo' : 'boo',
                            'cha' : 'error type mismatch',
                            'boo' : 'error type mismatch',
                            'str' : 'error type mismatch',
                            'void' : 'error type mismatch'

                        },
                        '>':{
                            'int' : 'boo',
                            'flo' : 'boo',
                            'cha' : 'error type mismatch'
                            'str' : 'error type mismatch'
                            'boo' : 'error type mismatch'
                            'void' : 'error type mismatch'
                        },
                        '<=':{
                            'int' : 'boo',
                            'flo' : 'boo',
                            'cha' : 'error type mismatch',
                            'boo' : 'error type mismatch',
                            'str' : 'error type mismatch',
                            'void' : 'error type mismatch'

                        },
                        '>=':{
                            'int' : 'boo',
                            'flo' : 'boo',
                            'cha' : 'error type mismatch'
                            'str' : 'error type mismatch'
                            'boo' : 'error type mismatch'
                            'void' : 'error type mismatch'
                        },
                        '!=':{
                            'int' : 'boo',
                            'flo' : 'boo',
                            'cha' : 'error type mismatch'
                            'str' : 'error type mismatch'
                            'boo' : 'error type mismatch'
                            'void' : 'error type mismatch'
                        },
                        '||':{
                            'int' : 'operator error',
                            'flo' : 'operator error',
                            'cha' : 'operator error'
                            'str' : 'operator error'
                            'boo' : 'error type mismatch'
                            'void' : 'operator error'
                        },
                        '&&':{
                            'int' : 'operator error',
                            'flo' : 'operator error',
                            'cha' : 'operator error'
                            'str' : 'operator error'
                            'boo' : 'error type mismatch'
                            'void' : 'operator error'
                        }
                    },
                    #TIPO CHA
                    'cha':{
                        '+':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'error type mismatch',
                            'str' : 'error type mismathc',
                            'boo' : 'error type mismatch',
                            'void' : 'error type mismatch'
                            },
                        '-':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'error type mismatch',
                            'str' : 'error type mismathc',
                            'boo' : 'error type mismatch',
                            'void' : 'error type mismatch'
                            },
                        '*':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'operator error',
                            'str' : 'operator error',
                            'boo' : 'operator error',
                            'void' : 'operator error'
                        },
                        '/':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'operator error',
                            'str' : 'operator error',
                            'boo' : 'operator error',
                            'void' : 'operator error'
                        },
                        '=':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'cha',
                            'str' : 'error type mismatch',
                            'boo' : 'error type mismatch',
                            'void' : 'operator error'
                        },
                        '==':{
                            'int' : 'boo'
                            'flo' : 'boo'
                            'cha' : 'boo',
                            'boo' : 'boo',
                            'str' : 'boo',
                            'void' : 'boo'
                        },
                        '<':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'boo',
                            'boo' : 'error type mismatch',
                            'str' : 'error type mismatch',
                            'void' : 'error type mismatch'

                        },
                        '>':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'boo'
                            'str' : 'error type mismatch'
                            'boo' : 'error type mismatch'
                            'void' : 'error type mismatch'
                        },
                        '<=':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'boo',
                            'boo' : 'error type mismatch',
                            'str' : 'error type mismatch',
                            'void' : 'error type mismatch'

                        },
                        '>=':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'boo'
                            'str' : 'error type mismatch'
                            'boo' : 'error type mismatch'
                            'void' : 'error type mismatch'
                        },
                        '!=':{
                            'int' : 'boo',
                            'flo' : 'boo',
                            'cha' : 'boo'
                            'str' : 'boo'
                            'boo' : 'boo'
                            'void' : 'boo'
                        },
                        '||':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'error type mismatch'
                            'str' : 'error type mismatch'
                            'boo' : 'error type mismatch'
                            'void' : 'error type mismatch'
                        },
                        '&&':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'error type mismatch'
                            'str' : 'error type mismatch'
                            'boo' : 'error type mismatch'
                            'void' : 'error type mismatch'
                        }
                    },
                    #TIPO STR
                    'str':{
                        '+':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'str',
                            'str' : 'str',
                            'boo' : 'error type mismatch',
                            'void' : 'error type mismatch'
                            },
                        '-':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'error type mismatch',
                            'str' : 'operator error',
                            'boo' : 'error type mismatch',
                            'void' : 'error type mismatch'
                            },
                        '*':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'error type mismatch',
                            'str' : 'operator error',
                            'boo' : 'error type mismatch',
                            'void' : 'error type mismatch'
                        },
                        '/':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'error type mismatch',
                            'str' : 'operator error',
                            'boo' : 'error type mismatch',
                            'void' : 'error type mismatch'
                        },
                        '=':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'str',
                            'str' : 'str',
                            'boo' : 'error type mismatch',
                            'void' : 'error type mismatch'
                        },
                        '==':{
                            'int' : 'boo'
                            'flo' : 'boo'
                            'cha' : 'boo',
                            'boo' : 'boo',
                            'str' : 'boo',
                            'void' : 'boo'
                        },
                        '<':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'operator error',
                            'boo' : 'error type mismatch',
                            'str' : 'operator error',
                            'void' : 'error type mismatch'

                        },
                        '>':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'operator error',
                            'boo' : 'error type mismatch',
                            'str' : 'operator error',
                            'void' : 'error type mismatch'
                        },
                        '<=':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'operator error',
                            'boo' : 'error type mismatch',
                            'str' : 'operator error',
                            'void' : 'error type mismatch'

                        },
                        '>=':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'operator error',
                            'boo' : 'error type mismatch',
                            'str' : 'operator error',
                            'void' : 'error type mismatch'
                        },
                        '!=':{
                            'int' : 'boo',
                            'flo' : 'boo',
                            'cha' : 'boo'
                            'str' : 'boo'
                            'boo' : 'boo'
                            'void' : 'boo'
                        },
                        '||':{
                            'int' : 'operator error',
                            'flo' : 'operator error',
                            'cha' : 'operator error',
                            'boo' : 'error type mismatch',
                            'str' : 'operator error',
                            'void' : 'operator error'
                        },
                        '&&':{
                            'int' : 'operator error',
                            'flo' : 'operator error',
                            'cha' : 'operator error',
                            'boo' : 'error type mismatch',
                            'str' : 'operator error',
                            'void' : 'operator error'
                        }
                    }
                    #TIPO BOO
                    'boo':{
                        '+':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'operator error',
                            'str' : 'error type mismastch',
                            'boo' : 'operator error',
                            'void' : 'operator error'
                            },
                        '-':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'operator error',
                            'str' : 'operator error',
                            'boo' : 'operator error',
                            'void' : 'operator error'
                            },
                        '*':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'operator error',
                            'str' : 'operator error',
                            'boo' : 'operator error',
                            'void' : 'operator error'
                        },
                        '/':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'operator error',
                            'str' : 'operator error',
                            'boo' : 'operator error',
                            'void' : 'operator error'
                        },
                        '=':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'error type mismatch',
                            'str' : 'error type mismatch',
                            'boo' : 'boo',
                            'void' : 'error type mismatch'
                        },
                        '==':{
                            'int' : 'boo'
                            'flo' : 'boo'
                            'cha' : 'boo',
                            'boo' : 'boo',
                            'str' : 'boo',
                            'void' : 'boo'
                        },
                        '<':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'operator error',
                            'boo' : 'operator error',
                            'str' : 'operator error',
                            'void' : 'error type mismatch'

                        },
                        '>':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'operator error',
                            'boo' : 'operator error',
                            'str' : 'operator error',
                            'void' : 'error type mismatch'
                        },
                        '<=':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'operator error',
                            'boo' : 'operator error',
                            'str' : 'operator error',
                            'void' : 'error type mismatch'

                        },
                        '>=':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'operator error',
                            'boo' : 'operator error',
                            'str' : 'operator error',
                            'void' : 'error type mismatch'
                        },
                        '!=':{
                            'int' : 'boo',
                            'flo' : 'boo',
                            'cha' : 'boo'
                            'str' : 'boo'
                            'boo' : 'boo'
                            'void' : 'boo'
                        },
                        '||':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'error type mismatch',
                            'boo' : 'boo',
                            'str' : 'error type mismatch',
                            'void' : 'error type mismatch'
                        },
                        '&&':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'error type mismatch',
                            'boo' : 'boo',
                            'str' : 'error type mismatch',
                            'void' : 'error type mismatch'
                        }
                    },
                    #tipo void
                    'void':{
                        'boo':{
                        '+':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'operator error',
                            'str' : 'error type mismastch',
                            'boo' : 'operator error',
                            'void' : 'operator error'
                            },
                        '-':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'operator error',
                            'str' : 'operator error',
                            'boo' : 'operator error',
                            'void' : 'operator error'
                            },
                        '*':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'operator error',
                            'str' : 'operator error',
                            'boo' : 'operator error',
                            'void' : 'operator error'
                        },
                        '/':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'operator error',
                            'str' : 'operator error',
                            'boo' : 'operator error',
                            'void' : 'operator error'
                        },
                        '=':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'error type mismatch',
                            'str' : 'error type mismatch',
                            'boo' : 'boo',
                            'void' : 'operator error'
                        },
                        '==':{
                            'int' : 'boo'
                            'flo' : 'boo'
                            'cha' : 'boo',
                            'boo' : 'boo',
                            'str' : 'boo',
                            'void' : 'operator error'
                        },
                        '<':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'operator error',
                            'boo' : 'operator error',
                            'str' : 'operator error',
                            'void' : 'operator error'

                        },
                        '>':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'operator error',
                            'boo' : 'operator error',
                            'str' : 'operator error',
                            'void' : 'operator error'
                        },
                        '<=':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'operator error',
                            'boo' : 'operator error',
                            'str' : 'operator error',
                            'void' : 'operator error'

                        },
                        '>=':{
                            'int' : 'error type mismatch',
                            'flo' : 'error type mismatch',
                            'cha' : 'operator error',
                            'boo' : 'operator error',
                            'str' : 'operator error',
                            'void' : 'operator error'
                        },
                        '!=':{
                            'int' : 'boo',
                            'flo' : 'boo',
                            'cha' : 'boo'
                            'str' : 'boo'
                            'boo' : 'boo'
                            'void' : 'boo'
                        },
                        '||':{
                            'int' : 'operator error',
                            'flo' : 'operator error',
                            'cha' : 'operator error',
                            'boo' : 'boo',
                            'str' : 'operator error',
                            'void' : 'operator error'
                        },
                        '&&':{
                            'int' : 'operator error',
                            'flo' : 'operator error',
                            'cha' : 'operator error',
                            'boo' : 'boo',
                            'str' : 'operator error',
                            'void' : 'operator error'
                        }

                    }
                }
