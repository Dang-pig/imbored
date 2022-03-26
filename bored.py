import time
print("Welcome to the 'im-bored' show!")
print("I'll show you a bunch of random things for a while.")
p = input("Press Enter to continue...")
prints = ["""
i'm bored""", """
i'm bored""", """
i'm bored""", """
i'm bored""", """
i'm bored""", """
i'm bored""", """
i'm bored""", """
i'm bored""", """
i'm bored""", """
i'm bored""", """
 i'm bored""",
"""
  i'm bored""",
"""
   i'm bored""",
"""
    i'm bored""",
"""
     i'm bored""",
    """
      i'm bored""",
    """
       i'm bored""",
    """
        i'm bored""",
    """
         i'm bored""",
        """
          i'm bored""",
        """
           i'm bored""",
        """
            i'm bored""",
        """
             i'm bored""",
            """
              i'm bored""",
            """
               i'm bored""",
            """
                i'm bored""",
            """
                 i'm bored""",
                """
                  i'm bored""",
                """
                   i'm bored""",
                """
                    i'm bored""",
                """
                     i'm bored""",
                    """
                      i'm bore""",
                    """
                        i'm bo""",
                    """
                         i'm b""",
                        """
                          i'm """,
                        """
                           i'm""",
                        """
                            i'""",
                        """
                             i""",
                            """
                            i'""",
                        """
                           i'm""",
                        """
                          i'm """,
                        """
                         i'm b""",
                        """
                        i'm bo""",
                    """
                       i'm bor""",
                    """
                      i'm bore""",
                    """
                     i'm bored""",
                    """
                    i'm bored""",
                """
                   i'm bored""",
                """
                  i'm bored""",
                """
                 i'm bored""",
                """
                i'm bored""",
            """
               i'm bored""",
            """
              i'm bored""",
            """
             i'm bored""",
            """
            i'm bored""",
        """
           i'm bored""",
        """
          i'm bored""",
        """
         i'm bored""",
        """
        i'm bored""",
    """
       i'm bored""",
    """
      i'm bored""",
    """
     i'm bored""",
    """
    i'm bored""",
"""
   i'm bored""",
"""
  i'm bored""",
"""
 i'm bored""", """
i'm bored""", """
i'm bore""", """
i'm bor""", """
i'm bo""", """
i'm b""", """
i'm """, """
i'""", """
i""", """
""", """
i""", """
i'""", """
i'm """, """
i'm b""", """
i'm bo""", """
i'm bor""", """
i'm bore""", """
i'm bored""", """
 i'm bored""",
"""
  i'm bored""",
"""
   i'm bored""",
"""
    i'm bored""",
"""
     i'm bored""",
    """
      i'm bored""",
    """
       i'm bored""",
    """
        i'm bored""",
    """
         i'm bored""",
        """
          i'm bored""",
        """
           i'm bored""",
        """
            i'm bored""",
        """
             i'm bored""",
            """
              i'm bored""",
            """
               i'm bored""",
            """
                i'm bored""",
            """
                 i'm bored""",
                """
                  i'm bored""",
                """
                   i'm bored""",
                """
                    i'm bored""",
                """
                     i'm bored""",
                    """
                      i'm bore""",
                    """
                        i'm bo""",
                    """
                         i'm b""",
                        """
                          i'm """,
                        """
                           i'm""",
                        """
                            i'""",
                        """
                             i""",
                            """
                            i'""",
                        """
                           i'm""",
                        """
                          i'm """,
                        """
                         i'm b""",
                        """
                        i'm bo""",
                    """
                       i'm bor""",
                    """
                      i'm bore""",
                    """
                     i'm bored""",
                    """
                    i'm bored""",
                """
                   i'm bored""",
                """
                  i'm bored""",
                """
                 i'm bored""",
                """
                i'm bored""",
            """
               i'm bored""",
            """
              i'm bored""",
            """
             i'm bored""",
            """
            i'm bored""",
        """
           i'm bored""",
        """
          i'm bored""",
        """
         i'm bored""",
        """
        i'm bored""",
    """
       i'm bored""",
    """
      i'm bored""",
    """
     i'm bored""",
    """
    i'm bored""",
"""
   i'm bored""",
"""
  i'm bored""",
"""
 i'm bored""", """
i'm bored""", """
i'm bore d""", """
i'm bore  d""", """
i'm bore   d""", """
i'm bore    d""", """
i'm bore     d""", """
i'm bore      d""", """
i'm bore       d""", """
i'm bore        d""", """
i'm bore         d""", """
i'm bore          d""", """
i'm bore           d""", """
i'm bore            d""", """
i'm bore             d""", """
i'm bore              d""", """
i'm bore               d""", """
i'm bore                d""", """
i'm bore                 d""", """
i'm bore                  d""", """
i'm bore                   d""", """
i'm bore                    d""", """
i'm bor e                    d""", """
i'm bor  e                   d""", """
i'm bor   e                  d""", """
i'm bor    e                 d""", """
i'm bor     e                d""", """
i'm bor      e               d""", """
i'm bor       e              d""", """
i'm bor        e             d""", """
i'm bor         e            d""", """
i'm bor          e           d""", """
i'm bor           e          d""", """
i'm bor            e         d""", """
i'm bor             e        d""", """
i'm bor              e       d""", """
i'm bor               e      d""", """
i'm bor                e     d""", """
i'm bor                 e    d""", """
i'm bor                  e   d""", """
i'm bor                   e  d""", """
i'm bor                    e d""", """
i'm bor                     ed""", """
i'm bo r                    ed""", """
i'm bo  r                   ed""", """
i'm bo   r                  ed""", """
i'm bo    r                 ed""", """
i'm bo     r                ed""", """
i'm bo      r               ed""", """
i'm bo       r              ed""", """
i'm bo        r             ed""", """
i'm bo         r            ed""", """
i'm bo          r           ed""", """
i'm bo           r          ed""", """
i'm bo            r         ed""", """
i'm bo             r        ed""", """
i'm bo              r       ed""", """
i'm bo               r      ed""", """
i'm bo                r     ed""", """
i'm bo                 r    ed""", """
i'm bo                  r   ed""", """
i'm bo                   r  ed""", """
i'm bo                    r ed""", """
i'm bo                     red""", """
i'm b o                    red""", """
i'm b  o                   red""", """
i'm b   o                  red""", """
i'm b    o                 red""", """
i'm b     o                red""", """
i'm b      o               red""", """
i'm b       o              red""", """
i'm b        o             red""", """
i'm b         o            red""", """
i'm b          o           red""", """
i'm b           o          red""", """
i'm b            o         red""", """
i'm b             o        red""", """
i'm b              o       red""", """
i'm b               o      red""", """
i'm b                o     red""", """
i'm b                 o    red""", """
i'm b                  o   red""", """
i'm b                   o  red""", """
i'm b                    o red""", """
i'm b                     ored""", """
i'm  b                    ored""", """
i'm   b                   ored""", """
i'm    b                  ored""", """
i'm     b                 ored""", """
i'm      b                ored""", """
i'm       b               ored""", """
i'm        b              ored""", """
i'm         b             ored""", """
i'm          b            ored""", """
i'm           b           ored""", """
i'm            b          ored""", """
i'm             b         ored""", """
i'm              b        ored""", """
i'm               b       ored""", """
i'm                b      ored""", """
i'm                 b     ored""", """
i'm                  b    ored""", """
i'm                   b   ored""", """
i'm                    b  ored""", """
i'm                     b ored""", """
i'm                      bored""", """
i' m                     bored""", """
i'  m                    bored""", """
i'   m                   bored""", """
i'    m                  bored""", """
i'     m                 bored""", """
i'      m                bored""", """
i'       m               bored""", """
i'        m              bored""", """
i'         m             bored""", """
i'          m            bored""", """
i'           m           bored""", """
i'            m          bored""", """
i'             m         bored""", """
i'              m        bored""", """
i'               m       bored""", """
i'                m      bored""", """
i'                 m     bored""", """
i'                  m    bored""", """
i'                   m   bored""", """
i'                    m  bored""", """
i'                     m bored""", """
i'                      mbored""", """
i '                     mbored""", """
i  '                    mbored""", """
i   '                   mbored""", """
i    '                  mbored""", """
i     '                 mbored""", """
i      '                mbored""", """
i       '               mbored""", """
i        '              mbored""", """
i         '             mbored""", """
i          '            mbored""", """
i           '           mbored""", """
i            '          mbored""", """
i             '         mbored""", """
i              '        mbored""", """
i               '       mbored""", """
i                '      mbored""", """
i                 '     mbored""", """
i                  '    mbored""", """
i                   '   mbored""", """
i                    '  mbored""", """
i                     ' mbored""", """
i                      'mbored""", """
 i                     'mbored""", """
  i                    'mbored""", """
   i                   'mbored""", """
    i                  'mbored""", """
     i                 'mbored""", """
      i                'mbored""", """
       i               'mbored""", """
        i              'mbored""", """
         i             'mbored""", """
          i            'mbored""", """
           i           'mbored""", """
            i          'mbored""", """
             i         'mbored""", """
              i        'mbored""", """
               i       'mbored""", """
                i      'mbored""", """
                 i     'mbored""", """
                  i    'mbored""", """
                   i   'mbored""", """
                    i  'mbored""", """
                     i 'mbored""", """
                      i'mbored""", """
                     i 'mbored""", """
                    i  'mbored""", """
                   i   'mbored""", """
                  i    'mbored""", """
                 i     'mbored""", """
                i      'mbored""", """
               i       'mbored""", """
              i        'mbored""", """
             i         'mbored""", """
            i          'mbored""", """
           i           'mbored""", """
          i            'mbored""", """
         i             'mbored""", """
        i              'mbored""", """
       i               'mbored""", """
      i                'mbored""", """
     i                 'mbored""", """
    i                  'mbored""", """
   i                   'mbored""", """
  i                    'mbored""", """
 i                     'mbored""", """
i                      'mbored""", """
i                     ' mbored""", """
i                    '  mbored""", """
i                   '   mbored""", """
i                  '    mbored""", """
i                 '     mbored""", """
i                '      mbored""", """
i               '       mbored""", """
i              '        mbored""", """
i             '         mbored""", """
i            '          mbored""", """
i           '           mbored""", """
i          '            mbored""", """
i         '             mbored""", """
i        '              mbored""", """
i       '               mbored""", """
i      '                mbored""", """
i     '                 mbored""", """
i    '                  mbored""", """
i   '                   mbored""", """
i  '                    mbored""", """
i '                     mbored""", """
i'                     m bored""", """
i'                    m  bored""", """
i'                   m   bored""", """
i'                  m    bored""", """
i'                 m     bored""", """
i'                m      bored""", """
i'               m       bored""", """
i'              m        bored""", """
i'             m         bored""", """
i'            m          bored""", """
i'           m           bored""", """
i'          m            bored""", """
i'         m             bored""", """
i'        m              bored""", """
i'       m               bored""", """
i'      m                bored""", """
i'     m                 bored""", """
i'    m                  bored""", """
i'   m                   bored""", """
i'  m                    bored""", """
i' m                     bored""", """
i'm                     b ored""", """
i'm                    b  ored""", """
i'm                   b   ored""", """
i'm                  b    ored""", """
i'm                 b     ored""", """
i'm                b      ored""", """
i'm               b       ored""", """
i'm              b        ored""", """
i'm             b         ored""", """
i'm            b          ored""", """
i'm           b           ored""", """
i'm          b            ored""", """
i'm         b             ored""", """
i'm        b              ored""", """
i'm       b               ored""", """
i'm      b                ored""", """
i'm     b                 ored""", """
i'm    b                  ored""", """
i'm   b                   ored""", """
i'm  b                    ored""", """
i'm b                     ored""", """
i'm b                    o red""", """
i'm b                   o  red""", """
i'm b                  o   red""", """
i'm b                 o    red""", """
i'm b                o     red""", """
i'm b               o      red""", """
i'm b              o       red""", """
i'm b             o        red""", """
i'm b            o         red""", """
i'm b           o          red""", """
i'm b          o           red""", """
i'm b         o            red""", """
i'm b        o             red""", """
i'm b       o              red""", """
i'm b      o               red""", """
i'm b     o                red""", """
i'm b    o                 red""", """
i'm b   o                  red""", """
i'm b  o                   red""", """
i'm b o                    red""", """
i'm bo                   r  ed""", """
i'm bo                  r   ed""", """
i'm bo                 r    ed""", """
i'm bo                r     ed""", """
i'm bo               r      ed""", """
i'm bo              r       ed""", """
i'm bo             r        ed""", """
i'm bo            r         ed""", """
i'm bo           r          ed""", """
i'm bo          r           ed""", """
i'm bo         r            ed""", """
i'm bo        r             ed""", """
i'm bo       r              ed""", """
i'm bo      r               ed""", """
i'm bo     r                ed""", """
i'm bo    r                 ed""", """
i'm bo   r                  ed""", """
i'm bo  r                   ed""", """
i'm bo r                    ed""", """
i'm bor                    e d""", """
i'm bor                   e  d""", """
i'm bor                  e   d""", """
i'm bor                 e    d""", """
i'm bor                e     d""", """
i'm bor               e      d""", """
i'm bor              e       d""", """
i'm bor             e        d""", """
i'm bor            e         d""", """
i'm bor           e          d""", """
i'm bor          e           d""", """
i'm bor         e            d""", """
i'm bor        e             d""", """
i'm bor       e              d""", """
i'm bor      e               d""", """
i'm bor     e                d""", """
i'm bor    e                 d""", """
i'm bor   e                  d""", """
i'm bor  e                   d""", """
i'm bor e                    d""", """
i'm bore                     d""", """
i'm bore                    d""", """
i'm bore                   d""", """
i'm bore                  d""", """
i'm bore                 d""", """
i'm bore                d""", """
i'm bore               d""", """
i'm bore              d""", """
i'm bore             d""", """
i'm bore            d""", """
i'm bore           d""", """
i'm bore          d""", """
i'm bore         d""", """
i'm bore        d""", """
i'm bore       d""", """
i'm bore      d""", """
i'm bore     d""", """
i'm bore    d""", """
i'm bore   d""", """
i'm bore  d""", """
i'm bore d""", """
i'm bored""", """
i'm bored""", """
i'm bored""", """
i'm bored""", """
i'm bored""", """
i'm bored""", """
i'm bored""", """
i'm bored""", """
i'm bored""", """
i'm bored""", """
i'm bored""", """
i'm bored""", """
 i'm bored""",
"""
  i'm bored""",
"""
   i'm bored""",
"""
    i'm bored""",
"""
     i'm bored""",
    """
      i'm bored""",
    """
       i'm bored""",
    """
        i'm bored""",
    """
         i'm bored""",
        """
          i'm bored""",
        """
           i'm bored""",
        """
            i'm bored""",
        """
             i'm bored""",
            """
              i'm bored""",
            """
               i'm bored""",
            """
                i'm bored""",
            """
                 i'm bored""",
                """
                  i'm bored""",
                """
                   i'm bored""",
                """
                    i'm bored""",
                """
                     i'm bored""",
                    """
                      i'm bore""",
                    """
                        i'm bo""",
                    """
                         i'm b""",
                        """
                          i'm """,
                        """
                           i'm""",
                        """
                            i'""",
                        """
                             i""",
                            """
                            i'""",
                        """
                           i'm""",
                        """
                          i'm """,
                        """
                         i'm b""",
                        """
                        i'm bo""",
                    """
                       i'm bor""",
                    """
                      i'm bore""",
                    """
                     i'm bored""",
                    """
                    i'm bored""",
                """
                   i'm bored""",
                """
                  i'm bored""",
                """
                 i'm bored""",
                """
                i'm bored""",
            """
               i'm bored""",
            """
              i'm bored""",
            """
             i'm bored""",
            """
            i'm bored""",
        """
           i'm bored""",
        """
          i'm bored""",
        """
         i'm bored""",
        """
        i'm bored""",
    """
       i'm bored""",
    """
      i'm bored""",
    """
     i'm bored""",
    """
    i'm bored""",
"""
   i'm bored""",
"""
  i'm bored""",
"""
 i'm bored""", """
i'm bored""", """
i'm bore""", """
i'm bor""", """
i'm bo""", """
i'm b""", """
i'm """, """
i'""", """
i""", """
""", """
i""", """
i'""", """
i'm """, """
i'm b""", """
i'm bo""", """
i'm bor""", """
i'm bore""", """
i'm bored""", """
 i'm bored""",
"""
  i'm bored""",
"""
   i'm bored""",
"""
    i'm bored""",
"""
     i'm bored""",
    """
      i'm bored""",
    """
       i'm bored""",
    """
        i'm bored""",
    """
         i'm bored""",
        """
          i'm bored""",
        """
           i'm bored""",
        """
            i'm bored""",
        """
             i'm bored""",
            """
              i'm bored""",
            """
               i'm bored""",
            """
                i'm bored""",
            """
                 i'm bored""",
                """
                  i'm bored""",
                """
                   i'm bored""",
                """
                    i'm bored""",
                """
                     i'm bored""",
                    """
                      i'm bore""",
                    """
                        i'm bo""",
                    """
                         i'm b""",
                        """
                          i'm """,
                        """
                           i'm""",
                        """
                            i'""",
                        """
                             i""",
                            """
                            i'""",
                        """
                           i'm""",
                        """
                          i'm """,
                        """
                         i'm b""",
                        """
                        i'm bo""",
                    """
                       i'm bor""",
                    """
                      i'm bore""",
                    """
                     i'm bored""",
                    """
                    i'm bored""",
                """
                   i'm bored""",
                """
                  i'm bored""",
                """
                 i'm bored""",
                """
                i'm bored""",
            """
               i'm bored""",
            """
              i'm bored""",
            """
             i'm bored""",
            """
            i'm bored""",
        """
           i'm bored""",
        """
          i'm bored""",
        """
         i'm bored""",
        """
        i'm bored""",
    """
       i'm bored""",
    """
      i'm bored""",
    """
     i'm bored""",
    """
    i'm bored""",
"""
   i'm bored""",
"""
  i'm bored""",
"""
 i'm bored""",
"""
i'm bored""", """
i'm bore d""", """
i'm bor e d""", """
i'm bo r e d""", """
i'm b o r e d""", """
i' m b o r e d""", """
i ' m b o r e d""", """
 i ' m b o r e d""", """
  i ' m b o r e d""", """
   i ' m b o r e d""", """
    i ' m b o r e d""", """
     i ' m b o r e d""", """
      i ' m b o r e d""", """
       i ' m b o r e d""", """
        i ' m b o r e d""", """
         i ' m b o r e d""", """
          i ' m b o r e d""", """
           i ' m b o r e d""", """
            i ' m b o r e d""", """
             i ' m b o r e d""", """
               i ' m b o r ed""", """
                i ' m b o red""", """
                 i ' m b ored""", """
                  i ' m bored""", """
                   i 'm bored""", """
                    i'm bored""", """
                     i'm bore""", """
                      i'm bor""", """
                       i'm bo""", """
                        i'm b""", """
                         i'm """, """
                          i'm""", """
                           i'""", """
                            i""", """
                             """, """
                            i""", """
                           i'""", """
                          i'm""", """
                         i'm """, """
                        i'm b""", """
                       i'm bo""", """
                      i'm bor""", """
                     i'm bore""", """
                    i'm bored""", """
                   i'm bored""", """
                  i'm bored""", """
                 i'm bored""", """
                i'm bored""", """
               i'm bored""", """
              i'm bored""", """
             i'm bored""", """
            i'm bored""", """
           i'm bored""", """
          i'm bored""", """
         i'm bored""", """
        i'm bored""", """
       i'm bored""", """
      i'm bored""", """
     i'm bored""", """
    i'm bored""", """
   i'm bored""", """
  i'm bored""", """
 i'm bored""", """
i'm bored""", """
 i'm bored""", """
  i'm bored""", """
   i'm bored""", """
    i'm bored""", """
     i'm bored""", """
      i'm bored""", """
       i'm bored""", """
        i'm bored""", """
         i'mbored""", """
        i'm  bored""", """
       i'm    bored""", """
       i'm    bored""", """
      i'm      bored""", """
      i'm      bored""", """
     i'm        bored""", """
     i'm        bored""", """
    i'm          bored""", """
    i'm          bored""", """
   i'm            bored""", """
   i'm            bored""", """
  i'm              bored""", """
  i'm              bored""", """
 i'm                bored""", """
 i'm                bored""", """
i'm                  bored""", """
i'm                  bored""", """
i'm                  bored""", """
i'm                  bored""", """
 i'm                bored""", """
 i'm                bored""", """
  i'm              bored""", """
  i'm              bored""", """
   i'm            bored""", """
   i'm            bored""", """
    i'm          bored""", """
    i'm          bored""", """
     i'm        bored""", """
     i'm        bored""", """
      i'm      bored""", """
      i'm      bored""", """
       i'm    bored""", """
       i'm    bored""", """
        i'm  bored""", """
        i'm  bored""", """
         i'mbored""", """
        i'm  bored""", """
       i'm    bored""", """
       i'm    bored""", """
      i'm      bored""", """
      i'm      bored""", """
     i'm        bored""", """
     i'm        bored""", """
    i'm          bored""", """
    i'm          bored""", """
   i'm            bored""", """
   i'm            bored""", """
  i'm              bored""", """
  i'm              bored""", """
 i'm                bored""", """
 i'm                bored""", """
i'm                  bored""", """
i'm                  bored""", """
i'm                  bored""", """
i'm                  bored""", """
 i'm                bored""", """
 i'm                bored""", """
  i'm              bored""", """
  i'm              bored""", """
   i'm            bored""", """
   i'm            bored""", """
    i'm          bored""", """
    i'm          bored""", """
     i'm        bored""", """
     i'm        bored""", """
      i'm      bored""", """
      i'm      bored""", """
       i'm    bored""", """
       i'm    bored""", """
        i'm  bored""", """
        i'm  bored""", """
         i'mbored""", """
        i'm  bored""", """
       i'm    bored""", """
       i'm    bored""", """
      i'm      bored""", """
      i'm      bored""", """
     i'm        bored""", """
     i'm        bored""", """
    i'm          bored""", """
    i'm          bored""", """
   i'm            bored""", """
   i'm            bored""", """
  i'm              bored""", """
  i'm              bored""", """
 i'm                bored""", """
 i'm                bored""", """
i'm                  bored""", """
i'm                  bored""", """
i'm                  bored""", """
i'm                  bored""", """
 i'm                bored""", """
 i'm                bored""", """
  i'm              bored""", """
  i'm              bored""", """
   i'm            bored""", """
   i'm            bored""", """
    i'm          bored""", """
    i'm          bored""", """
     i'm        bored""", """
     i'm        bored""", """
      i'm      bored""", """
      i'm      bored""", """
       i'm    bored""", """
       i'm    bored""", """
        i'm  bored""", """
        i'm  bored""", """
         i'mbored""", """
        i'm bored""", """
         i'm bored""", """
          i'm bored""", """
           i'm bored""", """
            i'm bored""", """
             i'm bored""", """
              i'm bored""", """
               i'm bored""", """
                i'm bored""", """
                 i'm bored""", """
                  i'm bored""", """
                   i'm bored""", """
                    i'm bored""", """
                     i'm bored""", """
                      i'mbored""", """
                     i 'mbored""", """
                    i  'mbored""", """
                   i   'mbored""", """
                  i    'mbored""", """
                 i     'mbored""", """
                i      'mbored""", """
               i       'mbored""", """
              i        'mbored""", """
             i         'mbored""", """
            i          'mbored""", """
           i           'mbored""", """
          i            'mbored""", """
         i             'mbored""", """
        i              'mbored""", """
       i               'mbored""", """
      i                'mbored""", """
     i                 'mbored""", """
    i                  'mbored""", """
   i                   'mbored""", """
  i                    'mbored""", """
 i                     'mbored""", """
i                      'mbored""", """
i                     ' mbored""", """
i                    '  mbored""", """
i                   '   mbored""", """
i                  '    mbored""", """
i                 '     mbored""", """
i                '      mbored""", """
i               '       mbored""", """
i              '        mbored""", """
i             '         mbored""", """
i            '          mbored""", """
i           '           mbored""", """
i          '            mbored""", """
i         '             mbored""", """
i        '              mbored""", """
i       '               mbored""", """
i      '                mbored""", """
i     '                 mbored""", """
i    '                  mbored""", """
i   '                   mbored""", """
i  '                    mbored""", """
i '                     mbored""", """
i'                     m bored""", """
i'                    m  bored""", """
i'                   m   bored""", """
i'                  m    bored""", """
i'                 m     bored""", """
i'                m      bored""", """
i'               m       bored""", """
i'              m        bored""", """
i'             m         bored""", """
i'            m          bored""", """
i'           m           bored""", """
i'          m            bored""", """
i'         m             bored""", """
i'        m              bored""", """
i'       m               bored""", """
i'      m                bored""", """
i'     m                 bored""", """
i'    m                  bored""", """
i'   m                   bored""", """
i'  m                    bored""", """
i' m                     bored""", """
i'm                     b ored""", """
i'm                    b  ored""", """
i'm                   b   ored""", """
i'm                  b    ored""", """
i'm                 b     ored""", """
i'm                b      ored""", """
i'm               b       ored""", """
i'm              b        ored""", """
i'm             b         ored""", """
i'm            b          ored""", """
i'm           b           ored""", """
i'm          b            ored""", """
i'm         b             ored""", """
i'm        b              ored""", """
i'm       b               ored""", """
i'm      b                ored""", """
i'm     b                 ored""", """
i'm    b                  ored""", """
i'm   b                   ored""", """
i'm  b                    ored""", """
i'm b                     ored""", """
i'm b                    o red""", """
i'm b                   o  red""", """
i'm b                  o   red""", """
i'm b                 o    red""", """
i'm b                o     red""", """
i'm b               o      red""", """
i'm b              o       red""", """
i'm b             o        red""", """
i'm b            o         red""", """
i'm b           o          red""", """
i'm b          o           red""", """
i'm b         o            red""", """
i'm b        o             red""", """
i'm b       o              red""", """
i'm b      o               red""", """
i'm b     o                red""", """
i'm b    o                 red""", """
i'm b   o                  red""", """
i'm b  o                   red""", """
i'm b o                    red""", """
i'm bo                   r  ed""", """
i'm bo                  r   ed""", """
i'm bo                 r    ed""", """
i'm bo                r     ed""", """
i'm bo               r      ed""", """
i'm bo              r       ed""", """
i'm bo             r        ed""", """
i'm bo            r         ed""", """
i'm bo           r          ed""", """
i'm bo          r           ed""", """
i'm bo         r            ed""", """
i'm bo        r             ed""", """
i'm bo       r              ed""", """
i'm bo      r               ed""", """
i'm bo     r                ed""", """
i'm bo    r                 ed""", """
i'm bo   r                  ed""", """
i'm bo  r                   ed""", """
i'm bo r                    ed""", """
i'm bor                    e d""", """
i'm bor                   e  d""", """
i'm bor                  e   d""", """
i'm bor                 e    d""", """
i'm bor                e     d""", """
i'm bor               e      d""", """
i'm bor              e       d""", """
i'm bor             e        d""", """
i'm bor            e         d""", """
i'm bor           e          d""", """
i'm bor          e           d""", """
i'm bor         e            d""", """
i'm bor        e             d""", """
i'm bor       e              d""", """
i'm bor      e               d""", """
i'm bor     e                d""", """
i'm bor    e                 d""", """
i'm bor   e                  d""", """
i'm bor  e                   d""", """
i'm bor e                    d""", """
i'm bore                     d""", """
i'm bore                    d""", """
i'm bore                   d""", """
i'm bore                  d""", """
i'm bore                 d""", """
i'm bore                d""", """
i'm bore               d""", """
i'm bore              d""", """
i'm bore             d""", """
i'm bore            d""", """
i'm bore           d""", """
i'm bore          d""", """
i'm bore         d""", """
i'm bore        d""", """
i'm bore       d""", """
i'm bore      d""", """
i'm bore     d""", """
i'm bore    d""", """
i'm bore   d""", """
i'm bore  d""", """
i'm bore d""", """
i'm bored""", """
i'm bored""", """
i'm bored""", """
i'm bored""", """
i'm bored""", """
i'm bored""", """
i'm bored""", """
i'm bored""", """
i'm bored""", """
i'm bored""", """
i'm bored""", """
i'm bored"""
]
ans = ''


def pr(ans):
  for i in range(len(prints)):
    print(prints[i])
    time.sleep(0.02)
  print("It's the end of my 'im-bored' show!")
  print("Hope you like it!")
  ask()


def ask():
  ans = input("Do you want to watch again? (y/n)")
  if ans == 'y':
    pr()
  elif ans == 'n':
    print("Bye!")
    exit()
  else:
    print("Press y or n")
    ask()
pr(ans)