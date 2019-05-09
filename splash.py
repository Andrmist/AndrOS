import time
from sys import stdout
class Splash:

    def header_screen_writer(self):
        # time.sleep(5)
        print("""
Cesvet Team
       CCCCC     EEEEEE     SSSSSSSS     V         V     EEEEEE     TTTTTTTTT
       C         E          S             V       V      E              T
       C         EEEEEE     SSSSSSSS       V     V       EEEEEE         T
       C         E                 S        V   V        E              T
       C         E                 S         V V         E              T
       CCCCC     EEEEEE     SSSSSSSS          V          EEEEEE         T

STARTING THE MACHINE...
        """)
        time.sleep(1)

        print('Starting AndrOS...')
        time.sleep(2)
        print('Loading plugins:')


    def logo_and_change_log_writer(self):
        icon = '''                              tt%:
  .  . .  .  . .  .  . .  .  tt;tS:  . .  .  . .  .  . ;888X
   .       .       .       ..%t;t;8 .      .       . X@S8 8888%
     .  .    .  .    .  .   8;tS;t;X   . .    . .    88XSt; 8 8t
 .       .       .       . ;%t8;tttS..      .     . % @     .%S
   .  .    .  .    .  .   .Xt%  S;t;8   .  .   .    8 .      88
  .    .  .    .  .    .  Xt;tS  Xt;tX       .   . .. 8..     8t
    .       .       .    :S;ttX: ttt;S:  .            t%; :8X8 :
  .   . .    .  .    .   8;t8%t8  X;tt@   . .  .   .. ;8X888S
    .     .    .  .    .%;tS. @t%  Xt;tS      .  .    ;t.888
  .    .   .       .   .@t;%  .8S. ttt;X:  .        . %S88888
     .   .   .  .    . 8;;S    .X8  X;t;8    . .      8% ;%;
  .    .      .   .   ;;tX  .   :tS  S;ttS       .  .:.X %8
    .     . .   .   . 8ttt   .  .@X: %t;tX: .  .      . 88X8@
  .   .           .  Xt;% .    .  88  Xt;t8      .  . :.t:   X
    .   . .  . .    .ttX   .      .%% .St;t%. .       S88 t88
  .         .    .  8;tt .   .  .  SX. %;t;X.   .  .  88888.
     . .  .    .   St;S       .     88  @;t;8        .
  .          .    ;%;8  . . .    .   8X  8tt;@. . .          .
    .  . . .    . 8;t: .       .   . :;. ;t;t;:     .         .
  .           .  tt;8     .  .   .    88  @;tt8  .
    . .  .  .   :St@ .  .      .    .  @X  @t;t8              .
  .       .   . @t;;   .   . .    .    ;;. ;t;t;. .  .
     . .       :%;8  .   .      .    .  88  8;tt8            .
  .      . . ..@;%%t::;.    .      :::;t%tX .8;t;X .  .   .    .
    .  .      Xtt;t;;tt;t;;tt;;t;;t;t;t;tt;. ;t;t;.     .   .
  .      .  ..S;S8888888888888888888888888X8  8;t;8  .    .   .
    . .      8tt; .  .          .  .  .   .XX..@;ttX   .
  .     .  .tt;8             .             :;. tt;t;;    .  .
     .    . @;S:    .   .  .     .        . 88. 8;;t8  .     .
  .    .   8;t%  .    .   .   .    . . .    .@X .@t;t8    .
    .    .:;t8     .    .      .         .   t%..t;tttt     .  .
  .   .   8;tt  .    .     . .   . .  .   .   @8. 8t;tS; .
    .   .8;t8 .   .    .  .            .    . t;S .Xt;tX.  .  .
  .     %;t;.   .   .   .    . . .  .    .     @%. %t;t;8.
     . ;St;8      .   .    .       .  .    .   Xt8  8t;t;X  .  .
  .   :St;t: . .    .    .    .  .      .    . .ttX .X;t;t8
X888X%;t;t;tSX@8888SS; .    .       .;XS8888@XSt;ttSS%;t;t;%S@8@'''
        print(icon)
        print(open('changelog.txt', 'r').read())
