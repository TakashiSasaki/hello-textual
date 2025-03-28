from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Button, DirectoryTree
from textual.containers import Container, Horizontal
from textual.widgets import Tree
import os

class HelloWorld(App):
    """A simple Textual app that says hello."""

    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("q", "quit", "Quit application")
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Horizontal(
            DirectoryTree(".", id="directory-tree"),
            Container(
                Static("ようこそ Textual へ!", id="welcome"),
                Static("選択したパス: なし", id="path-display"),
                Button("クリックしてね!", id="btn"),
                id="main",
            )
        )
        yield Footer()

    def on_directory_tree_file_selected(self, event: DirectoryTree.FileSelected) -> None:
        """ファイルが選択されたときのハンドラ"""
        path = event.path
        self.query_one("#path-display").update(f"選択したパス: {path}")

    def on_directory_tree_directory_selected(self, event: DirectoryTree.DirectorySelected) -> None:
        """ディレクトリが選択されたときのハンドラ"""
        path = event.path
        self.query_one("#path-display").update(f"選択したディレクトリ: {path}")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed."""
        button = event.button
        if button.id == "btn":
            self.query_one("#welcome").update("ボタンがクリックされました!")

if __name__ == "__main__":
    app = HelloWorld()
    app.run()
