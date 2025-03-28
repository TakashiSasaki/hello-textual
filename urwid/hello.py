#!/usr/bin/env python

import urwid

class MenuButton(urwid.Button):
    def __init__(self, caption, callback):
        super().__init__("")
        urwid.connect_signal(self, 'click', callback)
        self._w = urwid.AttrMap(urwid.SelectableIcon(
            [u'  \N{BULLET} ', caption], 2),
            None, 'highlighted')

class SubMenu(urwid.WidgetWrap):
    def __init__(self):
        self.welcome = urwid.Text('ようこそ urwid へ!')
        self.counter = 0
        self.counter_text = urwid.Text('クリック回数: 0')
        
        # メニューボタンを作成
        increment_button = MenuButton('カウントアップ', self.on_increment)
        quit_button = MenuButton('終了', self.on_quit)
        
        # レイアウトを構築
        pile = urwid.Pile([
            urwid.Divider(),
            self.welcome,
            urwid.Divider(),
            self.counter_text,
            urwid.Divider(),
            increment_button,
            quit_button
        ])
        
        # 中央寄せにする
        self.top = urwid.Filler(pile, 'middle')
        super().__init__(self.top)

    def on_increment(self, button):
        self.counter += 1
        self.counter_text.set_text(f'クリック回数: {self.counter}')

    def on_quit(self, button):
        raise urwid.ExitMainLoop()

class Application:
    def __init__(self):
        self.menu = SubMenu()
        # パレットの定義（色設定）
        self.palette = [
            ('highlighted', 'black', 'yellow'),
            ('body', 'black', 'light gray'),
            ('quit', 'light red', 'black'),
        ]
        
    def run(self):
        # メインループの実行
        self.loop = urwid.MainLoop(
            urwid.AttrMap(self.menu, 'body'),
            self.palette,
            unhandled_input=self.handle_input
        )
        self.loop.run()
        
    def handle_input(self, key):
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()

if __name__ == '__main__':
    app = Application()
    app.run()
