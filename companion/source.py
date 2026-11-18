"""Counter-Strike 2 game-state receiver for the player's own virtual ammo HUD."""
import hmac,time
from serve import page
INTERVAL=0
def ingest(o,m,event):
    token=o.get("token")
    if not token or not hmac.compare_digest(str(event.get("auth",{}).get("token","")),str(token)):raise PermissionError()
    player=event.get("player") or {};items=player.get("weapons") or {}
    active=next((w for w in items.values() if w.get("state")=="active"),{})
    def count(k):
        v=active.get(k)
        return v if type(v) is int and v>=0 else None
    m.update(clip=count("ammo_clip"),reserve=count("ammo_reserve"),capacity=count("ammo_clip_max"),
             item=str(active.get("name","")).removeprefix("weapon_")[:24],seen=time.monotonic())
def snapshot(o,m):
    if not m or time.monotonic()-m["seen"]>30:
        return dict(state="Awaiting game event",key="idle",pages=[page("VIRTUAL HUD","Stand by","Start CS2 with GSI enabled","Player weapons only")])
    clip=m["clip"];reserve=m["reserve"];cap=m["capacity"]
    return dict(state="Game feed / active item",key=m["item"]+str(clip),alert=clip==0,pages=[
      page("GAME AMMO","--" if clip is None else clip,m["item"] or "No active item","Reserve "+("--" if reserve is None else str(reserve)),fraction=clip/cap if clip is not None and cap else None),
      page("GAME RESERVE","--" if reserve is None else reserve,"Ammo for the active item","Game State Integration")])
