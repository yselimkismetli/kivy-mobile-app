# About Sportable 

This application was developed with Kivy, KivyMD and SQLite for to follow sports news, team fixtures, scores and more.

## Overview of application

<img src="https://yavuzselimkismetli.com/kma/k_1.jpg" alt="Overview" style="width: 40%; height: 40%"/>

<img src="https://yavuzselimkismetli.com/kma/k_2.jpg" alt="Overview" style="width: 40%; height: 40%"/>

## Variables of table

- .."Name" : Name of the team/player.
- .."Pos" : Position/rank of the team/player.
- .."W" : Wins.
- .."L" : Loses.
- .."D" : Draws.
- .."P" : Points.

> (fbName, bbPos, vbL, ... They all of are `StringProperty()`)

If you want to manage data on the screens; for the screens `..Screen(Screen) (etc. BBScreen(Screen))` classes are have `on_kv_post(self, base_widget)` methods. In these methods, you can manage all database and other processes. Managing about the screen data for from `..Data(BoxLayout) (etc. BBData(BoxLayout))` classes. Data classes keeps only properties.

### Components

- MDToolbar
- MDNavigationLayout
- MDNavigationDrawer
- MDList
- MDCard

## Requirements

- `kivy = 2.1.0`
- `kivymd = 0.104.2`

Also you can use the requirements.txt file.

> `pip install -r requirements.txt`

## Usage

Download the repo then just run it.

> Also: `Sportable().run()` method for run the application.

### Manage the run process

If you want to manage run process then you can modify `Sportable(MDApp)` class.