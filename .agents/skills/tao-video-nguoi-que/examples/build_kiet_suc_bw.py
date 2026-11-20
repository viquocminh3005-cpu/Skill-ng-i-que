import json
import sys
P = sys.argv[1] if len(sys.argv) > 1 else "scenes.json"   # scenes.json do `stick.py plan` tạo
d = json.load(open(P, encoding="utf-8"))
d["title"] = {"lines": []}
d.update(look="bw", rough=0.35, boil_fps=0, anim_fps=30,
         subs={"y": 0.775, "size": 0.1, "fix": {}})
d["cast"] = {"me": {"kind": "man", "h": 0.66, "shirt": True},
             "neg": {"kind": "plain", "h": 0.68},
             "fr": {"kind": "woman", "h": 0.62, "dress": True}}
T = [l.split("|") for l in [
 "0|2.85|Tại sao bạn lại cảm thấy kiệt sức sau khi ở cạnh một số người?",
 "2.85|6.9|Tâm lý học cho biết, một vài người sẽ hút cạn năng lượng của bạn nhiều hơn những người khác.",
 "6.9|9.75|Cơ thể bạn thường nhận ra điều đó trước cả tâm trí.",
 "9.75|15.71|Khi ai đó liên tục tiêu cực hoặc luôn chìm trong rắc rối, hệ thần kinh của bạn phải làm việc quá sức để gánh vác cả cảm xúc của họ.",
 "15.71|19.7|Đây được gọi là lao động cảm xúc và nhiều người cam chịu nó mà không hề hay biết."]]
S = []
for i, (s, e, t) in enumerate(T):
    S.append({"i": i + 1, "start": float(s), "end": float(e), "text": t})

# 1: bạn đứng giữa, hai người nói xối xả hai bên, bạn xìu dần
S[0].update(bg={"type": "room", "window": False}, tone="neutral", cam={"zoom": [1.0, 1.08]},
  items=[
   {"type": "prop", "name": "battery", "x": 0.5, "y": 0.2, "s": 0.3, "level": 0.95, "keys": [{"t": "kiệt sức", "level": 0.6, "d": 1.2}]},
   {"id": "neg", "x": 0.23, "y": 0.86, "pose": "angry_point", "expr": "shout", "face": 0.8, "do": ["talk", "jab"]},
   {"type": "prop", "name": "bubble", "x": 0.25, "y": 0.39, "s": 0.24, "content": "scribble", "spiky": True, "tail": [0.02, 0.06]},
   {"id": "fr", "x": 0.79, "y": 0.86, "pose": "shrug", "expr": "worried", "face": -0.8, "do": ["talk"]},
   {"type": "prop", "name": "bubble", "x": 0.78, "y": 0.4, "s": 0.22, "content": "...", "tail": [-0.02, 0.06]},
   {"id": "me", "x": 0.5, "y": 0.88, "pose": "stand", "expr": "neutral", "face": 0, "do": ["breathe"],
    "keys": [{"t": "kiệt sức", "pose": "slump", "expr": "sad", "d": 0.8}, {"t": "một số người", "dark": 0.35, "d": 0.8}]}])

# 2: người tiêu cực (đen) hút ánh sáng từ ngực bạn; xa xa một người bình thường vẫn ấm
S[1].update(bg={"type": "room", "window": False}, tone="cold", cam={"zoom": [1.04, 1.12]},
  items=[
   {"type": "prop", "name": "battery", "x": 0.5, "y": 0.22, "s": 0.34, "level": 0.6, "keys": [{"t": "hút cạn", "level": 0.08, "d": 1.4}]},
   {"type": "prop", "name": "battery", "x": 0.14, "y": 0.5, "s": 0.13, "level": 0.95, "appear": "những người khác-0.3"},
   {"id": "fr", "x": 0.14, "y": 0.8, "h": 0.36, "pose": "wave", "expr": "smile", "face": 0.6, "glow": 0.5, "opacity": 0.7, "do": ["breathe"], "appear": "những người khác-0.3"},
   {"id": "me", "x": 0.36, "y": 0.88, "pose": "stand", "expr": "worried", "face": 0.7, "glow": 0.9, "do": ["breathe"],
    "keys": [{"t": "hút cạn", "glow": 0, "dark": 0.55, "d": 1.4}, {"t": "hút cạn", "pose": "slump", "expr": "sad", "d": 1.4}]},
   {"id": "neg", "x": 0.72, "y": 0.88, "pose": "reach", "expr": "smile", "face": -0.8, "dark": 1, "do": ["breathe"],
    "reach": {"arm": "R", "to": "me.chest", "off": [0, 0.03]}, "reach_w": 0, "keys": [{"t": "một vài người", "reach_w": 1, "d": 1.0}]},
   {"type": "prop", "name": "sparkle", "x": 0.54, "y": 0.6, "s": 0.2, "n": 7, "appear": "hút cạn", "vanish": "nhiều hơn"}])

# 3: cơ thể biết trước: tay ôm ngực, tim đập run, dấu ? trên đầu
S[2].update(bg="paper", tone="neutral", cam={"from": [1.0, 0.5, 0.6], "to": [1.18, 0.5, 0.52]},
  items=[
   {"id": "me", "x": 0.5, "y": 0.86, "pose": "hand_chest", "expr": "worried", "face": 0.2, "dark": 0.25, "do": ["tremble", "breathe"]},
   {"type": "prop", "name": "heart", "x": 0.5, "y": 0.6, "s": 0.14, "beat": 1, "glow": 0.3, "at": "me.chest", "off": [0.0, -0.005]},
   {"type": "prop", "name": "heart", "x": 0.3, "y": 0.27, "s": 0.34, "beat": 1, "appear": 0.3},
   {"type": "prop", "name": "mark", "text": "?", "x": 0.72, "y": 0.27, "s": 0.26, "appear": "tâm trí-0.2"}])

# 4: bạn bè chìm trong mây mưa, nói không ngừng; bạn phải gánh tảng đá cảm xúc của họ
S[3].update(bg={"type": "outdoor", "horizon": 0.6}, tone="cold", cam={"zoom": [1.0, 1.1]},
  items=[
   {"type": "prop", "name": "cloud", "x": 0.66, "y": 0.25, "s": 0.44, "rain": True, "dark": 1, "appear": "tiêu cực"},
   {"id": "fr", "x": 0.74, "y": 0.86, "pose": "cover_face", "expr": "cry", "face": -0.6, "do": ["sob"],
    "keys": [{"t": "rắc rối", "pose": "hands_head", "d": 0.5}]},
   {"type": "prop", "name": "bubble", "x": 0.84, "y": 0.42, "s": 0.22, "content": "scribble", "spiky": True, "tail": [-0.03, 0.05], "appear": "liên tục"},
   {"id": "me", "x": 0.32, "y": 0.86, "pose": "stand", "expr": "worried", "face": 0.7, "do": ["breathe"],
    "keys": [{"t": "gánh vác", "pose": "slump", "d": 0.8}, {"t": "quá sức", "expr": "hurt", "do": ["tremble"], "crack": 0.5, "d": 0.8}]},
   {"type": "prop", "name": "rock", "at": "me.top", "off": [0, 0.012], "s": 0.28, "appear": "hệ thần kinh+0.2", "keys": [{"t": "gánh vác", "s": 0.4, "d": 1.0}]},
   {"type": "prop", "name": "lightning", "x": 0.2, "y": 0.3, "s": 0.18, "appear": "quá sức", "vanish": "gánh vác"}])

# 5: bạn vẫn mỉm cười ngoài mặt nhưng nứt bên trong; phía sau là cả đám đông cam chịu
S[4].update(bg={"type": "field", "horizon": 0.58}, tone="dark", cam={"from": [1.15, 0.5, 0.58], "to": [1.0, 0.5, 0.55]},
  items=[
   {"type": "prop", "name": "battery", "x": 0.5, "y": 0.2, "s": 0.3, "level": 0.3, "keys": [{"t": "cam chịu", "level": 0.1, "d": 1.0}]},
   {"type": "crowd", "layout": "rows", "n": 12, "h": 0.32, "cx": 0.5, "y": 0.66, "rows": 2, "w": 0.9, "depth_y": 0.06,
    "pose": "slump", "expr": "sad", "dark": 0.6, "do": ["breathe"], "appear": "nhiều người-0.2"},
   {"id": "me", "x": 0.5, "y": 0.9, "h": 0.7, "pose": "relaxed", "expr": "smile", "face": 0, "dark": 0.3, "crack": 0, "do": ["breathe"],
    "keys": [{"t": "lao động cảm xúc", "crack": 0.8, "d": 1.2}, {"t": "cam chịu", "pose": "slump", "d": 1.0}, {"t": "không hề", "expr": "sad", "dark": 0.6, "d": 1.0}]}])

d["scenes"] = S
json.dump(d, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok")
