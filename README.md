# dev
marge and improvement  
  
lowcostはcut-thetaの処理を高速化するためテキストの書き込みと読み込みをやめ、リストを使用。  
また、縦線を除いた線の角度を取得し、平均を算出  
<br>  
angle.pyは以下を参考  
http://dailyrobottechnology.blogspot.com/2014/11/76python.html　　
<br>
https://kato-robotics.hatenablog.com/entry/2019/02/18/053255　　
<br>
<br>
main.pyを作成したが、実際に動かして見ると横断歩道の奥の比較的０度に近いところが多いところによって思ったより曲がる角度が足りていない  
そのためリストの小さい方からいくつかを除外することにする。
