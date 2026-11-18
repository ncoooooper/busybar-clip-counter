# Clip Counter

Turn the active item's virtual magazine and reserve in Counter-Strike 2 into a desktop HUD.

Copy companion/gamestate_integration_busybar.cfg into the game's csgo/cfg folder and set the same local token in it and in config.json. The game posts player_weapons events to the companion at /event. Only the current item, clip and reserve reach the bar. A knife or item without ammo shows --. When the game stops sending events the HUD goes to standby. A game on another PC must use the reachable private LAN address of the companion.

## Connect the bar

Copy companion/example.json to a private config.json and adjust it for your source. From the project folder run `python3 companion/serve.py --config config.json`. Use Python 3.10+. Set Local companion URL to `http://127.0.0.1:8770/reading` on the emulator and allow local port 8770. On hardware, bind the companion to a trusted LAN interface and set its reachable address. The wheel browses pages. Click refreshes. Start pins or unpins the current page. The last good reading is labeled offline after a source error.

## Run locally

From this folder, run `~/.busy-emulator/bin/busy-emulator dev --once` with BUSY Bar Emulator open. Back exits.

![BUSY Bar front display](screenshots/front-1.png)
