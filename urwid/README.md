# Hello Urwid

A simple Terminal User Interface (TUI) application built with [Urwid](http://urwid.org/), demonstrating basic features of the framework.

## Features

- Interactive buttons with click handling
- Counter functionality
- Keyboard shortcuts
- Custom color palette
- Centered layout

## Requirements

- Python 3.x
- urwid 2.2.3

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python hello.py
```

### Controls

- Use arrow keys to navigate
- Press Enter to select a button
- Press 'q' to quit the application

## Key Differences from Textual

Urwid has some distinct characteristics:
- More low-level control over widgets
- Lighter weight
- Longer history (more mature)
- Different widget composition model
- Different approach to styling

Both Urwid and Textual are excellent choices for TUI applications, with different strengths and trade-offs.
