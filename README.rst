|PyPI| |license|

prettype
========

An easy to use text stylizer for your desktop!

.. figure:: https://media.giphy.com/media/xWBEn6avkyGib7ynG2/giphy.gif
   :alt: 

Installation
------------

-  To install ``prettype``, simply,

   ::

       $ pip install prettype

Supported unicode fonts
-----------------------

::

          Serif-Normal        PRETTYPE
           Serif-Bold         𝐏𝐑𝐄𝐓𝐓𝐘𝐏𝐄
          Serif-Italic        𝑃𝑅𝐸𝑇𝑇𝑌𝑃𝐸
        Serif-Bold-Italic     𝑷𝑹𝑬𝑻𝑻𝒀𝑷𝑬
        Sans-Serif-Normal     𝖯𝖱𝖤𝖳𝖳𝖸𝖯𝖤
         Sans-Serif-Bold      𝗣𝗥𝗘𝗧𝗧𝗬𝗣𝗘
        Sans-Serif-Italic     𝘗𝘙𝘌𝘛𝘛𝘠𝘗𝘌
     Sans-Serif-Bold-Italic   𝙋𝙍𝙀𝙏𝙏𝙔𝙋𝙀
       Calligraphy-Normal     𝒫ℛℰ𝒯𝒯𝒴𝒫ℰ
        Calligraphy-Bold      𝓟𝓡𝓔𝓣𝓣𝓨𝓟𝓔
         Fraktur-Normal       𝔓ℜ𝔈𝔗𝔗𝔜𝔓𝔈
          Fraktur-Bold        𝕻𝕽𝕰𝕿𝕿𝖄𝕻𝕰
            Monospace         𝙿𝚁𝙴𝚃𝚃𝚈𝙿𝙴
          Double-Struck       ℙℝ𝔼𝕋𝕋𝕐ℙ𝔼
         Inverse-Squared      🅿🆁🅴🆃🆃🆈🅿🅴
             Squared          🄿🅁🄴🅃🅃🅈🄿🄴
         Inverse-Circled      🅟🅡🅔🅣🅣🅨🅟🅔
             Circled          ⓅⓇⒺⓉⓉⓎⓅⒺ
          Paranthesized       ⒫⒭⒠⒯⒯⒴⒫⒠

Usage
-----

-  To run ``prettype``, open terminal and run this command:

   ::

       $ prettype

**Note:** Leave this terminal open as long as you want to use
**prettype**.

-  To stylize any text,

   -  select it
   -  press the key binding (``ctrl``\ +\ ``space`` by default) to open
      font selector
   -  select the font you want to stylize your text with using the GUI
   -  the stylized text gets copied to your clipboard
   -  press ``ctrl``\ +\ ``v`` to paste the stylized text wherever you
      want!

-  To close prettype, just press the exit key (``esc`` by default).

-  **CLI usage to configure key binding and exit key:**

   ::

       $ prettype [-h] [-b key1 key2] [-e key]

   You can always use ``$ prettype -h`` command to open this help
   message:

   ::

       optional arguments:
       -h, --help            show this help message and exit
       -b key1 key2, --binding key1 key2
                           Set a key binding for triggering prettype font
                           selector. Example: $ prettype -b ctrl space
       -e key, --exit_key key
                           Specify a key which stops the keyboard listener, when
                           pressed. Example: $ prettype -e esc

.. |PyPI| image:: https://img.shields.io/badge/PyPi-v1.0.0-f39f37.svg
   :target: https://pypi.python.org/pypi/clix
.. |license| image:: https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000
   :target: https://github.com/nikhilkumarsingh/clix/blob/master/LICENSE.txt
